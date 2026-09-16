# Scoring rubric

Version 0.1, 16 September 2026. Every product is scored on seven dimensions, each 0, 1, 2 or NA, from public documentation only. The 0, 1 and 2 criteria below are the ones in the plan shared with Kevin (`docs/PLF_Audit_Standard_Plan.md`). In week 4, before any scoring, each criterion gets fuller text so that a second person would reach the same score. The pass threshold further down is fixed now and does not move once scoring starts.

## Dimensions

| Dimension | 0 | 1 | 2 | NA: not assessable from public documentation |
|---|---|---|---|---|
| Indicator validity | Measures nothing that maps to a validated indicator | Measures a proxy | Measures a validated indicator directly | The documentation does not say what the product measures beyond general terms such as "monitoring" or "insights". |
| Validation evidence | None published | Internal validation only | External validation, published, independent | Used only when the product cannot be identified precisely enough to search for validation studies, for example an unnamed model generation. The criterion is about publication, so finding no published validation is a 0, not an NA. |
| Logging | Alerts only, raw data not kept | Raw readings kept | Raw readings plus alerts, timestamped, defined retention | The documentation does not say whether raw readings are kept, or for how long. Silence is not evidence that only alerts are kept. |
| Data lineage | Cannot trace an alert to source | Partial | Any alert traceable to raw readings and model version | The documentation does not describe how an alert relates to the readings or the model that produced it. |
| Access and ownership | Vendor locked, no export | Export possible | Farmer and certifier can access, ownership stated | Neither the documentation nor the public terms of service say anything about export, API access, third party access or data ownership. |
| Tamper evidence | Records editable without trace | Edit log | Append only or hash chained | The documentation does not say whether stored records can be changed or how changes are recorded. |
| Disclosure | No accuracy or validation figures published | Partial | Published with method | Used only when the product cannot be identified precisely enough to look for published figures. Finding no published figures is a 0, not an NA. |

## Pass threshold, fixed before scoring

A product meets the standard when all seven dimensions are assessable, no dimension scores 0, and the total is at least 9 of 14. A product is not assessable when three or more dimensions are NA.

A product with one or two NA dimensions is assessable but cannot meet the standard, because meeting it requires all seven dimensions to be assessable. It is recorded as not meeting the threshold. The reasoning behind 9 of 14 is that, with no zeros allowed, a product must at least partly satisfy every dimension and fully satisfy at least two of them.

The scorecard reports two headline numbers for the dairy products: how many are assessable, and how many of those meet the standard. AI4Animals is scored the same way and reported separately as the comparator.

`scripts/stats.py` reads the threshold from this table. The values were fixed on 16 September 2026, before any product was scored. If they ever change, the change gets an entry in `notes/decisions.md` and the old threshold is reported alongside the new one.

| Parameter | Value | Meaning |
|---|---|---|
| `pass_max_na` | 0 | Most NA dimensions a passing product may have |
| `pass_max_zero_dimensions` | 0 | Most dimensions at 0 a passing product may have |
| `pass_min_total` | 9 | Lowest total of the assessable scores for a pass |
| `not_assessable_min_na` | 3 | NA count at which a product is not assessable |

## Source of each requirement

| Dimension | Source regime | Citation |
|---|---|---|
| Indicator validity | Published welfare indicators and their mapping to sensors | EFSA 2023 scientific opinion on the welfare of dairy cows, doi 10.2903/j.efsa.2023.7993; Welfare Quality assessment protocol for dairy cattle; Maroto Molina et al. 2020, Journal of Dairy Research 87(S1); Tuyttens, Molento and Benaissa 2022 on indicators that do not mean anything for the animal |
| Validation evidence | Validation practice in the PLF literature | Stygar et al. 2021, Frontiers in Veterinary Science 8:634338, for internal versus external validation; Gómez et al. 2021, Frontiers in Veterinary Science 8:660565; Guarino, Norton, Berckmans, Vranken and Berckmans 2017, Animal Frontiers 7(1), for gold standards |
| Logging | EU AI Act, Regulation (EU) 2024/1689 | Article 12 on record keeping and Article 26(6) on retention of at least six months. PLF systems are not high risk under Annex III, so this is borrowed as the EU definition of adequate logging, not cited as a binding rule |
| Data lineage | Four level model of a sensor system | Rutten et al. 2013, Journal of Dairy Science 96(4); an alert at level IV must be traceable to the level I readings behind it |
| Access and ownership | EU Data Act, Regulation (EU) 2023/2854 | Chapter II, user access to product data and sharing with third parties, applicable from 12 September 2025 |
| Tamper evidence | Audit evidence and transparency log practice | SOC 2 trust services criteria; certificate transparency append only logs |
| Disclosure | ICAR sensor validation scheme | ICAR application checklist: technical manual, internal validation studies, peer reviewed publications, routine checking procedures; also EU AI Act Article 13 and Elliott and Werkheiser 2023, Animals 13(21) |

## Change log

| Date | Version | Change | Reason |
|---|---|---|---|
| 2026-09-16 | 0.1 | Rubric and pass threshold written from the repository spec | Threshold fixed before any scoring |
