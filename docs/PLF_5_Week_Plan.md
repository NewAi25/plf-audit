# PLF Welfare Audit Standard: five week execution plan
Dairy v0.1. Starts Monday 15 September, ends Sunday 19 October. The two weeks after that are buffer, revisions and the cohort presentation.

**Revised 15 September after the critical review in `PLF_Project_Resources.md` Part 1.** The changes, which override anything below that contradicts them: columns 1 and 2 of the crosswalk are taken from Maroto Molina 2020 and Stygar 2021, not built; the novelty is column 3 joined to them, plus column 4. Product list capped at 15 to 20 plus AI4Animals as a comparator, patents for five vendors only. Column 4 is drafted in week 1 from the legal sources and refined later, in parallel with the register. A 10% blind re code reliability check is added in week 3. The scorecard reports two numbers, products assessable from public documentation and products meeting the standard among those, with the threshold fixed in `rubric.md` before scoring. A scope note stating the standard takes no position on PLF itself. A legal column on the scorecard (Data Act). Two extra deliverables: a two page certifier annex and a one page ICAR note. Cut: the corpus as a deliverable, the broiler transfer test. The theory of change question goes to Kevin first.

Working assumption: 15 to 20 hours a week. Every week has four kinds of task. **Read** means sit with a document and extract something specific into a file. **Research** means go and find things you do not yet have. **Build** means produce an artifact. **Do** means an action involving another person. Each week ends with a definition of done. If Friday comes and it is not done, the weekend is for that, not for starting the next week.

Everything lives in one folder, `plf-audit/`, and from week 2 that folder is a git repo. Structure:

```
plf-audit/
  corpus/           source PDFs and saved pages, one subfolder per source type
  data/
    products.csv
    claims.csv
    crosswalk.csv
    scorecard.csv
  standard/
    coding_frame.md
    rubric.md
    standard_v0.1.md
  logger/
    logger.py
    verify.py
    README.md
  writeup/
    report.md
    onepager.md
  notes/
    duplication_check.md
    kevin_questions.md
    decisions.md
```

---

## Week 1 (15 to 21 September): foundation and the duplication check

Goal: by Sunday you know exactly what exists, you have every source document in one place, you have the product list, and the claims coding frame is written. Nothing is scored yet.

### Read

1. **ICAR Guidelines Section 11** (icar.org/Guidelines/11-Milk-Recording-Devices.pdf) and the **ICAR validated sensor systems page**. Extract into `notes/duplication_check.md`: what ICAR tests, what the test plan covers, what the Statement of Validation says, and a list of everything it does *not* cover (logging, lineage, ownership, tamper evidence, disclosure). Also copy every product on their validated list into `data/products.csv` with a column `icar_validated = yes`. About 3 hours.
2. **Stygar et al. 2021** full text on PMC (PMC8044875), including supplementary tables. Extract the product table into `data/products.csv`: vendor, product, sensor type, what it measures, validation status (none / internal / external), reference. Note their actual conclusions in `notes/decisions.md`: lying, standing, rumination validated well; active behaviour, BCS, health detection worse; low potential for appropriate behaviour. About 3 hours.
3. **Tuyttens, Molento and Benaissa 2022, Twelve Threats** (PMC9186058). One page of notes: the four threat categories, the two direct threats you score (poor external validation, meaningless indicators). Note the authors correctly. 1 hour.
4. **Elliott and Werkheiser 2023, A Framework for Transparency in PLF** (PMC10648797). One page of notes: the four kinds of information, the four audiences, and a list of every verification mechanism they do *not* specify. That list is your gap statement. 1 hour.

### Research

