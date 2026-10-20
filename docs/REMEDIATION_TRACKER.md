# WRH Remediation Tracker — Release Gates

**Governing record:** [PUBLIC_RELEASE_STATUS.md](../PUBLIC_RELEASE_STATUS.md), effective September 4, 2026. This tracker reflects the Phase 1 review branch, not the unchanged default branch.

> **THIS TRACKER DOES NOT PASS ANY GATE.** Delivery remains withheld until all six published release gates are satisfied and a version-specific release decision is documented. A draft PR, source inventory, claim list, or new warning does not constitute clinical approval, legal clearance, or delivery authorization.

**Phase 2 audit update (2026-10-20 UTC):** All 15 starter entries have bounded AI-assisted source assessments, with original research errors corrected and unresolved assertions retained. [PHASE2_SOURCE_AUDIT.md](PHASE2_SOURCE_AUDIT.md) records source links, inspection depth, and limitations. [PROPOSED_CONTENT_CORRECTIONS_PHASE2.md](PROPOSED_CONTENT_CORRECTIONS_PHASE2.md) and [INDEPENDENT_REVIEW_BRIEF.md](INDEPENDENT_REVIEW_BRIEF.md) are unapproved review inputs. No script or crisis procedure is changed. **No independent-review decision is recorded and no release gate is passed.**

The six gate texts below are quoted verbatim. Interpretation and remaining work are planning proposals, not additional agency requirements or evidence that a gate has passed. No independent reviewer or reviewer decision is recorded in Phase 1. Claims about absent records are limited to this repository; external records have not been ruled out. Review expertise is required across the named domains; the gate does not prescribe four separate people.

## Gate 1 — Evidence

**Gate text (verbatim):** "Claim-level evidence register with source and reviewer documentation."

**Present:** [EVIDENCE_BASE.md](EVIDENCE_BASE.md) supplies the seven-field schema. [EVIDENCE_REGISTER.md](EVIDENCE_REGISTER.md) contains 15 starter entries with exact source passages, baseline locators, unverified evidence status, and pending independent-review fields. The starter is part of this branch; it is not an untracked working-tree file. **Phase 2:** The corrected register has 15 assessments (8 narrower-support, 3 theoretical-framing, 4 unresolved exact assertions). No exact wording is established as supported by this bounded recheck, and no independent reviewer has approved a claim. Source assessments, proposals, and the handoff brief remain draft review material.

**Remaining:** Extend coverage to every material claim; qualified independent reviewers must disposition the Phase 2 assessments and proposed corrections (see [INDEPENDENT_REVIEW_BRIEF.md](INDEPENDENT_REVIEW_BRIEF.md) §6 questions) and document their decisions; identify revisions implementing those decisions. Unsupported claims must remain explicitly unsupported until reviewed, revised, or retired. General research does not validate WRH. AI-assisted research does not satisfy this gate.

**Status:** `IN PROGRESS`.

**Decision/review needed:** Appoint relevant independent subject-matter reviewers; prioritize Session 20 and the crisis materials. Session 20 entries WRH-ER-001 through WRH-ER-004 are blocking review items.

## Gate 2 — Independent review

**Gate text (verbatim):** "Independent clinical, legal/privacy, accessibility, and site-implementation review."

**Present:** No completed independent review records were identified in this repository. [LICENSING_ISSUES.md](LICENSING_ISSUES.md) records questions, not counsel's findings. Generic accessibility or implementation documents are not independent testing/review records.

**Remaining:** Obtain and document reviews in every named domain, their scope, reviewer qualifications, findings, required edits, and disposition. Clinical review must address crisis framing and instructions; legal/privacy review must address distribution/licensing, authority claims, and data practices. Accessibility and site-implementation review require documented assessment of the intended materials and setting.

**Status:** `NOT STARTED`.

**Decision/review needed:** Owner selects reviewers and supplies any relevant external records. Do not publish confidential records without appropriate privacy review.

## Gate 3 — Site procedures

**Gate text (verbatim):** "Site-specific safety, escalation, confidentiality, records, and referral procedures."

