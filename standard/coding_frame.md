# Claims coding frame

Version 0.1, drafted 16 September 2026 before any claim was coded. Every change is recorded in the change log at the end and in `notes/decisions.md`.

## Purpose

This frame fixes how every welfare claim in `data/claims.csv` is recorded, so that a second coder working from the same public sources would produce the same rows. It is the instrument for the claims register, which is item #9 on Kevin's list, and it feeds column 2 of the crosswalk and the scorecard. In the course vocabulary it is how welfare washing becomes visible: a welfare claim with nothing behind it shows up as a row with `evidence_cited` set to none.

The frame records what vendors say and what they cite. It does not judge whether a claim is true, and it never decides a welfare science question. Where a mapping to an indicator is not clean, the coder says so and the question goes to Kevin.

## Unit of analysis

One claim is one assertion about animal welfare, about health presented as a welfare proxy, or about compliance with a welfare scheme or rule, attributable to one product and found in one public source. A sentence that makes two separate assertions is two claims. A statement about production alone, such as milk yield, feed efficiency or labour saved, is not coded unless the vendor presents it as a welfare or health benefit. Oestrus and calving detection are coded only when the source frames them in welfare or health terms.

## Identifiers

Products are numbered `P001`, `P002` and so on in `data/products.csv`. Claims are numbered `C0001`, `C0002` and so on in the order they are coded, and a number is never reused, even when a row is deleted. Indicators are numbered in `data/indicators.csv`.

## Fields

| Field | Allowed values | Definition |
|---|---|---|
| claim_id | `C0001` onwards | Sequential identifier, assigned in coding order, never reused. |
| product_id | an id in `data/products.csv` | The product the claim is about. |
| claim_text | verbatim quote | The exact words from the source, with no paraphrase. A claim in another language is quoted in that language and translated in notes. |
| source_url | URL | The public page or document where the claim was found. For a PDF, the page number goes in notes. |
| source_type | marketing_page, product_manual, developer_doc, patent, peer_reviewed, press_release, recorded_talk | The kind of document the claim came from. |
| date_captured | ISO date, `YYYY-MM-DD` | The day the source was read and saved to `corpus/vendors/`. |
| claim_type | indicator_claim, outcome_claim, accuracy_claim, compliance_claim, no_public_documentation | indicator_claim: the product detects or measures a named condition or behaviour. outcome_claim: using the product improves welfare or health. accuracy_claim: a performance figure such as sensitivity, specificity or agreement with a reference. compliance_claim: the product meets or supports a named scheme, standard or law. no_public_documentation: a placeholder recording that documentation could not be found or was not public (rule 3). |
| mapped_indicator_id | an id in `data/indicators.csv`, or empty | The EFSA or Welfare Quality measure the claim maps to. Empty when mapping_confidence is none or unsure. |
| mapping_confidence | direct, proxy, none, unsure | direct: the signal the product claims to report is the measure as EFSA or Welfare Quality define it. proxy: the product reports a different signal from which it says it infers the measure, and that route is described in Maroto Molina 2020 or the protocol itself. none: the claim names no indicator. unsure: any other case (rule 6). |
| evidence_cited | none, vendor_internal, independent_external, peer_reviewed | What the source cites in support of this claim. none: nothing is cited. vendor_internal: the vendor's own trial, white paper or figure, or a study by vendor staff on a vendor population. independent_external: a validation by a party independent of the vendor on a population other than the training population, not peer reviewed, for example an ICAR report. peer_reviewed: a peer reviewed study that is independent of the vendor or uses an independent population. |
| evidence_ref | citation or URL, or empty | The reference as the source gives it. Empty when evidence_cited is none. |
| legal_flag | none, cap_3_7_unsubstantiated | cap_3_7_unsubstantiated when a welfare claim has evidence_cited set to none. It marks a claim that would lack documentary evidence under UK CAP Code rule 3.7 if advertised in the UK. It is a flag, not a legal finding. Rows of type no_public_documentation are always none. |
| notes | free text | Other URLs where the claim repeats, page numbers, translations, candidate indicators for unsure rows, sibling claim_ids, and anything a second coder would need. |