5. **Market scan for products launched since 2021** that Stygar could not have covered. Search vendor sites and trade press for Lely, DeLaval, Nedap, Allflex/SCR (now MSD Animal Health), CowManager, smaXtec, Afimilk, Moocall, Connecterra, Cainthus/Ever.Ag, Boumatic, GEA. Add to `data/products.csv` with `source = market_scan`. Pick the final 20 to 25: prefer products that make an explicit welfare claim in their marketing, and cover at least three sensor types (accelerometer or collar, bolus, camera, milking system). 3 hours.
6. **Natasha Boyland's group at RP.** Search RP's site and the EA Forum for anything on PLF, sensors, welfare technology or certification from her team. Write one paragraph in `notes/duplication_check.md`: overlap or none, with links. 1 hour.
7. **Gather the corpus.** Download into `corpus/`: EFSA 2023 dairy cow opinion (doi 10.2903/j.efsa.2023.7993), Welfare Quality dairy protocol PDF, RSPCA Assured dairy cattle standards (April 2026 version) plus the RSPCA standards justification document for dairy, National Dairy FARM Animal Care Version 5 manual, Global Animal Partnership dairy standard, Certified Humane dairy standard, EU AI Act Articles 12, 13 and 26, ICAR Section 11, the four papers above. Then index it with your retrieval setup so you can query across it. 3 hours.

### Build

8. **`standard/coding_frame.md`, the claims coding frame.** This is the fixed frame for #9 and the most important artifact of week 1. Write it before you code a single claim. Fields for `data/claims.csv`:

   | Field | Values |
   |---|---|
   | claim_id | sequential |
   | product_id | links to products.csv |
   | claim_text | verbatim quote |
   | source_url | where found |
   | source_type | marketing page / product manual / API or developer doc / patent / peer reviewed paper / press release |
   | date_captured | ISO date |
   | claim_type | indicator claim (we detect X) / outcome claim (welfare improves) / accuracy claim (X% sensitivity) / compliance claim (meets scheme Y) |
   | mapped_indicator | the EFSA ABM or Welfare Quality measure it maps to, or "none" |
   | mapping_confidence | direct / proxy / none |
   | evidence_cited | none / vendor internal / independent external / peer reviewed |
   | evidence_ref | citation or link if any |
   | notes | free text |

   Plus written rules: what counts as one claim, how to handle a claim repeated across pages, how to handle "helps improve welfare" with no indicator named (code as outcome claim, mapped_indicator none), and what to do when a page is behind login (record as "not publicly accessible"). 2 hours.

9. **`data/products.csv` finalised** with the 20 to 25 products, each with vendor, product, sensor type, country, Stygar validation status, ICAR validated flag, and the URLs of its marketing page, manual, developer docs and any patents. 1 hour after steps 2 and 5.

### Build, added in the revision

9b. **First draft of column 4 in `standard/standard_v0.1.md`.** Seven requirement groups, each with a one line requirement, a rationale, and the source it is borrowed from: EU Data Act Chapter II for access and ownership, AI Act Article 12 and 26(6) for logging and retention, Rutten 2013 for lineage, ICAR's application checklist for disclosure, SOC 2 and certificate transparency practice for tamper evidence, Stygar and Gómez's internal versus external distinction for validation evidence. This does not wait for the register. 3 hours.
9c. **`standard/scope_note.md`** per the repo spec. 30 minutes.
9d. **Read Maroto Molina 2020** and extract their measure to technology table into `data/indicators.csv` alongside the EFSA and Welfare Quality columns. This is column 1 to 2, done. 2 hours. Move the EFSA and Welfare Quality extraction from week 2 into this week to sit beside it.

### Do

10. **Send Kevin the updated plan doc** (`PLF_Audit_Standard_Plan.docx`) with a two line note: dairy confirmed, ICAR found as the nearest existing scheme, plan updated. Ask him the theory of change question first: certifier annex, ICAR note, or substantiation evidence base as the primary target. Everything in weeks 3 to 5 is shaped by his answer.
11. **Book the follow-up call** for the week of 21 September if not already done.
12. **Ask Kevin one question by message:** does RP or anyone he knows have contact with ICAR or a welfare certifier's technical team, for later. Not vendors. Just so the door exists when the standard is ready.

### Done when
`products.csv` has 20 to 25 rows with all URLs. `coding_frame.md` is written and you have tested it mentally against three real claims. `duplication_check.md` says in one paragraph why ICAR, Stygar, Tuyttens and Elliott/Werkheiser do not occupy the gap. The corpus is indexed. Kevin has the plan.

---

## Week 2 (22 to 28 September): the claims register, Kevin's #9