**Present:** Generic source exists in `docs/SAFETY_AND_ESCALATION.md`, Part IV crisis/reporting files, and toolkit/participant resources. Session 20, Session 76, and the Crisis Package carry withdrawal notices. The safety-language template and Session 76 worksheet carry visible template warnings; their placeholders remain unfilled.

**Remaining:** Identify intended delivery sites and qualified leads; develop and review site-specific escalation, confidentiality, records, referral, and adverse-event procedures with real personnel and pathways. Audit other templates for missing fields. Withdrawn generic source cannot serve as an approved site plan.

**Status:** `IN PROGRESS`.

**Decision/review needed:** Owner and site leads define settings; independent clinical/privacy/site reviewers assess the resulting procedures. No site plan is approved here.

## Gate 4 — Facilitator controls

**Gate text (verbatim):** "Defined facilitator authorization, training, supervision, and fidelity controls."

**Present:** Part IV contains draft certification, prerequisites, and toolkit source. The certification pathway is labeled an unapproved draft; the IP document's compliance/agency assertions are flagged unverified, with no supporting records found in this repository. The labels preserve source text and do not establish the asserted authority.

**Remaining:** Supply supporting records or revise unsupported assertions; define and review actual authorization, training, supervision, and fidelity standards. Merely labeling an assertion draft does not establish operational controls.

**Status:** `PENDING OWNER DECISION`.

**Decision/review needed:** Owner resolves supporting records and intended governance; appropriate independent reviewers assess proposed standards.

## Gate 5 — Audience separation

**Gate text (verbatim):** "Audience-separated participant, facilitator, internal, and revision documents."

**Present:** [CURRICULUM_MAP.md](../CURRICULUM_MAP.md) inventories audiences without declaring canonical authority. [CONTENT_CONCORDANCE.md](../new-system/CONTENT_CONCORDANCE.md) records proposed topic pairings; source filenames remain unchanged. READMEs distinguish the two participant sequences, and the dead presentation link is neutralized. Warning labels identify selected unfilled templates.

**Remaining:** Owner decides authoritative collections and numbering; confirm content fidelity across participant/facilitator materials; define how audience-specific packages are assembled and restricted. Workbook/guide titles match the eight-topic four-track sequence, not the differently ordered sixteen-lesson sequence; formal association remains an owner decision. Decide the portal's audience and fate. The bodily-signaling session lacks a handout.

**Status:** `IN PROGRESS`.

**Decision/review needed:** Owner establishes intended relationships; independent reviewers assess audience separation and suitability. A directory map is not a released audience package.

## Gate 6 — Versioned release decision

**Gate text (verbatim):** "Version manifest and documented release decision."

**Present:** The current release status withholds delivery. No delivery version manifest or affirmative release decision was identified. Phase 1 corrects selected labels to 76 numbered sessions plus one portal; that is a documentation repair, not a release manifest.

**Remaining:** Agree a manifest format and release inventory. A file/version/hash inventory is a proposed approach, not a format mandated by the gate text. After Gates 1–5 are satisfied, record a dated decision tied to the exact reviewed version and its evidence, naming the responsible decision-maker. Withhold release if requirements remain unmet.

**Status:** `NOT STARTED`.

**Decision/review needed:** Owner approves the manifest approach and eventually documents a version-specific release decision. Phase 1 authorizes none.

## Status summary

| Gate | Status | Satisfied? |
|---|---|---|
| 1. Evidence register | `IN PROGRESS` | No |
| 2. Independent reviews | `NOT STARTED` | No |
| 3. Site procedures | `IN PROGRESS` | No |
| 4. Facilitator controls | `PENDING OWNER DECISION` | No |
| 5. Audience separation | `IN PROGRESS` | No |
| 6. Version manifest and release decision | `NOT STARTED` | No |

**Catalog regeneration control:** The inherited catalog builder previously serialized master-session source despite the empty checked-in catalog. The Phase 1 follow-up changes ordinary catalog builds to emit only the withdrawn stub; two regression tests cover clean builds and replacement of a populated catalog. The checked-in catalog and explorer remain unchanged. This closes a regeneration path, not a release gate.

**Gates satisfied: 0 of 6. Delivery remains withheld.** Update this tracker against the actual branch state and cite supporting records when statuses change. Document repairs must not be reported as still pending after they are implemented, nor as satisfaction of the broader gate.
