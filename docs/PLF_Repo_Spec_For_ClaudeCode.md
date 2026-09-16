# Repository specification: plf-audit
Give this file to Claude Code as the first message, together with the resource files listed in `PLF_Resources_To_Share_With_ClaudeCode.md`. It creates the repository, every scaffold file, the data schemas, and the helper scripts, then stops. No research and no coding of claims happens in this session.

---

## Instructions to Claude Code

You are setting up a research repository. Build exactly what is specified below, show me the tree and the contents of `CLAUDE.md`, `standard/coding_frame.md` and `standard/rubric.md`, run the two scripts against the empty CSVs to prove they work, make the initial commit, and stop. Do not read the corpus, do not search the web, do not fill in any data rows.

Write all prose files in plain English with no dashes (no hyphens used as punctuation, no em dashes). Sentences of varied length. No bullet lists inside `standard/` or `writeup/` files; use paragraphs and tables.

### 1. Directory tree

```
plf-audit/
  CLAUDE.md
  README.md
  .gitignore
  docs/                    (copied in by me before this session; leave as is)
  corpus/                  (copied in by me; leave as is)
  data/
    products.csv
    claims.csv
    indicators.csv
    crosswalk.csv
    scorecard.csv
    reliability.csv
  standard/
    coding_frame.md
    rubric.md
    standard_v0.1.md
    scope_note.md
  logger/
    README.md
  writeup/
    report.md
    certifier_annex.md
    icar_note.md
    onepager.md
  notes/
    decisions.md
    kevin_questions.md
    duplication_check.md
    weekly_status.md
  scripts/
    validate_csv.py
    stats.py
```

### 2. `CLAUDE.md`

```markdown
# PLF Welfare Audit Standard (dairy v0.1)

## The project in one sentence
Can a welfare claim made by a dairy sensor system be verified by someone outside the vendor, and what would the system have to log and expose to make that possible?

Built for the Sentient Futures incubator, mentored by Kevin Xia at Rethink Priorities. Five build weeks, 15 September to 19 October 2026. Plan: docs/PLF_5_Week_Plan.md. Critical review and sources: docs/PLF_Project_Resources.md. Read Part 1 of the resources doc before doing anything, it changes the scope.

## Deliverables
1. Claims register: every welfare claim from 15 to 20 dairy PLF products plus AI4Animals as a comparator, coded against a fixed frame, with a reliability figure from a 10% blind re code. data/claims.csv, standard/coding_frame.md, data/reliability.csv.
2. Crosswalk: column 3 (what certification schemes require and how they audit it) joined to the existing column 1 to 2 mapping from Maroto Molina 2020 and Stygar 2021, plus an industry acceptability flag. data/indicators.csv, data/crosswalk.csv. The novelty is column 3 and the join, not columns 1 and 2.
3. Standard v0.1: seven requirement groups for what a system must log and prove, each tied to an existing legal or standards source, with a scope note taking no position on PLF itself. standard/standard_v0.1.md, standard/rubric.md, standard/scope_note.md.
4. Scorecard: every product scored 0/1/2 on seven dimensions from public documentation only, reporting two headline numbers: how many products are assessable at all, and how many of those meet the standard. Pass threshold written into rubric.md before any scoring. data/scorecard.csv.
5. Reference logger: hash chained append only log with verifier, standard library Python only, under 300 lines total. logger/.
6. Write up, two page certifier annex, one page note to ICAR, one pager. writeup/.

## Hard rules
- Public documentation, API references, patents, published papers and recorded talks only. Never contact a vendor, never suggest it, never fetch anything behind a login.
- Never make a welfare science judgement. Indicators come from the EFSA 2023 dairy cow opinion and the Welfare Quality dairy protocol, mapped to sensors by Maroto Molina 2020. If a claim does not map cleanly, set mapping_confidence to unsure and append it to notes/kevin_questions.md. Do not guess.
- Every coding or scoring decision not already covered by the coding frame or rubric gets a dated entry in notes/decisions.md before it is applied, and the frame or rubric is updated so the next case is covered.
- "Not assessable from public documentation" is a result with its own code (NA). It is never scored as 0.
- The pass threshold in rubric.md is fixed before scoring starts and never changed afterwards. If it needs changing, that is a decisions.md entry and the old threshold is reported alongside the new.
- CSV files keep their header row and column order. Run scripts/validate_csv.py after every edit to data/.
- Prose files use no dashes as punctuation, varied sentence length, first person where the author speaks. No bullet lists in standard/ or writeup/.
- Citations: Twelve Threats is Tuyttens, Molento and Benaissa 2022. The transparency framework is Elliott and Werkheiser 2023. The EU PLF blueprint is Berckmans 2017. Column 1 to 2 mapping is Maroto Molina et al. 2020. GLOBALG.A.P. discontinued its livestock scope and is not a source. ICAR has validated three sensor systems as of September 2026, none measuring a welfare indicator.
- Column 4 requirements cite their source: EU Data Act (applicable 12 September 2025) for access and ownership, EU AI Act Article 12 and 26(6) for logging and retention, Rutten 2013 four levels for lineage, ICAR's application checklist for disclosure, SOC 2 and certificate transparency practice for tamper evidence.
- The logger stays under 300 lines and uses only the standard library. It is a proof of cost, not a product.
- Vocabulary: welfare washing (claims without evidence), proxy drift (optimising a measure that stops tracking the animal's interests), precision welfare (PLF built around the animal). Use these terms as the course does.

## Theory of change
Primary user: a welfare certifier accepting sensor evidence in place of inspection (RSPCA Assured, Global Animal Partnership). Secondary: ICAR, for a welfare claim category in its validation scheme. By product: the claims register as an evidence base for claims substantiation under advertising rules (UK CAP Code 3.7). Confirm the primary with Kevin in week 1; until then, build for the certifier.

## Working style
- Start every session by reading notes/decisions.md, notes/weekly_status.md and the current week of the plan. State what done looks like for this session before doing anything.
- Work in small verified batches: ten claims, show them, continue. Three products scored, show them, continue.
- If a corpus file is missing, say so and stop. Never substitute recollection for a source.
- End every session by updating notes/weekly_status.md and committing with a message naming the week and the artifact.
```

