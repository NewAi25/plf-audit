"""Validate every CSV in data/ against the schemas in docs/PLF_Repo_Spec_For_ClaudeCode.md.

Prints one line per file, OK or the first error found, and exits non zero if any
file has an error. Standard library only.

    python scripts/validate_csv.py
"""
import csv
import sys
from datetime import date
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

YES_NO = {"yes", "no"}
SCORE = {"0", "1", "2", "NA"}
DIMENSIONS = [
    "indicator_validity", "validation_evidence", "logging", "data_lineage",
    "access_ownership", "tamper_evidence", "disclosure",
]

# header: exact column order. enums: allowed values. optional: fields that may be
# empty (computed by stats.py, or empty by rule). ints: non negative integers.
SCHEMAS = {
    "products.csv": {
        "header": [
            "product_id", "vendor", "product", "sensor_type", "measures_claimed", "species",
            "country", "stygar_listed", "stygar_validation", "icar_validated", "source",
            "marketing_url", "manual_url", "devdocs_url", "patent_urls", "comparator", "notes",
        ],
        "enums": {
            "sensor_type": {"collar_accelerometer", "ear_tag", "bolus", "camera", "milking_system", "other"},
            "stygar_listed": YES_NO,
            "stygar_validation": {"none", "external_self", "external_independent", "not_listed"},
            "icar_validated": YES_NO,
            "source": {"stygar", "icar", "market_scan", "course"},
            "comparator": YES_NO,
        },
        "required": ["product_id", "vendor", "product"],
        "key": ["product_id"],
    },
    "claims.csv": {
        "header": [
            "claim_id", "product_id", "claim_text", "source_url", "source_type", "date_captured",
            "claim_type", "mapped_indicator_id", "mapping_confidence", "evidence_cited",
            "evidence_ref", "legal_flag", "notes",
        ],
        "enums": {
            "source_type": {"marketing_page", "product_manual", "developer_doc", "patent",
                            "peer_reviewed", "press_release", "recorded_talk"},
            "claim_type": {"indicator_claim", "outcome_claim", "accuracy_claim",
                           "compliance_claim", "no_public_documentation"},
            "mapping_confidence": {"direct", "proxy", "none", "unsure"},
            "evidence_cited": {"none", "vendor_internal", "independent_external", "peer_reviewed"},
            "legal_flag": {"none", "cap_3_7_unsubstantiated"},
        },
        "required": ["claim_id", "product_id", "claim_text", "source_url", "date_captured"],
        "key": ["claim_id"],
    },
    "indicators.csv": {
        "header": [
            "indicator_id", "efsa_consequence", "efsa_abm", "wq_principle", "wq_criterion",
            "wq_measure", "maroto_molina_technology", "maroto_molina_feasible", "notes",
        ],
        "enums": {"maroto_molina_feasible": {"yes", "partial", "no", "not_covered"}},
        "required": ["indicator_id"],
        "key": ["indicator_id"],
    },
    "crosswalk.csv": {
        "header": [
            "indicator_id", "scheme", "requirement_text", "numeric_threshold", "audit_method",
            "industry_authored", "products_measuring_direct", "products_measuring_proxy",
            "any_external_validation", "icar_validated_any", "query_shortlist",
            "query_instrumented_not_required", "query_required_manual_only", "notes",
        ],
        "enums": {
            "scheme": {"RSPCA_Assured", "FARM_v5", "GAP_dairy", "Certified_Humane"},
            "audit_method": {"visual_inspection", "records_review", "sensor_accepted", "unspecified"},
            "industry_authored": YES_NO,
            "any_external_validation": YES_NO,
            "icar_validated_any": YES_NO,
            "query_shortlist": YES_NO,
            "query_instrumented_not_required": YES_NO,
            "query_required_manual_only": YES_NO,
        },
        "optional": {"audit_method", "query_shortlist", "query_instrumented_not_required",
                     "query_required_manual_only"},
        "ints": ["products_measuring_direct", "products_measuring_proxy"],
        "required": ["indicator_id"],
        "key": ["indicator_id", "scheme"],
    },
    "scorecard.csv": {
        "header": ["product_id"] + DIMENSIONS + [
            "assessable_dimensions", "total", "meets_threshold", "legal_required_somewhere",
            "evidence_urls", "notes",
        ],
        "enums": dict({d: SCORE for d in DIMENSIONS}, **{
            "meets_threshold": {"yes", "no", "not_assessable"},
            "legal_required_somewhere": YES_NO,
        }),
        "optional": {"meets_threshold", "assessable_dimensions", "total"},
        "ints": ["assessable_dimensions", "total"],
        "required": ["product_id"],
        "key": ["product_id"],
    },
    "reliability.csv": {
        "header": ["claim_id", "field", "coder_a_original", "coder_a_recode", "coder_b",
                   "agree_a_a", "agree_a_b"],
        "enums": {"agree_a_a": YES_NO, "agree_a_b": YES_NO},
        "optional": {"agree_a_a", "agree_a_b"},
        "required": ["claim_id", "field"],
        "key": ["claim_id", "field"],
    },
}


