# Resources to share with Claude Code
Checklist. Everything Claude Code needs is a file in the repo. Items marked "you" are for you to read, watch or listen to yourself; they do not go in the repo.

## A. Before session 0 (repository creation)

Copy these into `plf-audit/docs/` from `C:\Epoch Ai project`:

| File | Purpose |
|---|---|
| `PLF_Repo_Spec_For_ClaudeCode.md` | The build instructions. Paste its contents as the first message, or tell Claude Code to read it. |
| `PLF_Project_Resources.md` | Critical review, mentor's steer, source pack, SF week 3 materials, plan changes. Claude Code reads Part 1 and Part 4 first. |
| `PLF_5_Week_Plan.md` | Week by week tasks and definitions of done. |
| `PLF_Audit_Standard_Plan.docx` (or `.md`) | The plan as shared with Kevin: four columns, rubric, questions. |
| `Project2_Briefing_For_Kevin_Call.md` | Optional private context. |

Nothing else is needed for session 0.

## B. Before session 1 (week 1 work)

Download these into `plf-audit/corpus/` with the exact filenames. They are ignored by git; `corpus/README.md` records the source URLs.

### Prior work to position against

| Filename | Source |
|---|---|
| `maroto_molina_2020.pdf` | Journal of Dairy Research 87(S1) 28–33. Cambridge Core, or the open copy at helvia.uco.es (handle 10396/27738). |
| `stygar_2021.pdf` and `stygar_2021_supplementary.pdf` | PMC8044875 (Frontiers in Veterinary Science 8:634338). Get the supplementary product table too. |
| `gomez_2021.pdf` | Frontiers in Veterinary Science 8:660565. |
| `tuyttens_2022.pdf` | PMC9186058 (Frontiers in Veterinary Science 9:889623). |
| `elliott_werkheiser_2023.pdf` | PMC10648797 (Animals 13(21)). |
| `berckmans_2017_euplf_blueprint.pdf` | Animal Frontiers 7(1), doi 10.2527/af.2017.0103. |
| `rutten_2013.pdf` | Journal of Dairy Science 96(4) 1928–1952; open copy at dspace.library.uu.nl. |
| `van_erp_rutter_2020.pdf` | "Using precision farming to improve animal welfare," ResearchGate 347116954. |
| `coghlan_parker_2023.pdf` | "Harm to nonhuman animals from AI," the paper Tuyttens builds on. |

### Welfare indicators (column 1)

| Filename | Source |
|---|---|
| `efsa_2023_dairy_cows.pdf` | doi 10.2903/j.efsa.2023.7993. The Spanish ministry hosts a direct PDF (mapa.gob.es) if the Wiley page is awkward. |
| `welfare_quality_dairy.pdf` | welfarequalitynetwork.net/media/1319/dairy-cattle-protocol.pdf |
| `efsa_2023_calves.pdf` | doi 10.2903/j.efsa.2023.7896. Only if calf products enter the list. |

### Certification and existing governance (column 3 and theory of change)

| Filename | Source |
|---|---|
| `icar_validated_sensors.html` | Save the page icar.org/icar-validated-sensor-systems/ as HTML. Note the three validated systems and the application checklist. |
| `icar_section11.pdf` | icar.org/Guidelines/11-Milk-Recording-Devices.pdf |
| `icar_panazoo_report.pdf`, `icar_brolis_report.pdf`, `icar_ekomilk_report.pdf` | The three validation reports linked from the ICAR page. They show what an ICAR test actually checks. |
| `rspca_dairy_standards_2026.pdf` | rspcaassured.org.uk/industry/standards, dairy cattle, April 2026 version. |
| `rspca_dairy_justification_2026.pdf` | science.rspca.org.uk/documents/d/science/dairy-sjd-2026 |
| `farm_animal_care_v5.pdf` | nationaldairyfarm.com, Animal Care Version 5 manual. |
| `gap_dairy_standard.pdf` | globalanimalpartnership.org/standards/dairy-cattle/ |
| `certified_humane_dairy.pdf` | certifiedhumane.org, dairy cattle standards. |
| `iso_ts_34700_summary.md` | You cannot download the ISO text legally for free. Paste the scope and structure from the ISO online browsing platform (iso.org/obp) into a markdown file. |

