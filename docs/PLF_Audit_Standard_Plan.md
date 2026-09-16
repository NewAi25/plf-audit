# PLF Welfare Audit Standard: project plan (dairy v0.1)

> Text extracted from `PLF_Audit_Standard_Plan.docx` on 16 September 2026 so sessions can read it. This is the plan as shared with Kevin in early September. Where it disagrees with `PLF_Project_Resources.md` Part 1 or the revised week plan, those win: the Twelve Threats paper is Tuyttens, Molento and Benaissa 2022 (not Berckmans), GlobalGAP is not a source, the product cap is 15 to 20, and column 4 is drafted in week 1.

Manisha Sarkar, for discussion with Kevin Xia · Sentient Futures Incubator, fall 2026

## The question

A lot of precision livestock farming products are sold as welfare tools. A vendor can say “our camera improves welfare” and right now nobody can check, because there is no agreed list of what such a system should log, disclose or prove. So the question, in your wording: what would a proper technical audit of a “welfare” PLF system actually look like, and how many products out there would pass?

I read your comment on #9 as the infrastructure question rather than the pass/fail question: what tech and data infrastructure a PLF system needs so its welfare claims can be governed at all. That is where the second half of this plan goes. The first half is your #9 and #13 done as you specified them.

Species: dairy cattle for v0.1. Reasons below. Aquaculture and broilers are follow ons if scope allows, and the standard is written so that swapping species means replacing columns 1 and 3 and keeping column 4.