### 3. `README.md`

Title, the one sentence question, the six deliverables in a table with their file paths, a paragraph on method (public documentation only, coding frame, rubric, pre registered threshold, reliability check), a "how to re run the scoring next year" section (update products.csv, re code claims, run scripts/stats.py, compare to the previous tag), and the licence line: data and text CC BY 4.0, code MIT. Author: Manisha Sarkar. Mentor: Kevin Xia, Rethink Priorities. Programme: Sentient Futures incubator, fall 2026.

### 4. `.gitignore`

```
corpus/*.pdf
corpus/*.html
__pycache__/
*.pyc
.DS_Store
```

Corpus files are large and some are copyrighted; they stay local. `corpus/README.md` (create it) lists every expected file with its source URL so anyone can rebuild the folder.

### 5. Data schemas

Create each CSV with the header row only. `scripts/validate_csv.py` enforces these exactly.

**`data/products.csv`**
```
product_id,vendor,product,sensor_type,measures_claimed,species,country,stygar_listed,stygar_validation,icar_validated,source,marketing_url,manual_url,devdocs_url,patent_urls,comparator,notes
```
`sensor_type` one of: collar_accelerometer, ear_tag, bolus, camera, milking_system, other. `stygar_validation` one of: none, internal, external, not_listed. `icar_validated` yes or no. `source` one of: stygar, icar, market_scan, course. `comparator` yes only for AI4Animals.

