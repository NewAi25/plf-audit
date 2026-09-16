# PLF audit standard: critical review, mentor's steer, and source pack (v2)
Rewritten 15 September 2026 after a second round of research. Read part 1 before anything else. It changes what you build.

---

## Part 1. The critic's review

I read the plan the way Kevin or an external reviewer would. Eight problems, in order of how much they would hurt you if left alone.

### 1. Columns 1 and 2 of your crosswalk have already been built. Twice.

Maroto Molina et al. 2020, "Welfare Quality for dairy cows: towards a sensor based assessment" (Journal of Dairy Research 87 S1), went through every Welfare Quality measure and asked which PLF technologies can monitor it, and proposed options for the ones that cannot. That is your column 1 mapped to column 2. Stygar et al. 2021 then took the commercial products and coded which are validated. Between them, "which validated indicators can sensors measure" is answered in the literature.

What this means: if you present the crosswalk as new, the first reviewer who knows the field will stop reading. What it also means: two of your four columns arrive mostly done, which frees weeks. The novelty in the crosswalk is column 3 (what certification schemes actually require and how they audit it) joined to columns 1 and 2, plus the industry acceptability flag. Say so explicitly. Cite Maroto Molina as the source of column 1 to 2 mapping and build on it.

### 2. Scoring from public documents means the scorecard will mostly say "unknown"

Logging, data lineage, tamper evidence and retention are rarely described in marketing pages or manuals. Expect the majority of products to be unassessable on three or four of your seven dimensions. If the headline is "how many pass," the honest answer will be "we cannot tell for most of them," and that reads as a failed method unless you design for it.

Fix: change what the scorecard measures. It measures **auditability from the outside**: can a third party, using only what the vendor publishes, verify the welfare claim? That is a legitimate and important quantity, it is exactly what a certifier or a regulator faces, and "not assessable from public documentation" becomes a first class finding rather than an embarrassment. Report two numbers: how many products publish enough to be assessed at all, and of those, how many meet the standard. Set the pass threshold in writing before scoring.

### 3. One coder, no reliability check

You will code several hundred claims and score twenty products alone. Any reviewer will ask how reliable that coding is. You already know the answer from DeskBench: hand grade a sample twice and publish the agreement.

Fix: after coding, pick a random 10% of claims and re-code them blind a week later, and ask Kevin (or a second person he nominates) to code the same 10%. Report both agreement figures in the method. If agreement is poor on a field, tighten the frame and re-code. This costs a day and turns the register from an opinion into data.

### 4. No theory of change

The plan says the standard "could be the starting point for a certifier pilot, a policy submission, or a charity." That is three different projects. Kevin's framing was "integrate PLF and their welfare claims into a governable system," which means the output has to land with someone who governs. Nobody is named.

The research this week found three concrete pathways, and the deliverables should be shaped for one of them:

- **ICAR.** Their validation scheme is real but tiny: three validated sensor systems, all measuring milk yield or composition, none measuring a welfare indicator. The scheme is defined as confirming the device "meets manufacturer performance claims" for "the purpose defined by the applicant." So the one body with machinery to validate dairy sensors has validated zero welfare sensors and validates only what the vendor chooses to claim. A one page proposal to ICAR for a welfare claim category with evidence and logging requirements is a deliverable someone can act on.
- **Welfare certifiers accepting sensor data.** GAP launched its dairy standard with a sensor company partner. RSPCA Assured revised dairy standards in April 2026. When a certifier accepts a sensor reading in place of an inspection, it needs a rule for what that reading must prove. Your column 4 is that rule. Deliverable: a two page annex a certifier could bolt onto an existing standard.
- **Claims substantiation.** In the UK, CAP Code rule 3.7 requires advertisers to hold documentary evidence for any objective claim, and the ASA has ruled on welfare claims before (Red Tractor "high welfare pork" was found problematic). Your claims register, with evidence coded for every claim, is exactly the evidence base an advocacy organisation would need to challenge an unsubstantiated welfare claim. Deliverable: the register itself, published, plus a note on which claims have no cited evidence.

