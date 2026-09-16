"""Verify that every corpus file is the document its manifest says it is.

corpus/manifest.csv records, for each file, the exact URL its bytes came from
and the SHA256 of those bytes. This script checks three things:

  1. the local file exists and its SHA256 matches the manifest;
  2. the URL is live, and for binary files the bytes it serves today hash to
     the same value, so the link points at exactly the document in the corpus;
  3. for pasted text files, the URL is live and the recorded check phrase
     appears in the local file.

    python scripts/check_corpus.py            verify everything, exit 1 on any failure
    python scripts/check_corpus.py --local    hash check only, no network
    python scripts/check_corpus.py --record   write current local hashes into the manifest

Standard library only. A file listed with status "missing" in the manifest is
reported but does not fail the check.
"""
import csv
import hashlib
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
MANIFEST = CORPUS / "manifest.csv"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
FIELDS = ["filename", "kind", "url", "zip_member", "check_phrase", "sha256", "retrieved", "status", "doi_or_landing"]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://www.google.com/"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status, resp.read()


def load_manifest():
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        missing = [k for k in FIELDS if k not in r]
        if missing:
            sys.exit(f"manifest.csv is missing columns: {missing}")
    return rows


def save_manifest(rows):
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def check_row(r, network):
    path = CORPUS / r["filename"]
    if r["status"] == "missing":
        return "missing", "not downloaded, needs a browser (see corpus/README.md)"
    if not path.exists():
        return "FAIL", "file not in corpus/"
    local = path.read_bytes()
    if r["sha256"] and sha256(local) != r["sha256"]:
        return "FAIL", "local file has changed since the manifest was recorded"
    if not r["sha256"]:
        return "FAIL", "no sha256 recorded; run --record"
    if not network:
        return "ok", "local hash matches"
    try:
        status, remote = fetch(r["url"])
    except Exception as e:
        return "FAIL", f"url not reachable: {e}"
    if r["kind"] == "binary":
        if r["zip_member"]:
            try:
                remote = zipfile.ZipFile(io.BytesIO(remote)).read(r["zip_member"])
            except Exception as e:
                return "FAIL", f"zip member {r['zip_member']} not found: {e}"
        if sha256(remote) != r["sha256"]:
            return "FAIL", f"url serves different bytes now ({len(remote)} bytes); check whether the document was revised"
        return "ok", "url live and serves the exact same bytes"
    text = local.decode("utf-8", "replace")
    if r["check_phrase"] and r["check_phrase"] not in text:
        return "FAIL", "check phrase not found in the local text"
    if r["check_phrase"] and r["check_phrase"].encode("utf-8") not in remote:
        return "WARN", "url live but the check phrase no longer appears on the page"
    return "ok", "url live and check phrase present"


def main(argv):
    rows = load_manifest()
    if "--record" in argv:
        for r in rows:
            path = CORPUS / r["filename"]
            if path.exists():
                r["sha256"] = sha256(path.read_bytes())
                if r["status"] != "ok":
                    r["status"] = "ok"
        save_manifest(rows)
        print(f"recorded hashes for {sum(1 for r in rows if r['sha256'])} files")
        return 0
    network = "--local" not in argv
    failures = 0
    for r in rows:
        verdict, why = check_row(r, network)
        failures += verdict == "FAIL"
        print(f"{verdict:8} {r['filename']:40} {why}")
    print(f"\n{len(rows)} entries, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
