"""Summary numbers for the register, crosswalk, scorecard and reliability check.

Prints the counts and shares, and writes computed columns back into data/:
the three query_ columns in crosswalk.csv, assessable_dimensions, total and
meets_threshold in scorecard.csv, and the agree_ columns in reliability.csv.
The pass threshold is read from standard/rubric.md. Run scripts/validate_csv.py
first. Standard library only.

    python scripts/stats.py
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DIMENSIONS = [
    "indicator_validity", "validation_evidence", "logging", "data_lineage",
    "access_ownership", "tamper_evidence", "disclosure",
]
THRESHOLD_PARAMS = ["pass_max_na", "pass_max_zero_dimensions", "pass_min_total", "not_assessable_min_na"]


def load(name):
    with (DATA / name).open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if any((v or "").strip() for v in r.values())]
        return list(reader.fieldnames or []), rows


def save(name, header, rows):
    if not rows:
        return
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def yn(flag):
    return "yes" if flag else "no"


def pct(n, total):
    return f"{100 * n / total:.1f}%" if total else "n/a"


def shares(title, values):
    print(f"  by {title}:")
    if not values:
        print("    (no rows)")
        return
    for value, n in Counter(values).most_common():
        print(f"    {value or '(empty)'}: {n} ({pct(n, len(values))})")


def read_threshold():
    text = (ROOT / "standard" / "rubric.md").read_text(encoding="utf-8")
    found = dict(re.findall(r"^\|\s*`(\w+)`\s*\|\s*(\d+)\s*\|", text, flags=re.M))
    missing = [p for p in THRESHOLD_PARAMS if p not in found]
    if missing:
        sys.exit(f"standard/rubric.md threshold table is missing: {', '.join(missing)}")
    return {p: int(found[p]) for p in THRESHOLD_PARAMS}


def products_section(products):
    comparators = [p for p in products if p["comparator"] == "yes"]
    print("PRODUCTS")
    print(f"  products: {len(products) - len(comparators)} dairy, {len(comparators)} comparator")
    return {p["product_id"] for p in comparators}


def claims_section(products, claims):
    print("\nCLAIMS")
    print(f"  total claims: {len(claims)}")
    per_product = Counter(c["product_id"] for c in claims)
    print("  claims per product:")
    if not products:
        print("    (no products)")
    for p in products:
        print(f"    {p['product_id']} {p['vendor']} {p['product']}: {per_product[p['product_id']]}")
    shares("claim_type", [c["claim_type"] for c in claims])
    shares("mapping_confidence", [c["mapping_confidence"] for c in claims])
    shares("evidence_cited", [c["evidence_cited"] for c in claims])
    flagged = sum(c["legal_flag"] == "cap_3_7_unsubstantiated" for c in claims)
    print(f"  claims with legal_flag cap_3_7_unsubstantiated: {flagged} ({pct(flagged, len(claims))})")


def count(value):
    return int(value) if value.strip().isdigit() else 0


def crosswalk_section(header, rows):
    print("\nCROSSWALK")
    print(f"  rows: {len(rows)}")
    by_indicator = defaultdict(list)
    for row in rows:
        by_indicator[row["indicator_id"]].append(row)

    for group in by_indicator.values():
        direct = any(count(r["products_measuring_direct"]) > 0 for r in group)
        proxy = any(count(r["products_measuring_proxy"]) > 0 for r in group)
        required_anywhere = any(r["requirement_text"].strip() for r in group)
        required_by_farm = any(r["scheme"] == "FARM_v5" and r["requirement_text"].strip() for r in group)
        externally_validated = any(r["any_external_validation"] == "yes" for r in group)
        for r in group:
            r["query_shortlist"] = yn(direct and required_by_farm)
            r["query_instrumented_not_required"] = yn((direct or proxy) and not required_anywhere)
            r["query_required_manual_only"] = yn(
                bool(r["requirement_text"].strip())
                and r["audit_method"] == "visual_inspection"
                and externally_validated
            )
    save("crosswalk.csv", header, rows)

    def listing(column, per_row=False):
        hits = [r for r in rows if r[column] == "yes"]
        if per_row:
            return sorted(f"{r['indicator_id']} ({r['scheme']})" for r in hits)
        return sorted({r["indicator_id"] for r in hits})

    for label, items in [
        ("shortlist (measured directly, required by FARM v5)", listing("query_shortlist")),
        ("instrumented but required by no scheme", listing("query_instrumented_not_required")),
        ("required, visual inspection only, validated sensor exists", listing("query_required_manual_only", per_row=True)),
    ]:
        print(f"  {label}: {len(items)}")
        for item in items:
            print(f"    {item}")


def scorecard_section(header, rows, comparator_ids):
    t = read_threshold()
    print("\nSCORECARD")
    print(f"  threshold from rubric.md: {t}")
    for row in rows:
        scores = [row[d] for d in DIMENSIONS]
        bad = [s for s in scores if s not in {"0", "1", "2", "NA"}]
        if bad:
            sys.exit(f"scorecard row {row['product_id']} has invalid scores {bad}; run validate_csv.py")
        numeric = [int(s) for s in scores if s != "NA"]
        na = len(scores) - len(numeric)
        row["assessable_dimensions"] = str(len(numeric))
        row["total"] = str(sum(numeric))
        if na >= t["not_assessable_min_na"]:
            row["meets_threshold"] = "not_assessable"
        else:
            row["meets_threshold"] = yn(
                na <= t["pass_max_na"]
                and numeric.count(0) <= t["pass_max_zero_dimensions"]
                and sum(numeric) >= t["pass_min_total"]
            )
    save("scorecard.csv", header, rows)

    for label, group in [
        ("dairy", [r for r in rows if r["product_id"] not in comparator_ids]),
        ("comparator", [r for r in rows if r["product_id"] in comparator_ids]),
    ]:
        assessable = [r for r in group if r["meets_threshold"] != "not_assessable"]
        meeting = [r for r in assessable if r["meets_threshold"] == "yes"]
        print(f"  {label}: {len(group)} scored, {len(assessable)} assessable, "
              f"{len(meeting)} of those meet the standard")

    dairy = [r for r in rows if r["product_id"] not in comparator_ids]
    print("  distribution per dimension, dairy only (0 / 1 / 2 / NA):")
    for d in DIMENSIONS:
        c = Counter(r[d] for r in dairy)
        print(f"    {d}: {c['0']} / {c['1']} / {c['2']} / {c['NA']}")


def reliability_section(header, rows):
    print("\nRELIABILITY")
    for row in rows:
        original = row["coder_a_original"].strip()
        recode, second = row["coder_a_recode"].strip(), row["coder_b"].strip()
        row["agree_a_a"] = yn(original == recode) if recode else ""
        row["agree_a_b"] = yn(original == second) if second else ""
    save("reliability.csv", header, rows)
    if not rows:
        print("  (no rows)")
        return
    print("  percentage agreement per field (coder A re code, coder B):")
    by_field = defaultdict(list)
    for row in rows:
        by_field[row["field"]].append(row)
    for field, group in sorted(by_field.items()):
        a_a = [r["agree_a_a"] for r in group if r["agree_a_a"]]
        a_b = [r["agree_a_b"] for r in group if r["agree_a_b"]]
        print(f"    {field}: {pct(a_a.count('yes'), len(a_a))} of {len(a_a)}, "
              f"{pct(a_b.count('yes'), len(a_b))} of {len(a_b)}")


def main():
    _, products = load("products.csv")
    _, claims = load("claims.csv")
    comparator_ids = products_section(products)
    claims_section(products, claims)
    crosswalk_section(*load("crosswalk.csv"))
    scorecard_section(*load("scorecard.csv"), comparator_ids)
    reliability_section(*load("reliability.csv"))


if __name__ == "__main__":
    main()