Pick one as primary with Kevin in week 1. My recommendation is the certifier annex as primary, because it is the closest to Kevin's "governable system" and the smallest ask of any institution, with ICAR as the second target. The substantiation route is a by product you get for free from the register and should be mentioned, not built for.

### 5. Column 4 is partly law already, and the plan does not say so

Two things changed the legal ground and neither is in the plan.

The **EU Data Act** applies from 12 September 2025. Users of connected products (which includes farmers using sensors and connected machinery) have a legal right to access the data those products generate and to have it shared with a third party of their choice. Your "access and ownership" dimension is not a nice to have; in the EU a vendor scoring 0 on it may be non compliant. That turns one row of your rubric into a compliance finding.

The **EU AI Act Article 12** requires automatic event logging over the system lifetime for high risk AI systems, with retention of at least six months under Article 26(6). PLF systems are not high risk under Annex III, so the Act does not bind them, but it defines what "adequate logging" means in EU law, and you should borrow the wording.

Fix: cite both in the standard, per requirement, and add a column to the scorecard: "required by law somewhere" yes or no. It makes the standard harder to dismiss as an activist wish list.

### 6. The gap statement is right but the prior work list was incomplete and partly wrong

Corrected and extended:

- The Twelve Threats paper is **Tuyttens, Molento and Benaissa 2022**, not Berckmans.
- The transparency framework is **Elliott and Werkheiser 2023**.
- Daniel Berckmans did lead something relevant: the **EU PLF project** (2012 to 2016) and its 2017 blueprint in Animal Frontiers, which defined key indicators and "gold standards" for validating PLF tools. That is the origin of the validation thinking and should be cited as such.
- **Rutten et al. 2013** (Journal of Dairy Science) gave the field its four level model of a sensor system: technique, data interpretation, integration, decision. Your data lineage requirement is "can you trace a level IV decision back to level I data," and saying it in their terms will land with anyone from the PLF side.
- **ISO/TS 34700:2016**, animal welfare management for organisations in the food supply chain, exists and is what a retailer or processor would point to. It says nothing about technology evidence. Cite it as the management system layer your standard would sit under.
- **GLOBALG.A.P.** discontinued its livestock scope. Remove it.

With that list the gap statement holds: nobody has specified what a PLF welfare system must log and expose so a third party can verify the claim after the fact, and nobody has scored products against such a specification.

### 7. The welfare tech framing carries a risk Kevin's own list flags

Tuyttens et al. list indirect threats: PLF can entrench intensive systems and substitute monitoring for husbandry. A standard that makes welfare sensors more credible could be read as endorsing them. The plan does not address this.

Fix: one paragraph in the standard's scope section. The standard takes no position on whether PLF improves welfare. It says only that when a welfare claim is made, it must be verifiable. A product that makes no welfare claim is out of scope. This is the same position a claims substantiation regulator takes, and it keeps you out of the argument.

### 8. Scope is still slightly too large for five weeks

Twenty to twenty five products, with patents, across four schemes, plus a logger and a write up. The claims coding is the part that expands. Patents alone can be a day per vendor.

Fix: fifteen to twenty products. Patents only for the five best documented vendors, since patents mostly matter for column 2, which Maroto Molina and Stygar already cover. Four schemes is right because column 3 is where the novelty is.

---

## Part 2. The mentor's steer

**What the project is, in one sentence.** Can a welfare claim made by a dairy sensor system be verified by someone outside the vendor, and what would a system have to log and expose to make that possible?

**What success looks like on 19 October.**
1. A published claims register for 15 to 20 dairy products with coded evidence and a reliability figure.
2. A crosswalk whose new contribution is column 3 joined to the existing column 1 to 2 mapping, with the three queries answered.
3. A v0.1 auditability standard, each requirement tied to a source in law or an existing standard, with a scope note that takes no position on PLF itself.
4. A scorecard reporting how many products are assessable from public documentation and how many of those meet the standard, with the threshold fixed in advance.
5. A two page certifier annex, and a one page note to ICAR.
6. A reference logger under 300 lines mapped to the requirements.