Goal: every welfare claim from every product, coded. This is the raw data everything else is built on, and it is a project deliverable in its own right.

### Build

1. **Pilot on 3 to 4 firms, Monday and Tuesday.** Pick one product each from Lely, DeLaval, smaXtec and one camera product. Code every welfare claim you can find across marketing, manual, developer docs, patents. Expect 8 to 20 claims per product. After the pilot, revise the coding frame: which fields were ambiguous, which values were missing, which rules did you need that you had not written. Log every change in `notes/decisions.md` with the date. This is what makes the register defensible when Kevin asks how you coded something. 6 hours.
2. **Code the remaining products, Wednesday to Saturday.** Same process. Aim for 3 to 4 products a day. Keep a running count. Where a vendor publishes almost nothing, that is data: record one row with claim_type = "no public technical documentation" so the absence shows in the register. 10 hours.
3. **First look at the numbers, Sunday.** From `claims.csv`, compute: total claims, claims per product, share by claim_type, share with mapped_indicator = none, share with evidence_cited = none, share by evidence level. Write these into `writeup/report.md` as a first findings section, plain numbers, no interpretation yet. 1 hour.

### Read

4. **EFSA 2023 dairy opinion, sections on the five welfare consequences and their ABMs.** Extract every animal based measure into a draft `data/indicators.csv`: indicator_id, EFSA consequence, ABM name, how it is measured in the opinion. Then the **Welfare Quality dairy protocol** measure list, merged into the same file with the WQ principle and criterion. This is column 1 and you need it ready for week 3. 3 hours.

### Do

5. **Kevin call, week of the 21st.** Bring the pilot results (3 to 4 firms coded) and the coding frame. Ask him to look at five specific claim mappings where you were unsure whether the claim maps to an indicator directly or to a proxy. Those are the welfare science calls you said you would hand to him. Write his answers into `notes/decisions.md`.
6. **Message Kevin midweek** with the running count and one interesting finding, whatever it is. Keeps him engaged without a meeting.

### Done when
`claims.csv` covers every product. Every row has every field filled or an explicit "not found". `coding_frame.md` reflects the post pilot revisions with a change log. First numbers are in `report.md`. Kevin has ruled on your five unsure mappings.

---

## Week 3 (29 September to 5 October): the crosswalk, Kevin's #13, and drafting column 4

Goal: the three column crosswalk built and queried, and the first draft of what a system must log and prove.

### Read

1. **RSPCA Assured dairy standards plus the standards justification.** For every requirement that names an animal based indicator, add a row to `data/crosswalk.csv`: indicator_id, scheme = RSPCA, requirement text, numeric threshold if any, how it is audited (visual inspection / records / sensor accepted). The justification document tells you why each requirement exists; put that in a notes column, it makes the crosswalk defensible. 3 hours.
2. **FARM Animal Care Version 5.** Same extraction. FARM has numeric thresholds (locomotion score 3 at 5% or less, moderate lameness 15% benchmark), record those exactly. Mark `industry_authored = yes` for every FARM row, since NMPF wrote it. 2 hours.
3. **Global Animal Partnership dairy and Certified Humane dairy.** Same extraction, lighter. 2 hours.
4. **EU AI Act Article 12 (record keeping), Article 13 (transparency), Article 26(6) (log retention).** Read them as a template. In `standard/standard_v0.1.md` start a section called "Logging and evidence requirements" and write your requirements next to the Article 12 text, marking each one as borrowed or new for the farm setting. 2 hours.

### Build

5. **`data/crosswalk.csv` complete.** One row per indicator per scheme, joined to column 2 from `claims.csv` (which products claim to measure this indicator, and at what mapping confidence and evidence level) and to ICAR's validated list. 3 hours.
6. **Run the three queries** and write results into `report.md`:
   - Indicators that pass all three of Kevin's filters: measurable by AI (at least one product measures it directly), acceptable to industry (appears in FARM), covered by a scheme or sensor. This is the shortlist to steer towards.
   - Indicators instrumented by at least one product but required by no scheme. The cheap ask for certifiers.
   - Indicators required by a scheme but audited only by visual inspection, where a product with external validation exists. Where a sensor could replace an inspection.
   2 hours.
