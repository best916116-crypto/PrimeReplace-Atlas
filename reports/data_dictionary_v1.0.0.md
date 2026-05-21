# PrimeReplace Atlas data dictionary v1.0.0

## Core definitions

- `record-level coverage`: fraction of ClinVar P/LP records covered by a transcript unit. This is not patient prevalence.
- `single-exon unit`: one exon used as a transcript-unit grouping.
- `adjacent exon-block unit`: contiguous exon block used as a transcript-unit grouping.
- `boundary-driven CDS coverage`: grouping of records downstream of a transcript boundary by a coding-payload hypothesis.
- `donor/payload burden`: estimated donor or coding-payload span associated with a transcript unit.
- `architecture label`: public-facing summary of how record burden is organized relative to transcript units.

## Main public tables

### all_mapped_gene_semantic_summary.tsv
Gene-level architecture summary.

### all_mapped_low_burden_interpretation_flags.tsv
Low-record-burden interpretation flags.

### all_mapped_semantic_class_summary.tsv
Architecture class counts.

### all_mapped_unit_type_summary.tsv
Transcript-unit type counts.

### allmapped_unique_variant_coordinate_sensitivity.tsv
ClinVar record-level versus coordinate-level sensitivity.

### gene_condition_record_groups_v1.tsv
ClinVar condition-associated record groups.

### gene_condition_record_architecture_recovered_v1.tsv
Condition-associated architecture summaries.

### gene_condition_unit_coverage_recovered_v1.tsv
Condition-unit record-level coverage.

### condition_architecture_class_summary_recovered_v1.tsv
Condition architecture class counts.

### condition_facet_representative_examples_v1.tsv
Representative condition-facet examples.