**What to cut.** The corpus as a deliverable (it is scaffolding). The broiler transfer test (one paragraph in the write up on what it would take). "How many pass" as the headline (replace with "how many can be checked").

**What to move earlier.** Column 4. It is the novelty and it depends on nothing else. Draft it in week 1 from the Data Act, AI Act Article 12, Rutten's four levels and SOC 2 practice, then refine it after the register shows you what vendors actually disclose. The register and column 4 run in parallel, not in sequence.

**The five questions Kevin or a reviewer will ask, and your answers.**
- *What is new versus Maroto Molina and Stygar?* They mapped indicators to sensors and coded validation. I add what certification requires and what the system must log and expose to be checked, and I score products on that.
- *Why not talk to certifiers?* Your steer, and because the point is what can be verified from outside. Interviews would tell me what vendors say, not what they publish.
- *How do you know your requirements are right?* Every one is borrowed from a regime that already exists: Data Act for access, AI Act Article 12 for logging, Rutten for lineage, SOC 2 and certificate transparency practice for tamper evidence, ICAR's own application checklist for disclosure. I invented none of them; I assembled them for this setting.
- *Who uses this?* Primary: a certifier accepting sensor evidence. Secondary: ICAR, which today has validated three sensor systems and no welfare ones. Tertiary: anyone challenging an unsubstantiated welfare claim under advertising rules.
- *Why dairy?* The product list and indicator mapping already exist, so the five weeks go on the new part. The method transfers by swapping two columns.

**How to work with Kevin over five weeks.** Send something every Friday with one specific question. Batch every welfare science judgement into the questions file and never decide one yourself. When he pushes back, log it in decisions.md and change the artifact the same day. In week 3 ask him to code the 10% reliability sample; it takes him an hour and it makes the register his as well as yours.

---

## Part 3. Source pack, organised by what each source is for

### Prior work you position against (read all five in week 1)

| Source | What it did | Where it stops | What to extract |
|---|---|---|---|
| Maroto Molina et al. 2020, J Dairy Res 87(S1) 28–33 | Mapped every Welfare Quality dairy measure to PLF technologies that could monitor it | No products, no validation status, no certification, no logging | Their measure to technology table. This is column 1 to 2. |
| Stygar et al. 2021, Front Vet Sci 8:634338 (PMC8044875) | 129 commercial dairy sensors, 18 externally validated; lying, standing, rumination validated well; BCS and health detection worse; low potential for appropriate behaviour | No certification, no logging, no disclosure | Product table with validation status. Their conclusions verbatim for the write up. |
| Tuyttens, Molento, Benaissa 2022, Front Vet Sci 9:889623 (PMC9186058) | Twelve threats in four categories | A taxonomy, not a standard | The two direct threats you score, and the indirect threats for your scope note |
| Elliott and Werkheiser 2023, Animals 13(21) (PMC10648797) | What developers should disclose and to whom | No verification mechanism, no logging, no scoring | The list of what they leave unspecified. That list is your gap. |
| Berckmans 2017, Animal Frontiers 7(1), EU PLF blueprint | Key indicators and gold standards for validating PLF tools | Validation of accuracy only, pre commercial | The gold standard concept, cited as the origin of validation thinking |

Also read Rutten et al. 2013, J Dairy Sci 96(4) 1928–1952, for the four level model (technique, interpretation, integration, decision). Use their levels to define data lineage.

### Existing governance and certification (column 3 and the theory of change)

