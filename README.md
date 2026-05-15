# PrimeReplace Atlas

PrimeReplace Atlas is an all-mapped transcript-unit architecture resource for mutation-agnostic large-fragment replacement hypotheses across human disease genes.

**Browser:** follow Quick start  
**Repository:** https://github.com/best916116-crypto/PrimeReplace-Atlas.git  
**Zenodo archive:** https://doi.org/10.5281/zenodo.20174922

## What this resource is

PrimeReplace Atlas maps ClinVar pathogenic/likely pathogenic (P/LP) record burden onto MANE/GENCODE transcript structures and reports gene-level and transcript-unit descriptors:

- ClinVar record coverage,
- donor payload bins,
- transcript-unit type,
- low-record-burden flags,
- architecture labels.

## What this resource is not

PrimeReplace Atlas does **not** predict editing efficiency, therapeutic efficacy, safety, patient coverage, final PA-family implementation mode, population/pangenome robustness, boundary/scar risk, or a global score.

ClinVar record coverage is a **record-level descriptor**, not patient coverage.

## Release backbone

| Item | Count |
|---|---:|
| All-mapped genes | 5,738 |
| ClinVar P/LP gene-variant rows | 346,444 |
| Unique genomic coordinates | 336,901 |
| Transcript-unit opportunity rows | 437,301 |
| Low-record-burden interpretation-limited genes | 3,459 |
| Architecture-interpretable genes | 2,279 |

Low-record-burden is currently defined as fewer than 20 ClinVar P/LP records.

## Quick start

```bash
git clone https://github.com/best916116-crypto/PrimeReplace-Atlas.git
cd PrimeReplace
python -m http.server 8000 --directory docs
```

Then open:

```text
http://localhost:8000/
```

## How to use the browser

1. Open **Gene search**.
2. Search a gene symbol.
3. Read the architecture label, low-record-burden flag, unit-level record coverage, and payload summary.
4. Carry the result forward only as a pre-implementation architecture hypothesis.

## Core terms

### ClinVar P/LP record

A ClinVar record annotated as pathogenic or likely pathogenic. It is not a patient and not an allele-frequency denominator.

### ClinVar record coverage

For a transcript unit:

```text
ClinVar record coverage = records addressed by the unit / gene-level ClinVar P/LP records
```

### Transcript units

| Unit type | Meaning |
|---|---|
| Single exon | One local exon interval |
| Adjacent exon block | Neighboring exon interval |
| Downstream-CDS boundary hypothesis | Downstream coding payload after a transcript boundary |

High downstream-CDS coverage can be boundary-driven and must be read with payload and context caveats.

## Repository layout

```text
docs/                 Static browser for GitHub Pages
docs/genes/           All-mapped gene pages
docs/data/            Browser gene index and browser-facing compact data
docs/downloads/       Downloadable compact tables
data/small_tables/    Compact source tables
figures/              Source-locked SVG figure mockups
validation/           Validation summaries
scripts/              Minimal helper scripts only
```

Large all-mapped source tables and archived release packages should be deposited on Zenodo rather than committed to GitHub.

## Validation

```bash
python scripts/validate_public_release.py
```

## Citation

Use the Zenodo DOI after release:

```text
10.5281/zenodo.20174921.
```

Suggested citation before DOI assignment:

> PrimeReplace Atlas, version 1.0.0. Transcript-unit architecture resource for mutation-agnostic large-fragment replacement hypotheses.

## License

Recommended split:

- data, browser content, documentation, and figures: CC BY 4.0,
- minimal helper scripts: MIT.

See `LICENSE.md`.
