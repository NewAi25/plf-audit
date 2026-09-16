# Audit log

One entry per push. An entry is written only after the research-auditor agent has returned AUDIT: PASS on the unpushed changes and both mechanical checks (`scripts/validate_csv.py`, `scripts/check_corpus.py --local`) exit 0. The pre push hook in `.githooks/pre-push` refuses a push whose commit has no PASS entry here.

| Date | Commit audited | Claims checked | Wrong | Unsupported | Imprecise | Result | Summary |
|---|---|---|---|---|---|---|---|
| 2026-09-16 | 524ac03 | About 80 claims on the first run over 59cb13c, 14 corrected items re-verified at 524ac03 | 5 on the first run, 0 after correction | 4 on the first run, 0 after correction | 7 on the first run, 0 after correction | PASS | Week 1 batch: products.csv, indicators.csv, corpus manifest and README, decisions, Kevin questions. First run failed on the blueprint author (Guarino, not Berckmans), a missed EFSA ABM, one misjoin, four Maroto Molina cells, and a stale corpus count. All fixed and re-verified against the PDFs and Crossref. |
