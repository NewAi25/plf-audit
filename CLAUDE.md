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
- Citations: Twelve Threats is Tuyttens, Molento and Benaissa 2022. The transparency framework is Elliott and Werkheiser 2023. The EU PLF blueprint is Guarino, Norton, Berckmans, Vranken and Berckmans 2017, Animal Frontiers 7(1) 12 to 17; never shorten it to Berckmans 2017, the first author is Guarino. Column 1 to 2 mapping is Maroto Molina et al. 2020. GLOBALG.A.P. discontinued its livestock scope and is not a source. ICAR has validated three sensor systems as of September 2026, none measuring a welfare indicator.
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
- Never push without a passing audit. Run the /audit skill: mechanical checks, then the research-auditor agent verifies every factual claim in the unpushed changes against corpus/ and the live web. Push only on AUDIT: PASS, after logging the result in notes/audit_log.md. The pre push hook in .githooks/ enforces this; enable it once per clone with `git config core.hooksPath .githooks`.
- Every corpus file has a row in corpus/manifest.csv with the exact URL its bytes came from and a SHA256. scripts/check_corpus.py verifies both. A new corpus file is not usable until it has a manifest row.