Three outputs. A claims register and scorecard of 20 to 25 dairy PLF products (your #9), the indicator crosswalk (your #13), and a v0.1 audit standard with a reference logger that says what a governable system has to log and prove.

## Why it matters

The best number I have found: Stygar et al. (2021) identified 129 commercially available dairy sensors with a welfare application. Only 18 had been externally validated, meaning tested on a population other than the one they were built on. That is 14%. Gómez et al. (2021) found the same pattern for pigs. So most welfare claims on the market rest on nothing a third party has checked.

Berckmans et al. (2022) list twelve threats PLF poses to welfare. Two of the direct ones are inaccurate predictions from poor external validation, and uptake of indicators that don’t actually mean anything for the animal. Those two threats are what a standard would score.

On the governance side, the EU General Purpose AI Code of Practice (July 2025) lists risk to non human welfare as a systemic risk. That is a real foothold, but it applies to general purpose models, not to narrow farm systems, and there is no technical standard anywhere below it saying what a PLF welfare claim has to demonstrate. So there is a foothold in governance and nothing underneath it technically.

If the standard exists, “be transparent” becomes a checklist. If the scorecard exists, the field has a number for how far the market is from passing. Both are useful on their own, and either could be the starting point for a certifier pilot, a policy submission, or a charity.

## What already exists, and where this sits

I want to be clear about prior work so we are not redoing anything.

Stygar et al. 2021 (dairy) and Gómez et al. 2021 (pigs): systematic reviews of which commercial sensors have been validated. They answer “is the accuracy validated.” They do not cover logging, data ownership, auditability or disclosure. I would build on their product lists rather than rebuild them.

Berckmans et al. 2022, Twelve Threats: a threat taxonomy. Justifies what to score; is not itself a standard.

A Framework for Transparency in PLF (Animals, 2023): says what developers should disclose (goals, how the system works, embedded values, ML characteristics) and to whom (farmers, consumers, regulators, food industry). It is ethical and conceptual. It does not say how anyone would verify any of it: no logging requirements, no data lineage, no tamper evidence, no scoring.

So: they said what to disclose. Nobody has written what a system has to log and prove so a certifier can check it, and nobody has scored products against that. That is the gap.

## Why dairy first

Stygar et al. 2021 already list 129 commercial dairy sensors with validation status coded. The product list and most of column 2 exist before I start.

Welfare Quality has a complete dairy cattle protocol, so column 1 is a lookup from a published source, not my judgement.

RSPCA Assured, GlobalGAP and GAP all publish dairy standards, so column 3 is public.

Dairy vendors (Lely, DeLaval, Nedap, Allflex, CowManager, smaXtec and others) publish more technical documentation than any other livestock sector, which matters when scoring from public docs only.

Net effect: I spend the eight weeks on the audit layer instead of rebuilding the product and indicator lists. The cost is that dairy is the least neglected sector by animal numbers, so the write up needs to show the method transfers to broilers and fish.

## What I would build

Five things, in order.

The corpus. Welfare Quality dairy protocol, Stygar’s product list, vendor documentation and patents for each product, the certification standards, the four prior papers. Collected in one place and indexed with a retrieval setup I already have so I can search across it while working. Reusable afterwards if useful to anyone.

The claims register (your #9). For each of 20 to 25 products, every specific welfare claim in its marketing, documentation and patents, coded against a fixed frame: which welfare indicator it maps to, what evidence is cited, whether validation is internal, external or absent, and where the claim was found. I would write the coding frame first, pilot it on 3 to 4 firms as you suggest, then code the rest. This is the raw data everything else scores from.

The crosswalk (your #13). Four columns, structure below.

The standard, v0.1, and the scorecard. The rubric below applied to every product in the register. Versioned so it can be refreshed annually as you note: year two is a diff against year one, not a new project.

A reference logger. A small hash chained, append only log with a verifier. Its only job is to prove the logging requirements in the standard are cheap to implement. If I can write it in a weekend, a vendor cannot say it is a burden.

## Structure of the crosswalk and standard

This is your #13 crosswalk plus a fourth column. Your original #13 question had three filters: measurable by AI, acceptable to industry, and already covered by sensors or certification. Columns 1 to 3 give the first and third. For industry acceptability I would add a flag on whether the indicator appears in any industry authored code or trade body guidance, as a proxy that needs no vendor contact.

| Column | What it holds | Where it comes from |
|---|---|---|
| 1. Validated welfare indicators | Animal based measures that welfare science has validated for dairy cattle | Welfare Quality dairy protocol, species literature |
| 2. What the sensor measures | The signal each product captures and the indicator it claims to infer | Stygar list, claims register, vendor docs, patents |
| 3. What certification requires | Which indicators each scheme mandates, whether audited by sensor or manual inspection, and whether industry codes also name it | RSPCA Assured, GlobalGAP, GAP, Certified Humane, industry welfare codes |
| 4. What the system must log and prove | Validation evidence, data lineage, access and ownership, tamper evidence, alert audit trail | This is the new part, and it is the same work as SOC 2 / ISO 27001 style audits |

The cells you pointed at fall out as queries on this. Indicators that pass all three of your filters are the shortlist to steer towards, and column 4 says what logging they need to be trustworthy. Indicators already instrumented but not required by any scheme are a cheap ask sitting there for certifiers. Indicators required but only manually audited are where a validated sensor could replace inspection.

## Scoring rubric

Every product, every dimension, 0 / 1 / 2 against a written criterion.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Indicator validity | Measures nothing that maps to a validated indicator | Measures a proxy | Measures a validated indicator directly |
| Validation evidence | None published | Internal validation only | External validation, published, independent |
| Logging | Alerts only, raw data not kept | Raw readings kept | Raw readings plus alerts, timestamped, defined retention |
| Data lineage | Cannot trace an alert to source | Partial | Any alert traceable to raw readings and model version |
| Access and ownership | Vendor locked, no export | Export possible | Farmer and certifier can access, ownership stated |
| Tamper evidence | Records editable without trace | Edit log | Append only or hash chained |
| Disclosure | No accuracy or validation figures published | Partial | Published with method |

A product that scores 0 on disclosure is a finding, not a failure of the method. “Insufficient public documentation to assess” goes in the scorecard as a result. That is also my answer to whether public docs are enough for 20 to 25 products: where they are not, that is itself the point.

## Method and constraints

Public documentation, API references and patents only. No vendor interviews, per your steer. I would rather not spend relationships the movement might need later.

Indicator validity comes from the Welfare Quality dairy protocol, not from my own judgement. Where a product measures something the protocol does not cover, I flag it for you rather than decide.

The claims register, crosswalk and scorecard are kept as structured data with a written coding frame and scoring criteria, so someone else can re-run the scoring next year and get a comparable result.

## Eight week plan

Your estimates were about 20 hours for #9 and 25 for #13. I have more than that available, so the first four weeks cover both with room, and the second four go on the part that is new.

| Week | Work |
|---|---|
| 1 | Duplication check (5 hours). Build the corpus: Welfare Quality dairy protocol, Stygar product list, certification standards, prior papers. Product list: 20 to 25 dairy products from Stygar plus a market scan for anything launched since 2021. Write the claims coding frame. |
| 2 | Pilot the coding frame on 3 to 4 firms. Fix it. Code the remaining products. This is #9. |
| 3 | Draft columns 1 to 3 of the crosswalk from the protocol, the register and the certification standards. Add the industry acceptability flag. Run the three queries. This is #13. |
| 4 | Your review of the register and crosswalk. Fix the animal side. Freeze both. Draft column 4 and the rubric criteria text. |
| 5 | Score all products on the rubric. Log every “insufficient documentation” case. Freeze standard v0.1. |
| 6 | Build the reference logger and verifier. Write the logging requirements in the standard against what the logger actually does. |
| 7 | Write up: the register findings, the crosswalk queries, the scorecard, the standard. Send to you and one or two reviewers. |
| 8 | Revisions. Publish the standard, the register and scorecard as versioned data, and the logger repo. One pager for whoever the first user is. |

First week of November is buffer and the cohort presentation. If I am ahead by week 5, I start the broiler column 1 and 3 as a transfer test rather than widening the dairy scope.

## Deliverables

The claims register and scorecard, published as versioned data that can be refreshed annually. The crosswalk with the three query results. The v0.1 standard. The logger repo with verifier. A write up for the EA Forum or Sentient Futures. A one pager aimed at whoever we decide the first user is. The indexed corpus, if anyone wants it.

## Questions I want to settle with you

Governance target. When you say a “governable system,” do you have a target in mind: a certifier, a retailer procurement standard, an EU instrument, or RP itself? Column 4 has to satisfy someone specific, and this is a sharper version of the first user question.

Naming products. Public scorecard with names, or anonymised public version with the named version shared privately? This is the vendor relations question and I would rather it be your call.

Overlap. Does Natasha Boyland’s group cover any of this? Your notes say to check before anything adjacent.

Industry acceptability. Is “appears in an industry authored code” an acceptable proxy for your filter (b), or do you want something else that does not need vendor contact?

The corpus. Would your team use a searchable version, or should it stay as my own scaffolding?

## Risks and how I would handle them

Thin public docs for some vendors: scored as a result, not treated as a gap in the method.

Welfare science calls I am not qualified to make: indicator column comes from the published protocol; edge cases go to you.

Annoying vendors: no interviews, and the naming decision is yours.

Dairy is the least neglected sector by numbers: the write up shows the transfer path to broilers and fish, and the standard is built so columns 1 and 3 swap out.

Scope creep: v0.1, one species. A second species is a follow on, not part of this sprint.

## Compute

Close to nothing. A Claude seat and free Gemini credits cover the corpus indexing and any classification. No API budget needed beyond that, no GPU.