**`data/claims.csv`**
```
claim_id,product_id,claim_text,source_url,source_type,date_captured,claim_type,mapped_indicator_id,mapping_confidence,evidence_cited,evidence_ref,legal_flag,notes
```
`source_type` one of: marketing_page, product_manual, developer_doc, patent, peer_reviewed, press_release, recorded_talk. `claim_type` one of: indicator_claim, outcome_claim, accuracy_claim, compliance_claim, no_public_documentation. `mapping_confidence` one of: direct, proxy, none, unsure. `evidence_cited` one of: none, vendor_internal, independent_external, peer_reviewed. `legal_flag` one of: none, cap_3_7_unsubstantiated (a welfare claim with evidence_cited = none).

**`data/indicators.csv`**
```
indicator_id,efsa_consequence,efsa_abm,wq_principle,wq_criterion,wq_measure,maroto_molina_technology,maroto_molina_feasible,notes
```
`maroto_molina_feasible` one of: yes, partial, no, not_covered.

**`data/crosswalk.csv`**
```
indicator_id,scheme,requirement_text,numeric_threshold,audit_method,industry_authored,products_measuring_direct,products_measuring_proxy,any_external_validation,icar_validated_any,query_shortlist,query_instrumented_not_required,query_required_manual_only,notes
```
`scheme` one of: RSPCA_Assured, FARM_v5, GAP_dairy, Certified_Humane. `audit_method` one of: visual_inspection, records_review, sensor_accepted, unspecified. `industry_authored` yes for FARM_v5 rows, no otherwise. The three `query_` columns are yes or no and are computed by scripts/stats.py, not typed by hand.

**`data/scorecard.csv`**
```
product_id,indicator_validity,validation_evidence,logging,data_lineage,access_ownership,tamper_evidence,disclosure,assessable_dimensions,total,meets_threshold,legal_required_somewhere,evidence_urls,notes
```
Each dimension one of: 0, 1, 2, NA. `assessable_dimensions` is the count of non NA dimensions. `total` sums the non NA dimensions. `meets_threshold` is yes, no, or not_assessable, computed by scripts/stats.py using the threshold in rubric.md. `legal_required_somewhere` yes if the product is sold in the EU and scores below 2 on access_ownership (Data Act).

**`data/reliability.csv`**
```
claim_id,field,coder_a_original,coder_a_recode,coder_b,agree_a_a,agree_a_b
```

### 6. `standard/coding_frame.md`

Sections: Purpose. Unit of analysis (one claim is one assertion about welfare, health as a welfare proxy, or compliance, attributable to one product from one public source). Fields, as a table matching the claims.csv columns, each with allowed values and a one line definition. Rules, as numbered paragraphs: a claim repeated across pages is coded once with the first URL and the repetition noted; "improves welfare" with no indicator is outcome_claim with mapped_indicator_id empty and mapping_confidence none; a page behind login is a single row with claim_type no_public_documentation; accuracy figures without a stated population are evidence_cited vendor_internal; a peer reviewed paper by the vendor's own staff is vendor_internal unless an independent population is used; mapping_confidence unsure is always allowed and always goes to kevin_questions.md. Pilot procedure: code four products, list every ambiguity, revise, log in decisions.md, then code the rest. Reliability procedure: after coding, sample 10% of claim_ids at random with a fixed seed, re code blind after seven days, have a second coder do the same rows, record in reliability.csv, report percentage agreement per field in the write up. Change log table at the end.

### 7. `standard/rubric.md`

A table of the seven dimensions with the 0, 1, 2 criteria exactly as in docs/PLF_Audit_Standard_Plan.md, plus an NA definition per dimension (what absence of documentation looks like for that dimension). Then a section "Pass threshold, fixed before scoring" with this text: a product meets the standard when all seven dimensions are assessable, no dimension scores 0, and the total is at least 9 of 14. A product is not assessable when three or more dimensions are NA. Then a section "Source of each requirement" as a table: dimension, source regime, citation. Leave the citation cells filled from the CLAUDE.md list. Then a change log table.

### 8. `standard/standard_v0.1.md`

Headings only, with a one line note under each saying what goes there: Purpose. Scope (link to scope_note.md). Definitions (welfare claim, indicator, validated indicator, external validation, raw reading, alert, lineage). Structure (the four columns). Requirements (seven groups, each with requirement, rationale, source). Assessment procedure. Versioning and annual refresh. What this standard does not cover.