7. **Draft column 4 requirements**, the first version of the standard's core. Seven requirement groups, each with a one line requirement, a rationale, and a borrowed-from reference:
   - Validation evidence: published external validation on a population other than the training population, with method.
   - Logging: raw readings and derived alerts both retained, timestamped, with defined retention (AI Act Art 26(6) gives six months as a floor; argue for longer given audit cycles).
   - Data lineage: any alert traceable to the raw readings, model version and threshold that produced it.
   - Access and ownership: farmer can export raw data in an open format; certifier can be granted read access; ownership stated in terms.
   - Tamper evidence: records append only or hash chained; edits leave a trace.
   - Disclosure: accuracy and validation figures published with method.
   - Alert audit trail: every alert, its timestamp, and any human action on it, retained.
   3 hours.

### Build, added in the revision

7b. **Reliability check.** Sample 10% of claim_ids with a fixed random seed. Re code them blind without looking at the originals (do this at least seven days after the original coding, so early in week 3 for claims coded early in week 2). Record in `data/reliability.csv`. Send the same rows to Kevin or a second coder he names. Run `scripts/stats.py` for percentage agreement per field. If any field is below 80%, tighten the frame rule for that field, log it, and re code the affected rows. 3 hours plus Kevin's hour.

### Do

8. **Send Kevin the crosswalk and query results** by Friday with three questions: does the shortlist look right to a welfare scientist, is FARM an acceptable industry acceptability proxy, and does he see anything in column 1 that should not be there. Send the reliability sample with it.

### Done when
`crosswalk.csv` is complete for four schemes. The three query results are in `report.md` with the actual lists. Column 4 has seven requirement groups drafted with references. Kevin has the crosswalk.

---

## Week 4 (6 to 12 October): standard v0.1, the scorecard, and the logger

Goal: the standard is frozen, every product is scored, and the reference logger proves the requirements are cheap.

### Build

1. **`standard/rubric.md`, the scoring criteria text.** For each of the seven dimensions, write what 0, 1 and 2 mean in enough detail that a second person would score the same way. Include the rule that "insufficient public documentation to assess" is recorded as a result with its own code, not as a 0. 2 hours.
2. **Score all products, Monday to Wednesday.** `data/scorecard.csv`: product_id, seven dimension scores, an evidence URL for each score, a documentation_sufficiency flag, total. Score from `claims.csv` and the product's docs only. Where you are unsure, record both candidate scores and the reason, and resolve them in one batch at the end so you are consistent. 8 hours.
3. **Compute the headline numbers.** How many products score 2 on validation evidence. How many score 0 on tamper evidence. How many are unassessable on disclosure. Median total. Distribution per dimension. And the answer to Kevin's original question: with a pass threshold you define and justify in `rubric.md` (for example, no dimension at 0 and total at least 9 of 14), how many products pass. Put it all in `report.md`. 1 hour.
4. **Build the reference logger, Thursday to Saturday.** Python, no dependencies beyond the standard library, under 300 lines total.
   - `logger.py`: `append` command takes a sensor id and a JSON payload, writes a record `{seq, ts_utc, sensor_id, payload, model_version, prev_hash, hash}` to an append only JSONL file, where `hash = sha256(seq + ts + sensor_id + payload + model_version + prev_hash)`. An `alert` command writes an alert record that references the seq numbers of the raw readings it was derived from. An `export` command dumps the file in CSV for the farmer.
   - `verify.py`: walks the chain, recomputes every hash, reports the first broken link if any, and for every alert confirms the referenced readings exist and precede it.
   - `demo.py`: writes 1,000 readings and 10 alerts, verifies, then edits one reading in place and shows the verifier catching it.
   - `README.md`: a table mapping each of the seven column 4 requirements to the feature that satisfies it, and the line count. That table is the argument: this is what it costs.
   6 hours.
5. **Freeze `standard/standard_v0.1.md`.** Sections: purpose and scope, definitions, the four column structure, the seven requirement groups with criteria, the scoring rubric, how to run an assessment, versioning and annual refresh, what this standard does not cover. 3 hours.

