# PLF Welfare Audit Standard (dairy v0.1)

Can a welfare claim made by a dairy sensor system be verified by someone outside the vendor, and what would the system have to log and expose to make that possible?

## Deliverables

| # | Deliverable | Files |
|---|---|---|
| 1 | Claims register for 15 to 20 dairy products plus one comparator, with a reliability figure | `data/claims.csv`, `standard/coding_frame.md`, `data/reliability.csv` |
| 2 | Crosswalk joining what certification schemes require to the existing indicator and sensor mapping | `data/indicators.csv`, `data/crosswalk.csv` |
| 3 | Standard v0.1 with rubric and scope note | `standard/standard_v0.1.md`, `standard/rubric.md`, `standard/scope_note.md` |
| 4 | Scorecard of every product on seven dimensions | `data/scorecard.csv` |
| 5 | Reference logger with verifier | `logger/` |
| 6 | Write up, certifier annex, ICAR note, one pager | `writeup/` |

## Method

Everything here comes from public documentation: vendor marketing pages, manuals, developer documentation, patents, published papers and recorded talks. No vendor was contacted. I code every welfare claim against a fixed frame written before coding began, and I score each product on seven dimensions against a written rubric. The pass threshold was fixed in `standard/rubric.md` before any product was scored. Where a vendor publishes too little to judge a dimension, the scorecard records NA rather than zero, and the number of products that cannot be assessed is reported as a finding in its own right. Welfare indicators are taken from the EFSA 2023 dairy cow opinion and the Welfare Quality dairy protocol, never from my own judgement.

Reliability is checked the same way throughout. A random 10% of claims, drawn with a fixed seed, is re coded blind at least seven days after the original coding, and a second coder codes the same rows. Agreement per field is reported in the write up.

The source documents are not in this repository because several are large and some are copyrighted. `corpus/README.md` lists every file with its source so the folder can be rebuilt.

## How to re run the scoring next year

Start from the previous tag. Update `data/products.csv` for products that have launched, been renamed or been withdrawn. Re code the claims against the current coding frame, capturing each source again with a fresh date, and re score every product against the rubric. Then run the two scripts.

```
python scripts/validate_csv.py
python scripts/stats.py
```

Compare the data and the printed numbers with the previous release using `git diff v0.1 -- data/`. Any change to the coding frame or the rubric is logged in `notes/decisions.md` before it is applied, and a changed pass threshold is reported next to the old one. Tag the result as the next version.

## Licence

Data and text are licensed CC BY 4.0. Code is licensed MIT.

## Credits

Author: Manisha Sarkar. Mentor: Kevin Xia, Rethink Priorities. Programme: Sentient Futures incubator, fall 2026.
