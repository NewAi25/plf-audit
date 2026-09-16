# Data dictionary

Six CSV files, each with a fixed header and column order. `python scripts/validate_csv.py` checks every file against these definitions and fails on any value outside the allowed set. `python scripts/stats.py` fills the computed columns and prints the summary numbers. Column names and order never change without an entry in `notes/decisions.md`.

An empty cell means something specific in each file, and the meaning is given at the end of each section. An empty cell never means "probably none"; where a source was checked and nothing was found, the row says so in `notes`.

## products.csv

One row per product in the register. Twenty products plus one comparator as of 16 September 2026.

| Column | Values | Meaning |
|---|---|---|
| product_id | P001 onwards | Identifier used by claims.csv and scorecard.csv |
| vendor | text | Company name as it trades today, with the earlier name in brackets where it changed |
| product | text | Product name as the vendor uses it |
| sensor_type | collar_accelerometer, ear_tag, bolus, camera, milking_system, other | The main sensing hardware. Leg mounted accelerometers and load cell plates are coded other, with the mounting named in notes |
| measures_claimed | text | What the product says it measures, copied from the Stygar appendix for Stygar sourced rows |
| species | text | dairy cattle for every row except the comparator |
| country | text | Vendor country, from the Stygar appendix or the ICAR report |
| stygar_listed | yes, no | Whether the product appears in the Stygar et al. 2021 appendix of 129 technologies |
| stygar_validation | none, external_self, external_independent, not_listed | Stygar's validation finding. none means listed with no external validation study found. external_self means every cited study had a developer or company author. external_independent means at least one cited study had none. not_listed means the product is not in the appendix |
| icar_validated | yes, no | Whether the product is on the ICAR validated sensor systems list |
| source | stygar, icar, market_scan, course | Where the product entered the list |
| marketing_url | URL | The public product page |
| manual_url | URL | Public product manual, if any |
| devdocs_url | URL | Public API or developer documentation, if any |
| patent_urls | URLs separated by spaces | Patents, only for the five best documented vendors |
| comparator | yes, no | yes only for AI4Animals, which is scored but reported outside the dairy count |
| notes | text | Provenance of the row, reference numbers behind the validation value, naming discrepancies, and anything not yet verified |

Empty means: for marketing_url, the URL has not been captured yet; for manual_url, devdocs_url and patent_urls, the market scan has not yet searched for it. After the market scan, a search that found nothing is recorded in notes, not as an empty cell.

## claims.csv

One row per welfare claim per product. Empty until the register is coded in week 2. The coding rules are in `standard/coding_frame.md`.

| Column | Values | Meaning |
|---|---|---|
| claim_id | C0001 onwards | Sequential in coding order, never reused |
| product_id | an id in products.csv | The product the claim is about |
| claim_text | verbatim | The exact words from the source |
| source_url | URL | The public page or document where the claim was found |
| source_type | marketing_page, product_manual, developer_doc, patent, peer_reviewed, press_release, recorded_talk | The kind of document |
| date_captured | YYYY-MM-DD | The day the source was read and saved to corpus/vendors |
| claim_type | indicator_claim, outcome_claim, accuracy_claim, compliance_claim, no_public_documentation | What kind of assertion it is. no_public_documentation records that a product publishes nothing or gates it behind a login |
| mapped_indicator_id | an id in indicators.csv | The indicator the claim maps to |
| mapping_confidence | direct, proxy, none, unsure | How the claim relates to that indicator. unsure always goes to notes/kevin_questions.md |
| evidence_cited | none, vendor_internal, independent_external, peer_reviewed | What the source cites in support of the claim |
| evidence_ref | citation or URL | The reference as given |
| legal_flag | none, cap_3_7_unsubstantiated | Set when a welfare claim cites no evidence at all |
| notes | text | Other pages where the claim repeats, page numbers, sibling claims, candidate indicators for unsure rows |

Empty means: mapped_indicator_id is empty when mapping_confidence is none or unsure; evidence_ref is empty when evidence_cited is none. No other column may be empty.

## indicators.csv

Column 1. One row per indicator, 57 rows as of 16 September 2026: the 30 animal based measures in the EFSA 2023 ABM tables and the 31 Welfare Quality dairy measures, joined into one row only where EFSA cites Welfare Quality for the definition or the names are identical. Six rows are joined.