| Source | Use |
|---|---|
| ICAR validated sensor systems page and Section 11 guidelines | The nearest existing scheme. Note: three validated systems as of this month, all milk yield or composition, none welfare. Validation confirms the device meets the manufacturer's own claim for the applicant's own purpose. Their application checklist (technical manual, internal validation studies, peer reviewed publications, routine checking procedures) is a ready made disclosure list; borrow it for your disclosure dimension. |
| RSPCA Assured dairy cattle standards (in force 20 April 2026) and the RSPCA standards justification for dairy | Column 3, with the reasoning behind each requirement. The justification document makes your crosswalk defensible. |
| National Dairy FARM Animal Care Version 5 (1 July 2024 to 31 December 2027) | Column 3 with numeric thresholds: 5% or less of the lactating herd at locomotion score 3, 15% moderate lameness benchmark with improvement plan. Industry authored by NMPF, so it is your industry acceptability proxy. |
| Global Animal Partnership dairy standard (launched 2021 with HerdDogg partnership) | Column 3, and evidence that certifiers already ingest sensor data |
| Certified Humane dairy standard | Column 3 |
| ISO/TS 34700:2016 animal welfare management | The management system layer above your standard. Cite; do not extract. |

### Welfare indicators (column 1, taken from published sources, never your judgement)

| Source | Use |
|---|---|
| EFSA Scientific Opinion on the welfare of dairy cows, 2023, doi 10.2903/j.efsa.2023.7993 | Five welfare consequences (locomotory disorders including lameness, mastitis, restriction of movement, inability to perform comfort behaviours, metabolic disorders) with animal based measures for each. The spine of column 1. |
| Welfare Quality assessment protocol for dairy cows (welfarequalitynetwork.net, dairy cattle protocol PDF) | The detailed measure list under four principles and twelve criteria. |
| EFSA opinion on the welfare of calves, 2023, doi 10.2903/j.efsa.2023.7896 | Only if calf products enter the list |

### Legal templates for column 4 (what the system must log and prove)

| Source | Requirement it supports |
|---|---|
| EU Data Act, applicable from 12 September 2025 (Chapter II, user access to product data and sharing with third parties) | Access and ownership. In the EU this is now a right, not a request. Cite the Regulation and the Commission's data act page. |
| EU AI Act Article 12 (record keeping), Article 13 (transparency to deployers), Article 26(6) (log retention, six months minimum) | Logging, alert audit trail, retention, disclosure. Not binding on PLF, but the EU's definition of adequate logging. |
| Rutten et al. 2013 four levels | Data lineage: a level IV alert traceable to level I readings, the interpretation model and its version |
| SOC 2 trust services criteria; ISO/IEC 42001 | Audit evidence practice for validation evidence and change control |
| Certificate Transparency style append only logs | Tamper evidence; the design your reference logger follows |
| UK CAP Code rule 3.7 and ASA rulings on welfare claims (Red Tractor pork; ASA guidance on farming methods) | The substantiation pathway. Every claim in the register coded "no evidence cited" is a claim that would fail rule 3.7 if advertised in the UK. |

### Governance context, for the write up

- EU General Purpose AI Code of Practice, 10 July 2025: lists risk to non human welfare as a systemic risk. Voluntary, general purpose models only, does not reach farm systems.
- EFSA 2023 opinions feed the EU farm animal welfare legislative revision.

---

## Part 3b. The Sentient Futures week 3 materials, and what they give you

Kevin's cohort reads these. Using their vocabulary and citing their sources tells him you did the homework and places your project inside the debate the course sets up.

