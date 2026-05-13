#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

FORBIDDEN = [
    "Why 306", "selected 306", "306 selected", "candidate", "shortlist", "no-go",
    "report-card", "proxy", "pending Paper 1", "PA possible", "PA impossible",
    "therapeutic candidate", "final mode recommendation", "patient coverage estimate",
    "global score",
]

REQUIRED = [
    "README.md",
    "CITATION.cff",
    ".zenodo.json",
    "LICENSE.md",
    "docs/index.html",
    "docs/gene_search.html",
    "docs/all_gene_index.html",
    "docs/opportunity_units.html",
    "docs/glossary.html",
    "docs/downloads.html",
    "docs/assets/style.css",
    "docs/assets/browser.js",
    "docs/data/gene_index_v5_clean.tsv",
]

SKIP = {
    "scripts/validate_public_release.py",
    "validation/public_language_audit.tsv",
    "validation/public_language_hits.json",
    "validation/public_release_validation.summary.json",
}

def allowed_context(ctx: str) -> bool:
    low = ctx.lower()
    return any(x in low for x in [
        "not ", "no ", "does not", "do not", "forbidden", "excluded", "removed", "legacy",
        "not patient coverage", "not a patient", "not an estimate"
    ])

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = []
    for rel in REQUIRED:
        if not (root / rel).exists():
            failures.append(f"missing required file: {rel}")

    hits = []
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        rel = str(p.relative_to(root))
        if rel in SKIP:
            continue
        if p.suffix.lower() not in {".md", ".html", ".txt", ".json", ".tsv", ".py", ".sh", ".cff"}:
            continue
        text = p.read_text(errors="replace")
        low = text.lower()
        for term in FORBIDDEN:
            idx = low.find(term.lower())
            if idx >= 0:
                ctx = text[max(0, idx-100):idx+220].replace("\n", " ")
                if not allowed_context(ctx):
                    hits.append({"file": rel, "term": term, "context": ctx})

    if hits:
        failures.append(f"public-language hits: {len(hits)}")

    (root / "validation").mkdir(exist_ok=True)
    (root / "validation" / "public_language_hits.json").write_text(json.dumps(hits, indent=2), encoding="utf-8")
    result = {"passed": not failures, "failures": failures, "public_language_hits": len(hits)}
    (root / "validation" / "public_release_validation.summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
