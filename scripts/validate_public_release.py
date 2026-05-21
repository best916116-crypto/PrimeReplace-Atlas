#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "LICENSE-DATA.md",
    "CITATION.cff",
    ".zenodo.json",
    "docs/index.html",
    "docs/gene_search.html",
    "docs/condition_facets.html",
    "docs/methods.html",
    "docs/downloads.html",
    "docs/citations.html",
    "docs/VERSION.txt",
]

FORBIDDEN = [
    r"/home/",
    r"paper2_prime_replace_hardened",
    r"cell_genomics_presubmission",
    r"genome_biology_presubmission",
    r"nar_fallback",
    r"presubmission_package",
    r"source_locked",
    r"source-locked",
    r"deep-enumerated",
    r"deep_enumerated",
    r"mockup",
    r"v4_allmapped",
    r"v5_clean",
    r"v5\.1_clean_link_fixed",
    r"v6_condition_facet",
    r"condition-facet patch",
    r"therapeutic candidate",
    r"wet shortlist",
    r"no-go",
    r"PA possible",
    r"PA impossible",
]

SCAN = [
    "README.md",
    "CITATION.cff",
    ".zenodo.json",
    "LICENSE",
    "LICENSE-DATA.md",
    "docs/*.html",
    "docs/VERSION.txt",
    "docs/downloads/*.tsv",
    "reports/*.md",
    "reports/*.tsv",
    "validation/*.json",
    "validation/*.tsv",
    "figures/*.svg",
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def collect_scan_files() -> list[Path]:
    files = []
    for pat in SCAN:
        files.extend(ROOT.glob(pat))
    return sorted(set([p for p in files if p.is_file()]))

def main() -> int:
    validation = ROOT / "validation"
    validation.mkdir(exist_ok=True)

    checks = []
    for rel in REQUIRED:
        p = ROOT / rel
        checks.append({
            "check": "required_file",
            "item": rel,
            "status": "PASS" if p.exists() else "FAIL",
            "detail": rel,
        })

    audit_rows = []
    generated_validation_files = {
        "public_language_audit_v1.0.0.tsv",
        "public_release_checks_v1.0.0.tsv",
        "public_release_checks_v1.0.0.json",
        "checksum_manifest_v1.0.0.tsv",
    }

    for p in collect_scan_files():
        if p.name in generated_validation_files:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for pat in FORBIDDEN:
            m = re.search(pat, text, flags=re.I)
            if m:
                audit_rows.append({
                    "file": str(p.relative_to(ROOT)),
                    "pattern": pat,
                    "status": "REVIEW",
                    "context": text[max(0, m.start()-80):m.end()+160].replace("\n", " "),
                })

    with (validation / "public_language_audit_v1.0.0.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "pattern", "status", "context"], delimiter="\t")
        w.writeheader()
        for r in audit_rows:
            w.writerow(r)

    checksum_rows = []
    for p in collect_scan_files():
        checksum_rows.append({
            "path": str(p.relative_to(ROOT)),
            "bytes": p.stat().st_size,
            "sha256": sha256(p),
        })

    with (validation / "checksum_manifest_v1.0.0.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["path", "bytes", "sha256"], delimiter="\t")
        w.writeheader()
        for r in checksum_rows:
            w.writerow(r)

    checks.append({
        "check": "public_language_audit",
        "item": "forbidden_terms",
        "status": "PASS" if not audit_rows else "FAIL",
        "detail": f"review_hits={len(audit_rows)}",
    })

    summary = {
        "release": "1.0.0",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "passed": all(c["status"] == "PASS" for c in checks),
        "counts": {
            "PASS": sum(c["status"] == "PASS" for c in checks),
            "FAIL": sum(c["status"] == "FAIL" for c in checks),
        },
        "browser_url": "https://best916116-crypto.github.io/PrimeReplace-Atlas/",
        "repository_url": "https://github.com/best916116-crypto/PrimeReplace-Atlas",
        "zenodo_doi": "10.5281/zenodo.20174922",
        "public_language_review_hits": len(audit_rows),
    }

    (validation / "public_release_checks_v1.0.0.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    with (validation / "public_release_checks_v1.0.0.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["check", "item", "status", "detail"], delimiter="\t")
        w.writeheader()
        for c in checks:
            w.writerow(c)

    print(json.dumps(summary, indent=2))
    return 0 if summary["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