class Invalid(Exception):
    pass


def load(name, schema):
    path = DATA / name
    if not path.exists():
        raise Invalid("file missing")
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] != schema["header"]:
        raise Invalid(f"header does not match schema; expected {','.join(schema['header'])}")
    header = rows[0]
    records = []
    for line, values in enumerate(rows[1:], start=2):
        if not any(v.strip() for v in values):
            continue
        if len(values) != len(header):
            raise Invalid(f"line {line}: {len(values)} fields, header has {len(header)}")
        records.append((line, dict(zip(header, values))))
    return records


def check_rows(name, schema, records):
    optional = schema.get("optional", set())
    seen = set()
    for line, row in records:
        for field in schema["required"]:
            if not row[field].strip():
                raise Invalid(f"line {line}: {field} is empty")
        for field, allowed in schema["enums"].items():
            value = row[field]
            if value == "" and field in optional:
                continue
            if value not in allowed:
                raise Invalid(f"line {line}: {field} = {value!r}, allowed {sorted(allowed)}")
        for field in schema.get("ints", []):
            value = row[field]
            if value == "" and field in optional:
                continue
            if not value.isdigit():
                raise Invalid(f"line {line}: {field} = {value!r}, expected a whole number")
        key = tuple(row[k] for k in schema["key"])
        if key in seen:
            raise Invalid(f"line {line}: duplicate {'/'.join(schema['key'])} {'/'.join(key)}")
        seen.add(key)
        extra_rules(name, line, row)


def extra_rules(name, line, row):
    if name == "claims.csv":
        try:
            date.fromisoformat(row["date_captured"])
        except ValueError:
            raise Invalid(f"line {line}: date_captured {row['date_captured']!r} is not YYYY-MM-DD")
        if row["legal_flag"] == "cap_3_7_unsubstantiated" and row["evidence_cited"] != "none":
            raise Invalid(f"line {line}: legal_flag set but evidence_cited is {row['evidence_cited']}")
        if row["claim_type"] == "no_public_documentation" and row["legal_flag"] != "none":
            raise Invalid(f"line {line}: no_public_documentation rows take legal_flag none")
    elif name == "crosswalk.csv":
        if (row["industry_authored"] == "yes") != (row["scheme"] == "FARM_v5"):
            raise Invalid(f"line {line}: industry_authored must be yes for FARM_v5 rows and no otherwise")
        if row["requirement_text"].strip() and not row["audit_method"]:
            raise Invalid(f"line {line}: audit_method is empty for a row with a requirement")
        if not row["requirement_text"].strip() and row["audit_method"]:
            raise Invalid(f"line {line}: audit_method set on a row with no requirement")
    elif name == "reliability.csv":
        if row["field"] not in SCHEMAS["claims.csv"]["header"]:
            raise Invalid(f"line {line}: field {row['field']!r} is not a claims.csv column")


# (file, field, target file, target key); empty values are not checked
REFERENCES = [
    ("claims.csv", "product_id", "products.csv", "product_id"),
    ("claims.csv", "mapped_indicator_id", "indicators.csv", "indicator_id"),
    ("scorecard.csv", "product_id", "products.csv", "product_id"),
    ("crosswalk.csv", "indicator_id", "indicators.csv", "indicator_id"),
    ("reliability.csv", "claim_id", "claims.csv", "claim_id"),
]


def main():
    loaded, errors = {}, {}
    for name, schema in SCHEMAS.items():
        try:
            records = load(name, schema)
            check_rows(name, schema, records)
            loaded[name] = records
        except Invalid as e:
            errors[name] = str(e)

    for name, field, target, key in REFERENCES:
        if name in errors or name not in loaded:
            continue
        if target not in loaded:
            errors[name] = f"cannot check {field}: {target} has errors"
            continue
        known = {row[key] for _, row in loaded[target]}
        for line, row in loaded[name]:
            if row[field] and row[field] not in known:
                errors[name] = f"line {line}: {field} {row[field]!r} not found in {target}"
                break

    for name in SCHEMAS:
        print(f"{name}: {errors.get(name, 'OK')}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