### Legal templates (column 4)

| Filename | Source |
|---|---|
| `eu_ai_act_art12_13_26.md` | Paste the text of Articles 12, 13 and 26 from artificialintelligenceact.eu into one markdown file with headings. |
| `eu_data_act_chapter2.md` | Paste Chapter II (Articles 3 to 7) of Regulation (EU) 2023/2854 from EUR-Lex, plus one paragraph noting it applies from 12 September 2025. |
| `cap_code_rule_3_7.md` | Paste CAP Code rule 3.7 (substantiation) and the ASA advice page on farming methods (asa.org.uk/advice-online/farming-methods.html). |
| `simoneau_gilbert_birch_2024.md` | Save the Aeon essay text. It is the normative source for column 4. |

### Sentient Futures week 3 written materials

| Filename | Source |
|---|---|
| `boddy_welfare_tech.md` | EA Forum post "Welfare tech should be developed by welfare people." |
| `boddy_industry_table.md` | EA Forum post "Animal advocates are too reluctant to sit at the industry's table." |
| `brown_2024_restrict_ai.md` | beforeporcelain.substack.com, "We should campaign to restrict AI in animal agriculture." The counter position. |
| `taylor_2024_ai_factory_farming.md` | Sentient Futures substack, parts I and II. |
| `mckay_shah_2025_forecast.md` | RP 2033 farmed animal forecast, summary section. |

## C. Vendor documentation (gathered during week 1 and 2, not before)

Claude Code will save these itself as it builds the product list, into `corpus/vendors/<vendor>/`. You do not need to pre download them. Expected vendors: Lely, DeLaval, Nedap, Allflex (MSD Animal Health), CowManager, smaXtec, Afimilk, Moocall, Connecterra, Cainthus (Ever.Ag), Boumatic, GEA, plus AI4Animals as the comparator. Patents only for the five best documented vendors.

## D. For you, not for the repo

Watch or listen in week 1, then write two paragraphs of notes into `notes/course_notes.md` so Claude Code can use them:

| Item | Why |
|---|---|
| Foy and Reynolds, "Food animal welfare data collection for audits" (Livestack podcast episode 25, 53 min) | The history of US welfare audits and where sensors are replacing inspection. Directly informs the audit_method column in the crosswalk. |
| Foy and Reynolds, "Precision behaviour measurement for welfare and sustainability" (Livestack episode 26, 45 min) | Industry view on data ownership. Anticipates vendor objections to the access dimension. |
| Carlos Morales, "Slaughterhouse monitoring with AI4Animals" (38 min) | The comparator product. Note what it logs, who sees the dashboard, and what changed as a result. |
| Constance Li, "Unlocking new campaign targets with AI" (24 min) | The advocacy use of the claims register. |
| Marian Dawkins, "AI in farming: helping or harming animal welfare" (35 min) | Lab to farm gap; why external validation is scored separately. |
| The AI in Farming panel (Veit, Sheldon, Simoneau-Gilbert, 31 min) | The debate your scope note sits inside. |

## E. Not needed

Market reports (MarketsandMarkets, Grand View). Blockchain traceability papers. GLOBALG.A.P. documents. Anything requiring vendor contact.

## Order of operations

1. Copy section A files into `docs/`. Run session 0 with the repo spec. Review the scaffold.
2. Download section B files into `corpus/`. This is an hour or two of clicking; do it in one sitting.
3. Watch section D items over week 1 evenings and write `notes/course_notes.md`.
4. Start session 1 with: "Read CLAUDE.md, notes/decisions.md, docs/PLF_Project_Resources.md Part 1 and Part 4, and week 1 of docs/PLF_5_Week_Plan.md. List which corpus files you can see and which are missing. Then tell me what done looks like today."