**The vocabulary to adopt.** The course names two risks: **welfare washing** (claiming welfare benefit without evidence) and **proxy drift** (optimising a measurable proxy that stops tracking the animal's actual interests). Your claims register is the instrument for detecting welfare washing. Your indicator validity dimension (does the sensor measure a validated indicator or a proxy) is the instrument for detecting proxy drift. Say both in the write up, in those words. The course also uses **precision welfare** for PLF designed around the animal's interests; your standard is what would let anyone tell precision welfare from marketing.

**The framing question the course asks** is whether PLF brings welfare transparency or fully automated exploitation. Your scope note answers it the only defensible way: the standard takes no position, it only makes claims checkable. That is also why the standard should not be read as pro PLF.

**Sources from the page that go into the project.**

| Source | Use in the project |
|---|---|
| Simoneau-Gilbert and Birch 2024, "How to reduce the ethical dangers of AI assisted farming" (Aeon) | Their four principles: no AI to justify higher stocking density, mandated public transparency for welfare data, accountability for unaddressed issues, farmer autonomy. Principles 2 and 3 are your column 4 stated as ethics. Cite them as the normative case and present your standard as the engineering of principles 2 and 3. Principle 4 supports your access and ownership dimension. |
| Aaron Boddy, "Welfare tech should be developed by welfare people" and "Animal advocates are too reluctant to sit at the industry's table" (EA Forum) | Your theory of change. The certifier annex is sitting at the table; the standard is welfare people specifying the tech. |
| Constance Li, "Unlocking new campaign targets with AI" (2025 talk) | The substantiation pathway. A register of unevidenced welfare claims is a list of campaign targets. Cite for the advocacy use of the register. |
| AI4Animals (Carlos Morales 2025 talk), slaughterhouse monitoring in 20 European sites, built by Deloitte with welfare organisations, with a metrics dashboard that has changed protocols | The one deployed system built explicitly for accountability. Two uses: add it to the product list as the welfare driven comparator (does a system built by welfare people score better on column 4?), and cite it as proof that governable PLF exists. |
| aWISH project (EU funded, sensor based welfare indicators at slaughter for broilers and pigs, real time feedback) | Second example of accountability focused PLF. Mention in the write up; not dairy, so not scored. |
| Foy and Reynolds, "Food animal welfare data collection for audits" (Livestack podcast, 2025) | History of US welfare audits from Validus onward, and how real time monitoring could replace annual checks. This is your column 3 "audited by inspection versus by sensor" question told by practitioners. Listen to it in week 1. |
| Foy and Reynolds, "Precision behaviour measurement for welfare and sustainability" (Livestack podcast, 2025) | Includes a discussion of data ownership from the industry side. Useful for the access and ownership dimension and for anticipating vendor objections. |
| van Erp-van der Kooij and Rutter 2020, "Using precision farming to improve animal welfare" | Reviews PLF as production focused with welfare co benefits, and says current systems lack the integration for comprehensive welfare assessment. Supports the finding that the market measures what is easy. |
| Coghlan and Parker 2023, harm to animals from AI (the paper Tuyttens et al. build on) | Cite alongside Tuyttens for the threat framing. |
| Marian Dawkins 2025 talk | Cautions on hype, training data quality and the lab to farm gap. Use for the validation evidence dimension: lab accuracy is not farm accuracy, which is exactly why external validation is scored separately. |
| McKay and Shah 2025, RP forecast of farmed animal numbers to 2033 | Scale framing for the write up. |
| Zachary Brown 2024, "We should campaign to restrict AI in animal agriculture" | The strongest counter position. Address it in one paragraph: a standard that makes claims checkable does not increase adoption; it removes the marketing advantage of unverified claims. |

**One product to add to the list.** AI4Animals. It is not dairy and not a farm sensor, but it is the only system on the course built for accountability, and scoring it on column 4 next to commercial dairy products tells you whether "built by welfare people" actually shows up in the logging and disclosure. Mark it as a comparator, outside the dairy count.

## Part 4. Changes to make to the plan this week

1. Rename the crosswalk's novelty: column 3 joined to the Maroto Molina and Stygar mapping, plus the industry flag.
2. Cut the product list to 15 to 20, patents for five vendors only.
3. Move column 4 drafting to week 1, run it in parallel with the register.
4. Add the reliability check: 10% re code blind plus Kevin's coding, reported as agreement.
5. Replace "how many pass" with two numbers: assessable from public documentation, and meeting the standard among those.
6. Add the scope paragraph: no position on PLF itself; only that a welfare claim made must be verifiable.
7. Add the legal column to the scorecard and the Data Act and AI Act citations to the standard.
8. Add the certifier annex (two pages) and the ICAR note (one page) as deliverables. Drop the corpus and the broiler test from the deliverables list.
9. Fix the citations: Tuyttens 2022, Elliott and Werkheiser 2023, Berckmans 2017 for the EU PLF blueprint. Remove GLOBALG.A.P.
10. Put the theory of change question to Kevin first, before species or anything else, since it decides what the standard has to satisfy.
