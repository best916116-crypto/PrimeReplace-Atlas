# PrimeReplace Atlas

PrimeReplace Atlas is an all-mapped transcript-unit architecture database that reorganizes disease-associated ClinVar pathogenic/likely pathogenic records into large-fragment replacement hypotheses across human disease genes.

The resource maps ClinVar P/LP records onto MANE/GENCODE transcript structures and summarizes whether pathogenic-record burden forms local exon/block architecture, boundary-CDS payload architecture, donor-burden stress, low-record-burden interpretation-limited cases, tumor-predisposition control contexts, or mechanism-complex limitations.

**Browser:** https://best916116-crypto.github.io/PrimeReplace-Atlas/  
**Repository:** https://github.com/best916116-crypto/PrimeReplace-Atlas  
**Zenodo archive:** https://doi.org/10.5281/zenodo.20174922

---

## What this resource provides

PrimeReplace Atlas provides a precomputed transcript-unit architecture layer for disease-associated ClinVar P/LP records.

The current release includes:

| Layer | Count |
|---|---:|
| ClinVar VCF records scanned | 4,403,650 |
| Primary ClinVar P/LP VCF records | 337,682 |
| ClinVar P/LP gene-variant rows | 346,444 |
| Unique genomic coordinates | 336,901 |
| All-mapped genes | 5,738 |
| Transcript-unit opportunity rows | 437,301 |
| Low-record-burden interpretation-limited genes | 3,459 |
| Architecture-interpretable genes | 2,279 |
| High-support condition-associated record groups | 3,389 |
| High-support condition groups with recovered unit coverage | 1,278 |
| Condition-unit coverage rows in the recovered deep-enumerated condition subset | 160,125 |

---

## Browser quick start

Open the public browser:

https://best916116-crypto.github.io/PrimeReplace-Atlas/

Suggested first-use workflow:

1. Open **Gene search**.
2. Search a gene symbol, for example `DMD`, `F9`, `ABCA4`, `CFTR`, `LDLR`, or `BRCA1`.
3. Open the gene page.
4. Inspect the gene-level architecture class.
5. Review unit-level record coverage and payload/context caveats.
6. Open **Condition facets** to inspect condition-associated ClinVar P/LP record groups.
7. Download source tables from the **Downloads** page.

---

## Local browser

The browser is a static site and can also be opened locally.

```bash
git clone https://github.com/best916116-crypto/PrimeReplace-Atlas.git
cd PrimeReplace-Atlas
python -m http.server 8000 --directory docs
```

Then open:

```text
http://localhost:8000/
```

---

## Conceptual overview

Disease-associated pathogenic variants are catalogued as individual records, whereas large-fragment replacement hypotheses are interpreted at transcript-unit, exon-block, and coding-payload scale.

PrimeReplace Atlas bridges this gap by converting:

```text
ClinVar P/LP record
→ MANE/GENCODE transcript coordinate
→ transcript-unit grouping
→ record-level coverage
→ payload/context burden
→ architecture class
```

The core output is not a single score. PrimeReplace Atlas reports independent interpretation axes:

- record support
- transcript-unit type
- record-level coverage
- donor payload burden
- boundary/context caveat
- mechanism or control class
- condition-associated record facet, where source-locked

---

## Transcript-unit definitions

PrimeReplace Atlas defines three primary transcript-unit families.

### Single-exon unit

A single-exon unit asks whether ClinVar P/LP records concentrate within one exon.

### Adjacent exon-block unit

An adjacent exon-block unit asks whether neighboring exons form a local compact replacement architecture.

### Boundary-CDS payload unit

A boundary-CDS payload unit, formally a transcript-boundary CDS payload hypothesis, asks whether an upstream endogenous transcript segment could in principle connect to a donor CDS payload that groups downstream pathogenic records.

This is a boundary-dependent transcript-bypass hypothesis. It is not equivalent to local exon/block replacement and does not imply functional rescue without RNA, junction, reading-frame, isoform, expression, dosage, NMD, and protein-function validation.

---