### Do

6. **Send Kevin the scored scorecard and the pass count** with one question: name products publicly, or anonymise the public version. You need his answer before week 5 writing.
7. **Ask Kevin for one or two external reviewers** for the write up. Someone at a certifier's technical team would be ideal. Not vendors.

### Done when
`scorecard.csv` is complete with evidence links. `standard_v0.1.md` is frozen. `logger/` runs end to end and `demo.py` shows tamper detection. `report.md` has the headline numbers and the pass count. Kevin has decided on naming.

---

## Week 5 (13 to 19 October): write up, review, publish

Goal: everything public, in the form the first user needs.

### Build

1. **`writeup/report.md`, the full write up, Monday to Wednesday.** Structure:
   - The question, in Kevin's words.
   - What exists and where it stops (ICAR, Stygar, Tuyttens, Elliott/Werkheiser), one paragraph each.
   - Method: public docs only, the coding frame, the rubric, the pass threshold, all with links to the files.
   - Findings from the claims register: the numbers from week 2, with the three or four most telling examples (anonymised or named per Kevin's decision).
   - Findings from the crosswalk: the three query results as lists, with what each implies for a certifier.
   - The scorecard: distribution, headline numbers, how many pass, the "unassessable" count as a finding.
   - The standard: what it requires and why, with the borrowed-from references.
   - The logger: what it cost to implement the requirements, line count, link to repo.
   - What this does not show, honestly: one species, public docs only, no field validation of the standard, welfare science taken from EFSA and Welfare Quality not assessed independently.
   - Next steps: who should pick this up and what the second species would take.
   About 3,000 words. 8 hours.
2. **`writeup/certifier_annex.md`**, two pages: when the annex applies (a scheme accepts sensor data alongside or instead of inspection), the seven requirements a sensor system must meet for its data to be accepted, how an auditor checks each from documentation, one worked example from the scorecard. This is the primary deliverable if Kevin confirms the certifier pathway. 3 hours.
2b. **`writeup/icar_note.md`**, one page: what ICAR validates today (three systems, none welfare, validation against the applicant's own claim), what a welfare claim category would add, the evidence and logging requirements, what it would cost a vendor with a link to the logger. 1 hour.
2c. **`writeup/onepager.md`** for whoever Kevin names as first user. The gap in two sentences, what the standard requires, the two headline numbers, what adopting it would take, a link to the repo. 1 hour.
3. **Publish the repo** with all data as CSV, the standard, the logger, and a README that says how to re-run the scoring next year. Tag it v0.1. 1 hour.

### Do

4. **Send the write up to Kevin and the reviewers on Wednesday.** Ask for comments by the following Monday. While waiting, prepare the cohort presentation from the report.
5. **Post the write up** to the EA Forum or wherever Kevin advises, after his comments are in. If that slips into the buffer weeks, fine.
6. **Update Kevin's Top 30 doc** with a comment on #9 and #13 pointing to the repo, so the next person who reads his list finds the work.

### Done when
Report and one pager written. Repo public and tagged. Kevin and reviewers have the draft. Presentation outline exists.

---

## Buffer (20 October to early November)

Revisions from Kevin and reviewers. Cohort presentation. If there is time, the broiler transfer test: extract column 1 from EFSA's broiler opinion and Welfare Quality's poultry protocol, and column 3 from RSPCA Assured broiler standards and the Better Chicken Commitment, and show the standard swaps species by replacing two columns.

## Weekly rhythm

Monday: read tasks. Tuesday to Thursday: build tasks. Friday: send Kevin whatever the week produced with one specific question. Weekend: whatever is not done. Keep `notes/decisions.md` current every day you work; it is what lets you answer "why did you code it that way" in November.

## The three things most likely to derail this

- **Coding claims takes longer than planned.** If by Thursday of week 2 you are under half way, cut the product list to 15 and say so in the method. Fifteen fully coded products beat twenty five half done.
- **Column 1 judgement calls.** Do not make them. Batch every unsure mapping into a list for Kevin and keep moving with the ones that are clear.
- **The logger grows.** It exists to prove cost, not to be a product. If it passes 300 lines, stop adding.