## Rules

**Rule 1. Repeated claims.** A claim that appears on several pages is coded once, with the URL of the first source where it was found, and the other URLs are listed in notes. It counts as a repeat only when it makes the same assertion about the same indicator with the same evidence. If a later page adds a figure or a citation, that later statement is a new claim.

**Rule 2. Welfare with no indicator.** A statement such as "improves welfare" or "a healthier, happier herd" that names no measure is coded as outcome_claim, with mapped_indicator_id empty and mapping_confidence none.

**Rule 3. Pages behind a login, and vendors that publish nothing.** No page behind a login, registration wall or customer portal is ever opened. When documentation for a product sits only behind one, the product gets a single row with claim_type no_public_documentation. The claim_text describes what is gated, for example "Product manual available only after customer login", the source_url is the page where the gate appears, and notes says "not publicly accessible". A vendor that publishes no technical documentation at all for a product gets the same kind of row, so that the absence shows in the register.

**Rule 4. Accuracy figures without a population.** An accuracy figure that does not say what animals, farms or conditions it was measured on is coded evidence_cited vendor_internal, and notes records that no population was stated.

**Rule 5. Studies by vendor staff.** A peer reviewed paper with an author employed by the vendor is coded vendor_internal, unless the paper states that the validation used a population independent of the one the system was developed on. If the paper does not say, it stays vendor_internal.

**Rule 6. Unsure.** mapping_confidence unsure is always allowed and never a failure. Every unsure row is appended to `notes/kevin_questions.md` on the day it is coded, with its claim_id, the claim text and the candidate indicators, and the candidates also go in notes. An unsure row is changed only after Kevin's answer has been entered in `notes/decisions.md`.

**Rule 7. One sentence, several indicators.** A sentence that names several indicators, such as "detects lameness, mastitis and reduced rumination", is split into one row per indicator. Each row carries the full sentence as claim_text, and notes lists the sibling claim_ids.

**Rule 8. An indicator with a figure.** A statement that names an indicator and gives an accuracy figure for it is one accuracy_claim with the indicator mapped. It is not also coded as an indicator_claim.

**Rule 9. Keep a copy.** Every source is saved to `corpus/vendors/<vendor>/` on the day it is captured, named `<product_id>_<YYYY-MM-DD>_<short_name>`, so the claim can be checked again after the vendor changes the page.

## Pilot procedure

Before coding the full list, code every welfare claim for four products: one from Lely, one from DeLaval, one from smaXtec and one camera based product. While coding, write down every place where a field was ambiguous, a value was missing or a rule was needed that this frame does not have. Two questions are already expected: how to handle a claim on a company wide page that names no product, and whether a translated claim should be coded from the original language or the English page when both exist. After the pilot, revise the frame, record each change with its date and reason in `notes/decisions.md` and in the change log below, re code the pilot products where the change affects them, and only then code the rest.

## Reliability procedure

After all claims are coded, draw a random 10% of claim_ids, rounded up, using a fixed seed that is written into `notes/decisions.md` before the draw. At least seven days after the original coding, re code those rows blind, seeing only the claim_text and source_url and not the original codes. The fields re coded are claim_type, mapped_indicator_id, mapping_confidence and evidence_cited. A second coder, Kevin or someone he names, codes the same rows the same way. Each result is a row in `data/reliability.csv`, one row per claim and field, and `scripts/stats.py` fills the agreement columns and prints percentage agreement per field. If agreement on any field is below 80%, tighten the rule for that field, log the change, and re code the affected rows. Both agreement figures are reported in the method section of the write up.

## Change log

| Date | Version | Change | Reason |
|---|---|---|---|
| 2026-09-16 | 0.1 | Frame drafted from the repository spec and the week 1 plan | Written before any coding |