## Architecture classes

PrimeReplace Atlas uses architecture labels to describe how pathogenic records are organized relative to transcript-unit replacement hypotheses.

Primary public-facing groups include:

- **Low-record-burden interpretation-limited**: genes retained in the atlas but not overinterpreted because record support is sparse.
- **Local compact architecture**: pathogenic records concentrate in a single exon or adjacent exon block.
- **Boundary-CDS payload architecture**: records are grouped downstream of a transcript boundary by a coding-payload hypothesis.
- **Donor-burden stress**: high theoretical record coverage may require large or context-burdened payloads.
- **Tumor-predisposition control context**: high-burden tumor-predisposition genes retained as control/caution contexts.
- **Mechanism-complex limitation**: repeat, noncoding, splice, isoform, or mechanism-specific biology limits transcript-unit interpretation.

---

## Condition-associated pathogenic-record facets

PrimeReplace Atlas includes condition-associated ClinVar P/LP record facets.

These facets group public ClinVar records by ClinVar condition annotation where available and connect source-locked groups to transcript-unit architecture in the recovered deep-enumerated subset.

Condition facets are record-level ClinVar annotation groups. They are not patient cohorts, disease prevalence estimates, patient-coverage estimates, therapeutic-coverage estimates, safety predictions, editing-efficiency predictions, or final implementation-mode recommendations.

---

## What this resource is not

PrimeReplace Atlas is not:

- an editing-efficiency predictor
- a therapeutic-efficacy predictor
- a safety predictor
- a patient-coverage or prevalence estimator
- a final PA-family implementation-mode recommender
- a global ranking score
- a clinical decision engine

PrimeReplace Atlas is a pre-implementation architecture resource for organizing public disease-associated pathogenic records relative to transcript-unit replacement hypotheses.

---

## Main browser pages

- **Overview:** `index.html`
- **Start here:** `start_here.html`
- **Gene search:** `gene_search.html`
- **All-gene index:** `all_gene_index.html`
- **Opportunity units:** `opportunity_units.html`
- **Architecture classes:** `architecture_classes.html`
- **Condition facets:** `condition_facets.html`
- **Glossary:** `glossary.html`
- **Downloads:** `downloads.html`

---

## Main downloadable tables

The browser provides source tables and validation-linked summaries, including:

- `all_mapped_gene_semantic_summary.tsv`
- `all_mapped_low_burden_interpretation_flags.tsv`
- `all_mapped_semantic_class_summary.tsv`
- `all_mapped_unit_type_summary.tsv`
- `allmapped_unique_variant_coordinate_sensitivity.tsv`
- `gene_condition_record_groups_v1.tsv`
- `gene_condition_record_architecture_recovered_v1.tsv`
- `gene_condition_unit_coverage_recovered_v1.tsv`
- `condition_architecture_class_summary_recovered_v1.tsv`
- `condition_layer_recovered_readiness_v1.tsv`
- `figure4_condition_example_candidates_source_locked_v1.tsv`

Large archival payloads, validation manifests, checksums, and release bundles are available through the Zenodo archive.

---

## Data sources

PrimeReplace Atlas uses a frozen public resource stack:

| Layer | Resource |
|---|---|
| Genome build | GRCh38 / GRCh38.p14 |
| Transcript anchor | MANE Select |
| Transcript structure | GENCODE v49 |
| Variant records | ClinVar GRCh38 pathogenic/likely pathogenic VCF |

---

## Repository structure

```text
docs/
  Static browser pages and browser-downloadable source tables

data/
  Compact source tables and small release tables

reports/
  Resource summaries and validation-linked documentation

validation/
  Validation summaries and release checks

scripts/
  Source scripts used to generate and validate the release
```

---

## Citation

Please cite the Zenodo archived release:

https://doi.org/10.5281/zenodo.20174922

A manuscript citation will be added after publication.

---

## License

See the repository license file for reuse terms.

---

## Contact

For questions about the PrimeReplace Atlas release, please contact the corresponding maintainer listed in the manuscript or repository metadata.
