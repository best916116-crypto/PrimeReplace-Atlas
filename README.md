# PrimeReplace Atlas

PrimeReplace Atlas maps ClinVar pathogenic/likely pathogenic variants onto MANE/GENCODE transcript structures to show how disease-associated variant burden is distributed across exons, exon blocks, and coding-payload units.

It is designed to help researchers triage human disease genes for large-fragment genome-writing hypotheses, including local exon/block replacement and coding-payload replacement architectures.

The atlas does not predict editing efficiency, safety, clinical efficacy, or patient coverage; it provides a pre-implementation target-architecture map.

**Browser:** https://best916116-crypto.github.io/PrimeReplace-Atlas/  
**Repository:** https://github.com/best916116-crypto/PrimeReplace-Atlas  
**Zenodo archive:** https://doi.org/10.5281/zenodo.20174922

---

## What it does

PrimeReplace Atlas converts public disease-associated variant records into transcript-level architecture summaries.

In practical terms, the atlas helps answer whether ClinVar P/LP records for a gene are:

- concentrated in one exon,
- distributed across an adjacent exon block,
- grouped by a downstream coding-payload unit,
- spread across a large or payload-burdened gene,
- limited by sparse ClinVar record support,
- affected by tumor-predisposition, repeat, noncoding, splice, isoform, or other mechanism-complex contexts.

The core output is an architecture map, not a yes/no feasibility call.

---

## Use it to ask

Use PrimeReplace Atlas to ask questions such as:

- For a disease gene, where do ClinVar P/LP records fall across the MANE/GENCODE transcript?
- Do records cluster in a local exon or adjacent exon block?
- Does apparent high coverage depend on a large coding payload or boundary-driven CDS coverage?
- Is the gene record-supported enough for architecture interpretation, or is it low-record-burden?
- Are condition-associated ClinVar record groups available for disease-facing interpretation?
- Which downloadable source tables support the gene or condition summary?

---

## Open the browser

Start here:

https://best916116-crypto.github.io/PrimeReplace-Atlas/

Suggested first-use workflow:

1. Open **Gene search**.
2. Search a gene symbol, for example `DMD`, `F9`, `ABCA4`, `CFTR`, `LDLR`, or `BRCA1`.
3. Open the gene page.
4. Inspect the gene-level architecture label.
5. Review unit-level record coverage and payload/context caveats.
6. Open **Condition facets** to inspect condition-associated ClinVar P/LP record groups.
7. Download source tables from the **Downloads** page.

---

## What the atlas reports

PrimeReplace Atlas reports several independent interpretation axes.

| Axis | Meaning |
|---|---|
| Record support | Number of ClinVar P/LP records available for a gene or condition-associated record group |
| Transcript-unit type | Single exon, adjacent exon block, or coding-payload / boundary-driven CDS unit |
| Record-level coverage | Fraction of ClinVar records covered by a transcript unit |
| Payload/context burden | Donor span, coding-payload burden, boundary context, or related caveat |
| Architecture label | Public-facing summary of how the pathogenic-record burden is organized |
| Condition facet | ClinVar condition-associated record group, where source-locked |

The atlas deliberately keeps these axes separate. It does not reduce them to a single suitability score.

---

## Architecture labels

PrimeReplace Atlas uses architecture labels to describe how pathogenic records are organized relative to transcript-unit replacement hypotheses.

Primary public-facing groups include:

- **Low-record-burden interpretation-limited**: genes retained in the atlas but not overinterpreted because record support is sparse.
- **Local compact architecture**: pathogenic records concentrate in a single exon or adjacent exon block.
- **Boundary-driven CDS coverage architecture**: records downstream of a transcript boundary can be grouped by a coding-payload hypothesis; this is a burden-aware architecture descriptor, not a functional-rescue claim.
- **Donor-burden stress**: high theoretical record coverage may require large or context-burdened payloads.
- **Tumor-predisposition control context**: high-burden tumor-predisposition genes retained as control/caution contexts.
- **Mechanism-complex limitation**: repeat, noncoding, splice, isoform, or mechanism-specific biology limits transcript-unit interpretation.

---

## What this resource is not

PrimeReplace Atlas is not:

- an editing-efficiency predictor,
- a therapeutic-efficacy predictor,
- a safety predictor,
- a patient-coverage or prevalence estimator,
- a final PA-family or genome-writing modality recommender,
- a global ranking score,
- a clinical decision engine.

PrimeReplace Atlas is a pre-implementation architecture resource for organizing public disease-associated ClinVar records relative to transcript-unit replacement hypotheses.

---

## Data release

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

## Downloads

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

ClinVar, MANE, GENCODE, and other third-party public resources remain subject to their original provider terms.

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

## Repository structure

```text
data/small_tables/
  Compact release tables

docs/
  Static browser pages and browser-downloadable source tables

figures/
  Public figure mockups or release figures

scripts/
  Source scripts used to generate and validate the release

validation/
  Validation summaries and release checks
```

---

## Citation

If you use PrimeReplace Atlas in your work, please cite the archived release:

> Park J, Cho SI. PrimeReplace Atlas: a transcript-unit architecture database for disease-associated large-fragment genome writing. Zenodo. https://doi.org/10.5281/zenodo.20174922

A manuscript describing the atlas is in preparation. Until the manuscript is available, please cite the Zenodo DOI for the release used in your analysis.

---

## License

This repository uses separate licenses for software and generated data:

- **Code and static browser source:** MIT License. See `LICENSE`.
- **Generated atlas tables, figures, and archived release materials:** Creative Commons Attribution 4.0 International (CC BY 4.0). See `LICENSE-DATA.md`.

ClinVar, MANE, GENCODE, and other third-party public resources are not relicensed by this repository and remain subject to their original provider terms.

---

## Contact

For public questions, bug reports, or feature requests, please use GitHub Issues.

For release correspondence, contact the project maintainer through the contact information listed in the Zenodo record.