| Column | Values | Meaning |
|---|---|---|
| indicator_id | I001 onwards | Identifier used by claims.csv and crosswalk.csv |
| efsa_consequence | one of the five EFSA welfare consequences | Locomotory disorders, Mastitis, Restriction of movement and resting problems, Inability to perform comfort behaviour, Metabolic disorders |
| efsa_abm | text | The ABM name as EFSA's table gives it |
| wq_principle | Good feeding, Good housing, Good health, Good behaviour | Welfare Quality principle |
| wq_criterion | text | Welfare Quality criterion, one of twelve |
| wq_measure | text | Welfare Quality measure, one of thirty one |
| maroto_molina_technology | text | The technology Maroto Molina et al. 2020 identify for the measure, or "Not discussed by Maroto Molina" |
| maroto_molina_feasible | yes, partial, no, not_covered | yes: they identify commercially available technology. partial: research level, needs adaptation, or a substitute measure. no: they say sensors cannot provide it. not_covered: the paper does not discuss it |
| notes | text | The EFSA table the ABM came from, whether EFSA cites Welfare Quality, scale differences, and any open question |

Empty means: efsa_consequence and efsa_abm are empty for a Welfare Quality only row; wq_principle, wq_criterion and wq_measure are empty for an EFSA only row; wq_measure alone is empty for the thermal comfort criterion, where Welfare Quality defines no measure.

## crosswalk.csv

Column 3 joined to columns 1 and 2. One row per indicator per scheme, so an indicator no scheme requires still has four rows. Empty until week 3.

| Column | Values | Meaning |
|---|---|---|
| indicator_id | an id in indicators.csv | |
| scheme | RSPCA_Assured, FARM_v5, GAP_dairy, Certified_Humane | The certification scheme |
| requirement_text | text | The scheme's requirement naming this indicator, quoted |
| numeric_threshold | text | Any number the scheme sets, exactly as written |
| audit_method | visual_inspection, records_review, sensor_accepted, unspecified | How the scheme checks it |
| industry_authored | yes, no | yes for FARM_v5 rows only, the industry acceptability proxy |
| products_measuring_direct | whole number | Products in the register mapping to this indicator with mapping_confidence direct |
| products_measuring_proxy | whole number | Same with proxy |
| any_external_validation | yes, no | Whether any of those products has external validation |
| icar_validated_any | yes, no | Whether any of those products is ICAR validated |
| query_shortlist | yes, no | Computed: measured directly by at least one product and required by FARM v5 |
| query_instrumented_not_required | yes, no | Computed: measured by at least one product and required by no scheme |
| query_required_manual_only | yes, no | Computed per row: this scheme requires it, audits it by visual inspection, and an externally validated product measures it |
| notes | text | Why the scheme has the requirement, from the RSPCA justification document where available |

Empty means: requirement_text empty means this scheme does not require the indicator, and audit_method is then empty too; the three query columns are empty until scripts/stats.py has run.

## scorecard.csv

One row per product, scored on the seven column 4 dimensions against `standard/rubric.md`. Empty until week 4.

| Column | Values | Meaning |
|---|---|---|
| product_id | an id in products.csv | |
| indicator_validity, validation_evidence, logging, data_lineage, access_ownership, tamper_evidence, disclosure | 0, 1, 2, NA | The score per dimension. NA is not assessable from public documentation and is never treated as 0 |
| assessable_dimensions | whole number | Computed: dimensions not NA |
| total | whole number | Computed: sum of the non NA scores |
| meets_threshold | yes, no, not_assessable | Computed from the threshold in rubric.md |
| legal_required_somewhere | yes, no | Whether a dimension scored below 2 is a legal requirement where the product is sold, for example access under the EU Data Act |
| evidence_urls | URLs separated by spaces | One public source per scored dimension |
| notes | text | Reasoning for any score a second person might set differently |

Empty means: assessable_dimensions, total and meets_threshold are empty until scripts/stats.py has run. A dimension cell is never empty; it is 0, 1, 2 or NA.

## reliability.csv

The 10% blind re code. One row per claim per re coded field. Empty until week 3.

| Column | Values | Meaning |
|---|---|---|
| claim_id | an id in claims.csv | |
| field | a claims.csv column name | The field re coded |
| coder_a_original | value | The original code |
| coder_a_recode | value | The same coder, blind, at least seven days later |
| coder_b | value | The second coder, Kevin or someone he names |
| agree_a_a | yes, no | Computed: original equals re code |
| agree_a_b | yes, no | Computed: original equals second coder |

Empty means: coder_b is empty until the second coder has coded the row; the agree columns are computed by scripts/stats.py.