### 9. `standard/scope_note.md`

Write this one in full, about 150 words: the standard takes no position on whether precision livestock farming improves animal welfare. It applies only to systems that make a welfare claim, and it specifies what such a system must log, retain, expose and disclose so that the claim can be verified by a party outside the vendor. A system that makes no welfare claim is out of scope. The standard does not endorse the substitution of monitoring for husbandry, does not treat a validated sensor as evidence that an animal's welfare is good, and does not treat a high score as a welfare outcome. It treats a welfare claim the way a claims substantiation regime treats any objective claim: if made, it must be provable. Cite Tuyttens et al. 2022 for the indirect threats and Simoneau-Gilbert and Birch 2024 for the transparency principle.

### 10. `logger/README.md`

Specification only, no code yet. Three files to be written in week 4: logger.py with commands append, alert and export; verify.py that walks the chain and checks every alert references existing earlier readings; demo.py that writes 1,000 readings and 10 alerts, verifies, tampers with one reading, and shows the verifier catching it. Record format: seq, ts_utc, sensor_id, payload, model_version, prev_hash, hash where hash is sha256 over the concatenation of the other fields. Standard library only. Under 300 lines total. A table mapping each of the seven dimensions to the feature that satisfies it, to be filled in when the code exists.

### 11. `writeup/` files

`report.md`: headings only, from the plan's week 5 structure. `certifier_annex.md`: headings: Purpose. When this annex applies (a scheme accepts sensor data in place of or alongside inspection). Requirements a sensor system must meet for its data to be accepted (the seven, one paragraph each). How an auditor checks each one from documentation. Worked example. `icar_note.md`: headings: What ICAR validates today. What a welfare claim category would add. Proposed evidence and logging requirements. What it would cost a vendor (link to logger). `onepager.md`: headings only.

### 12. `notes/` files

`decisions.md`: heading and a first entry dated today: repository created from spec, threshold set per rubric.md, product cap 15 to 20 plus one comparator. `kevin_questions.md`: heading, a section "Open" with the five questions from the plan plus "Which of the three theory of change pathways is primary," and a section "Answered." `duplication_check.md`: headings for ICAR, Maroto Molina 2020, Stygar 2021, Tuyttens 2022, Elliott and Werkheiser 2023, Berckmans 2017, Boyland group at RP, each with the line "not yet checked." `weekly_status.md`: a table with columns week, planned, done, blocked, sent to Kevin, and a row for week 1.

### 13. Scripts

`scripts/validate_csv.py`: reads every CSV in data/, checks the header matches the schema above exactly, checks every enumerated field contains only allowed values, checks product_id in claims and scorecard exists in products, checks indicator_id in crosswalk exists in indicators, prints one line per file (OK or the first error), exits non zero on any error. Standard library only.

`scripts/stats.py`: reads data/, prints: product count and comparator count; claims per product; share of claims by claim_type, mapping_confidence and evidence_cited; number of claims with legal_flag set; for the crosswalk, computes and writes back the three query columns; for the scorecard, computes assessable_dimensions, total and meets_threshold using the threshold from rubric.md, and prints the two headline numbers (assessable products, and products meeting the standard among them) plus the per dimension distribution including NA counts; for reliability.csv, prints percentage agreement per field. Works on empty files without crashing. Standard library only.

### 14. Git

`git init`, add everything except what .gitignore excludes, commit with message "Week 0: repository scaffold from spec." Then show me `git log --oneline` and the tree.

---

## What the next session will do (do not start it now)

Week 1 tasks from docs/PLF_5_Week_Plan.md with the Part 4 changes from docs/PLF_Project_Resources.md applied: duplication check starting with ICAR and Maroto Molina, column 4 first draft from the legal sources, product list from Stygar plus ICAR plus market scan capped at 15 to 20 plus AI4Animals, coding frame tested on three real claims, indicators.csv filled from EFSA and Welfare Quality with Maroto Molina's technology mapping.
