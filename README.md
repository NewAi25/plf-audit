# PLF Welfare Audit Standard (dairy v0.1)

Can a welfare claim made by a dairy sensor system be verified by someone outside the vendor, and what would the system have to log and expose to make that possible?

## Start here

Five files, in this order, give the shape of the project in about twenty minutes.

| Step | File | What it tells you |
|---|---|---|
| 1 | [`CLAUDE.md`](CLAUDE.md) | The question, the six deliverables, the hard rules, and the fixed citation list |
| 2 | [`docs/reading_order.md`](docs/reading_order.md) | The full reading order for the repository and the sources, with what to look for in each |
| 3 | [`notes/decisions.md`](notes/decisions.md) | Every judgement call in date order, including the mistakes and how they were corrected. Read this before trusting any number |
| 4 | [`data/README.md`](data/README.md) | What each CSV holds, what every column means, and what an empty cell means in each file |
| 5 | [`notes/kevin_questions.md`](notes/kevin_questions.md) | What is unresolved. Every welfare science question is here rather than decided in the data |

The project has four columns. Column 1 is the validated welfare indicators, taken from the EFSA 2023 dairy cow opinion and the Welfare Quality dairy protocol. Column 2 is what commercial sensors measure and how well that has been validated, taken from Stygar et al. 2021 and the claims register. Column 3 is what certification schemes require and how they audit it. Column 4 is what a system must log and prove so a third party can check its welfare claim. Columns 1 and 2 already existed in the literature; columns 3 and 4 are the new work.

## How to verify any number

Every value in `data/` traces to a public source, and the trail is meant to be walked, not trusted. Pick a row in [`data/indicators.csv`](data/indicators.csv), say I001. Its `notes` cell names the EFSA table it came from (Table 16). Open [`corpus/README.md`](corpus/README.md), find `efsa_2023_dairy_cows.pdf`, and follow the File link: it is the exact PDF that was read, and [`corpus/manifest.csv`](corpus/manifest.csv) holds its SHA256 so you can confirm you have the same bytes. Find Table 16 and compare. The same walk works for a product row against the Stygar supplementary spreadsheet, and for any statement in `notes/` against the file it cites.

Three things make the trail hold. First, `python scripts/check_corpus.py` re-fetches every source URL and confirms it still serves the same document. Second, nothing is pushed until a separate auditing agent has checked every factual claim in the change against the sources and returned PASS; the results, including the failures, are in [`notes/audit_log.md`](notes/audit_log.md). Third, every value is one of three kinds and the kind is visible: sourced, with a file and page in the notes; decided, with a dated entry in `notes/decisions.md`; or unknown, recorded as `NA`, `unsure`, `not_covered` or an explicit "missing" rather than left blank or guessed.

What the trail does not do: it does not make the welfare science right. Which indicators are valid is taken from EFSA and Welfare Quality, and where two sources disagree or a mapping is uncertain, the question is in `notes/kevin_questions.md` and the data says `unsure`. It also does not replace a human reading a rendered page where a table layout matters; those cases are named in `decisions.md` when they arise.

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

## Glossary

| Term | Meaning here |
|---|---|
| PLF | Precision livestock farming: sensors, cameras and analytics applied to farm animals |
| Welfare claim | A vendor statement that a product detects, measures or improves an aspect of animal welfare or health presented as welfare |
| Indicator, ABM | An animal based measure: something observed on the animal, such as lameness or lying time, rather than on the housing. Column 1 uses EFSA's ABMs and the Welfare Quality measures |
| Welfare Quality | The EU protocol for on farm welfare assessment; the dairy version has four principles, twelve criteria and thirty one measures |
| EFSA 2023 | The European Food Safety Authority scientific opinion on dairy cow welfare, which names five welfare consequences and the ABMs for each |
| Proxy | A signal a product records that is not the indicator itself but is used to infer it, for example activity as a proxy for oestrus |
| Direct, proxy, none, unsure | The four values of `mapping_confidence` in the claims register. Unsure always goes to Kevin |
| External self validation, external independent validation | Stygar et al. 2021's two levels. Both use herds not used for development; self validation means a developer or company author took part |
| Column 4 | What a system must log and prove: indicator validity, validation evidence, logging, data lineage, access and ownership, tamper evidence, disclosure |
| NA | Not assessable from public documentation. A result with its own code, never scored as 0 |
| Pass threshold | Fixed before scoring in `standard/rubric.md`: all seven dimensions assessable, none at 0, total at least 9 of 14 |
| Welfare washing | Claiming a welfare benefit without evidence. The claims register is the instrument for detecting it |
| Proxy drift | Optimising a measurable proxy that has stopped tracking the animal's interests. The indicator validity dimension is the instrument for detecting it |
| Precision welfare | PLF designed around the animal's interests rather than production alone |
| ICAR | The International Committee for Animal Recording, whose sensor validation scheme is the nearest existing scheme to this standard |
| Corpus | The source documents, listed in `corpus/README.md` and verified by `corpus/manifest.csv`; not committed to git |
| Audit | The pre push check: mechanical validation, then a separate agent verifying every claim against the sources, logged in `notes/audit_log.md` |

## Licence

Data and text are licensed CC BY 4.0. Code is licensed MIT.

## Credits

Author: Manisha Sarkar. Mentor: Kevin Xia, Rethink Priorities. Programme: Sentient Futures incubator, fall 2026.
