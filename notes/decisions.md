# Decisions

Every coding or scoring decision not already covered by the coding frame or the rubric is entered here, dated, before it is applied. The frame or rubric is then updated so the next case is covered.

## 2026-09-16: repository created from spec

Repository created from `docs/PLF_Repo_Spec_For_ClaudeCode.md`. The pass threshold is set in `standard/rubric.md` and fixed before any scoring: all seven dimensions assessable, no dimension at 0, total at least 9 of 14, and a product is not assessable at three or more NA. The product cap is 15 to 20 dairy products plus AI4Animals as a comparator, following point 8 of Part 1 of the resources doc.

## 2026-09-16: scaffold choices the spec left open

**Corpus kept out of git entirely.** The spec's `.gitignore` excluded only PDF and HTML files, but several corpus files are pasted Markdown, including the Aeon essay, the EA Forum posts and legal text, and some of that is copyrighted. `.gitignore` now excludes everything in `corpus/` except `corpus/README.md`.

**The crosswalk is a full grid.** It holds one row per indicator per scheme for every indicator in `data/indicators.csv`. An empty requirement_text means that scheme does not require the indicator, and audit_method is then left empty. Without these rows the second query, indicators instrumented but required by no scheme, would have nowhere to be recorded.

**The three queries as `scripts/stats.py` computes them.** The shortlist is yes for every row of an indicator that at least one product measures directly and that FARM v5 requires. Instrumented but not required is yes for every row of an indicator that at least one product measures directly or by proxy and that no scheme requires. Required but manual only is decided per row: that scheme requires the indicator, audits it by visual inspection, and some product measuring it has external validation. I made it per row rather than per indicator because a certifier acts on its own scheme.

**NA versus 0 on validation evidence and disclosure.** Both criteria are about what has been published, so finding nothing published scores 0, not NA. NA on these two is kept for a product that cannot be identified precisely enough to search. On logging, lineage, access and tamper evidence, silence in the documentation is NA. This will shape the headline numbers and should be shown to Kevin with the rubric.

**Headline numbers exclude the comparator.** AI4Animals is scored but reported on its own line.

**Reliability agreement is computed.** `scripts/stats.py` fills agree_a_a and agree_a_b from the coder columns, so they are never typed by hand.

**Plan text in Markdown.** `docs/PLF_Audit_Standard_Plan.md` is a text extraction of the .docx, with a header note saying where the resources doc supersedes it (Berckmans 2022 citation, GlobalGAP, product cap).

**Open, to decide before scoring.** `legal_required_somewhere` depends on whether a product is sold in the EU, and `data/products.csv` has no column for that. It also needs a rule for when access_ownership is NA. Both need a decision here before week 4.
