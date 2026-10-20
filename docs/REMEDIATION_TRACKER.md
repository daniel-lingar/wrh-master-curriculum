# WRH Remediation Tracker — Release Gates

**Repository:** https://github.com/daniel-lingar/wrh-master-curriculum
**Branch:** `review/wrh-remediation-phase1` · **Created:** 2026-10-19 (Phase 1 Repository Remediation)
**Governing document:** `PUBLIC_RELEASE_STATUS.md` (effective 2026-09-04), which places the curriculum in a controlled-release / withdrawn state.

---

> **THIS TRACKER DOES NOT PASS ANY GATE.**
>
> Creating this tracker is a bookkeeping step only. It satisfies none of the six published release gates below. **Delivery of WRH remains withheld until all six published release gates are satisfied and a version-specific release decision is documented.** No gate may be marked complete on the basis of this tracker, of remediation plans, or of work in progress — only on the basis of evidence actually present in the repository.

## How this tracker works

- Each gate is quoted verbatim from `PUBLIC_RELEASE_STATUS.md`. Where a gate's wording required interpretation, the interpretation is stated under "Interpretation applied" and flagged as such.
- **Statuses allowed:** `NOT STARTED` / `IN PROGRESS` / `BLOCKED` / `PENDING OWNER DECISION` / `PENDING INDEPENDENT REVIEW`. Nothing is marked complete unless the evidence is in the repo.
- Reviewer names, credentials, and decisions are **never invented**. Where a reviewer is required but not yet appointed, this is stated as `TBD`.
- Blocking findings from the October 2026 sampled assessment are cross-referenced. The assessment was sampled (Session 01 read in full plus selected sessions/passages), so remediation work must extend beyond what it inspected.

---

## Gate 1 — Claim-level evidence register with source and reviewer documentation

**Gate text (verbatim):** "Claim-level evidence register with source and reviewer documentation."

**Interpretation applied:** The register must follow the 7-field schema already specified in `docs/EVIDENCE_BASE.md`: (1) exact claim + module/session where it appears; (2) supporting primary or authoritative source, publication date, link or identifier; (3) applicable population and setting; (4) strengths, limitations, and uncertainty; (5) claim type (educational, clinical, legal, operational, marketing); (6) reviewer name, relevant qualification, review date, decision, required edits; (7) the revision version that implemented the decision. A claim with a source but no documented reviewer decision, or a reviewer decision with no cited source, does **not** satisfy this gate. Claims with no support must be recorded honestly as unsupported — "grading up" unsupported claims (e.g., calling them evidence-informed without review) does not satisfy the gate.

**What is actually present in the repo:**
- `docs/EVIDENCE_BASE.md` — self-described "release-control placeholder, not an evidence register." The 7-field schema exists; the register itself does not.
- `docs/EVIDENCE_REGISTER.md` — **Phase 1 starter register** (working tree only, untracked, not committed, created 2026-10-19 by a Phase 1 worker). Follows the 7-field schema; starts with the Session 20 high-risk claims flagged BLOCKING. It explicitly states it is **not** a completed, independently reviewed evidence record, that no claim is validated, and that all independent reviewer fields are PENDING. This is a genuine start on the register, not a satisfied gate.

**Remaining work:**
- Complete the register for all material claims (currently a starter, not comprehensive).
- Fill the independent reviewer fields: reviewer name, relevant qualification, review date, decision, required edits — for every entry. No reviewer names, credentials, or decisions may be invented.
- Record the revision version that implements each reviewer decision.

**Status:** `IN PROGRESS` (starter register exists in the working tree; independent reviewer documentation and comprehensive claim coverage do not)

**Reviewer / owner decision required:** Independent reviewer(s) with relevant subject-matter qualifications (TBD) must document per-claim review decisions. Owner must decide whether to produce supporting records for the authority claims or have them relabeled as draft/aspirational in the source documents before review.

---

## Gate 2 — Independent clinical, legal/privacy, accessibility, and site-implementation review

**Gate text (verbatim):** "Independent clinical, legal/privacy, accessibility, and site-implementation review."

**Interpretation applied:** Four distinct independent reviews are required: clinical, legal/privacy, accessibility, and site-implementation. "Independent" means reviewer(s) who are not the curriculum author/owner, with documented relevant qualifications. Each review's scope, qualifications, findings, and required edits must be recorded in the repo — a review that happened but is undocumented does not satisfy the gate. I interpret the legal/privacy review's scope as necessarily including the license conflict described below, since it is a legal question affecting distribution posture.

**What is actually present in the repo:**
- No independent review records of any kind exist in the repo — no clinical review, no legal/privacy review, no accessibility testing, no site-implementation review.
- `docs/ACCESSIBILITY.md` exists but contains no testing records.
- The license conflict is unresolved: root `LICENSE` is Creative Commons Attribution-NonCommercial 4.0, while every session file footer and `Part-IV/IP_and_Usage_Rights.md` declare the curriculum "exclusive and proprietary intellectual property of Capitol Contracts LLC" with "All rights… expressly reserved." Both postures stand unreconciled. `docs/LICENSING_ISSUES.md` (working tree only, untracked, not committed, created 2026-10-19 by a Phase 1 worker) documents the conflict factually — it changes nothing, contains no legal conclusions, and is explicitly a record for qualified legal review, not legal review itself.

**Remaining work:**
- Commission independent clinical review — Session 20 is a blocking content-safety item (see Gate 1) and must not be delivered or piloted until reviewed.
- Commission legal review covering: the CC BY-NC 4.0 vs. All-Rights-Reserved conflict; the forward licensing intent; the distribution history of CC-licensed versions and which permissions survive for prior recipients (CC licenses are irrevocable for recipients who received the material while the CC license was valid and remain compliant); and consistent labeling across the root `LICENSE`, session footers, and `IP_and_Usage_Rights.md`.
- Commission independent accessibility review with documented testing (not a self-assessment).
- Commission site-implementation review of deployment readiness.
- Record reviewer identity, qualifications, review date, findings, required edits, and disposition in the repo.

**Status:** `NOT STARTED`

**Reviewer / owner decision required:** Four independent reviewers (clinical, legal, accessibility, site-implementation — all TBD) must be appointed and their documented reviews filed. Owner must select reviewers and, for the legal review, supply the full distribution history of CC-licensed versions. No reviewer names, credentials, or decisions are recorded here because none exist.

---

## Gate 3 — Site-specific safety, escalation, confidentiality, records, and referral procedures

**Gate text (verbatim):** "Site-specific safety, escalation, confidentiality, records, and referral procedures."

**Interpretation applied:** "Site-specific" is the operative word. Generic procedures, templates, and safety frameworks are necessary prerequisites but do not satisfy this gate on their own — the gate requires procedures naming an actual delivery site's personnel, contact points, referral pathways, confidentiality rules, and records practices. Template documents with unfilled fields (e.g., `[insert from App B]`, `[Insert name of clinical lead]`) cannot satisfy this gate as-is and must carry a visible "TEMPLATE — DO NOT DELIVER UNFILLED" marker.

**What is actually present in the repo:**
- `docs/SAFETY_AND_ESCALATION.md` — generic safety/escalation document.
- `Part-IV/Crisis_Package.md`, `Part-IV/Protocols_and_Reporting.md`, `Part-IV/Adverse_Event_Reporting.md`, `Part-IV/adverse_events_template.csv` — operational layer.
- `Part-IV/Session_76_Behavioral_Health_Crisis_Response_Safety_Protocols_and_Escalation_Management_Framework.md` — crisis-protocol session; its safety-plan worksheet contains an unfilled `[insert from App B]` field for the local VA emergency number.
- `Part-IV/Safety_Language_Template.md` — contains unfilled `[Insert name of clinical lead]` and `[Insert Session Tool]` fields.
- `Part-IV/Facilitator-Toolkit/` (core rules, decompression protocol, readiness checklist) and `Part-IV/Participant-Materials/` (Plan B wallet card, handout, safety rules) — generic materials.
- **Blocking dependency:** Session 20's framing of suicidal ideation as a necessary healing milestone is a content-safety item that must be resolved by independent clinical review (Gate 2) before any safety-procedure package can be treated as delivery-ready.

**Remaining work:**
- Resolve Session 20 through independent clinical review; revise or retire per reviewer decision.
- Mark all unfilled safety-adjacent templates visibly as TEMPLATE — DO NOT DELIVER UNFILLED.
- Produce site-specific safety, escalation, confidentiality, records, and referral procedures for each actual delivery site, with named personnel and real contact/referral pathways.
- Document adverse-event and confidentiality/record-retention procedures per site.

**Status:** `IN PROGRESS` (generic materials exist; no site-specific procedures exist; unfilled template fields unresolved)

**Reviewer / owner decision required:** Independent clinical reviewer (TBD) on Session 20 and the crisis materials. Owner must identify the delivery site(s), appoint site clinical/safety leads, and approve site-specific procedures. No such site or lead is named anywhere in the repo.

---

## Gate 4 — Defined facilitator authorization, training, supervision, and fidelity controls

**Gate text (verbatim):** "Defined facilitator authorization, training, supervision, and fidelity controls."

**Interpretation applied:** The gate requires documented answers to four questions: who is authorized to facilitate (authorization), what training is required (training), what ongoing oversight applies (supervision), and how delivery fidelity is monitored and enforced (fidelity controls). Documents that assert certification authority, board oversight, or federal-agency alignment must be supported by records (board charter, agency correspondence, approvals) or explicitly relabeled as draft/aspirational — unsupported authority claims cannot count as authorization controls.

**What is actually present in the repo:**
- `Part-IV/Certification_Path.md` — describes a "Capitol Contracts LLC Certification Board" and claims the pathway "meet[s] the rigorous requirements of federal agencies, including VA, DoD, DOL, SAMHSA"; offers "WRH Certified Provider" status. No board charter, agency correspondence, or approval records exist in the repo.
- `Part-IV/Facilitator_Prerequisites.md` — prerequisite definitions exist.
- `Part-IV/IP_and_Usage_Rights.md` — claims alignment with VA/DoD clinical practice guidelines and Joint Commission standards; states unauthorized deviation "will immediately void the compliance certification of the delivery" — invoking a certification no repo record shows was granted.
- `Part-IV/Facilitator-Toolkit/` (core rules, decompression protocol, readiness checklist, diagrams) and `Part-IV/Staff-Tools/` (pre/post belief-shift survey) — operational supports, but none defines authorization, supervision, or fidelity controls.

**Remaining work:**
- Owner decision: produce supporting records for the certification-board and federal-alignment claims, or relabel `Certification_Path.md` and the affected sections of `IP_and_Usage_Rights.md` explicitly as draft/aspirational and qualify or remove the federal-alignment claims.
- Define authorization tiers, training requirements, supervision structure, and fidelity-monitoring controls as documented, reviewable standards.
- Have the defined standards independently reviewed (clinical + site-implementation reviewers, TBD).

**Status:** `PENDING OWNER DECISION` (the existing documents cannot serve as authorization controls until their unsupported authority claims are either evidenced or relabeled; that decision belongs to the owner alone)

**Reviewer / owner decision required:** Owner must decide whether the certification/federal-alignment claims are evidenced or draft — no one else can make that call. Independent clinical and site-implementation reviewers (TBD) must then review the resulting standards.

---

## Gate 5 — Audience-separated participant, facilitator, internal, and revision documents

**Gate text (verbatim):** "Audience-separated participant, facilitator, internal, and revision documents."

**Interpretation applied:** Four audience classes are named: participant, facilitator, internal (ops/buyer/compliance), and revision (change-control records — versioned deltas and decision records, not draft content). The gate requires that materials be separated by audience in practice (a participant must not receive facilitator scripts or internal commercial/ops content, and vice versa) and that this separation be documented in an audience map. Structural separation in the folder tree is a start, not the deliverable.

**What is actually present in the repo:**
- The folder tree is architecturally audience-aware: facilitator scripts (`Part-I/`–`Part-IV/`, `new-system/sessions/`), participant lessons (`docs/core-curriculum/lesson-01..16`, `docs/core-curriculum/Lesson_01..08`), participant handouts (`new-system/handouts/`), participant workbooks (`docs/participant-workbooks/`), internal/ops docs (`docs/executive/` brand/buyer/federal/sales systems, `Part-IV` pricing/IP), release-control docs (`docs/`).
- `CURRICULUM_MAP.md` (repo root, created 2026-10-19 in Phase 1 remediation) inventories the six curriculum lines and records unresolved canonical-authority questions — it is a map, not an audience-separation plan.
- **Gaps:** no document defines which lines are canonical for delivery; `docs/core-curriculum/README.md` documents only the 16 lowercase lessons and never mentions the four-track set in the same folder; the new-system lane's numbering diverges from master sessions and its handouts misalign with its sessions by topic; `Part-I/Session_12_Pilot_Portal.md` mixes a participant-facing worksheet with facilitator compliance anchors and links a nonexistent presentation deck; unfilled safety templates sit alongside finished content without TEMPLATE markers.

**Remaining work:**
- Document the audience map: which lines serve which audience, which are canonical vs. legacy vs. draft, and how materials move between audiences (or are restricted).
- Resolve the handout/session misalignments (see Gate notes / CURRICULUM_MAP.md) so participant-facing materials pair correctly with facilitator sessions.
- Fix or remove the dead presentation-deck link in `Session_12_Pilot_Portal.md`; decide that page's audience.
- Add visible TEMPLATE — DO NOT DELIVER UNFILLED headers to unfilled safety-adjacent documents.

**Status:** `IN PROGRESS` (structure exists; documented audience map and canonical-authority decisions do not)

**Reviewer / owner decision required:** Owner decisions on canonical lanes (facilitator: master v5.0 vs. new-system rewrite; participant: 16-lesson core vs. four-track vs. workbook layer) and on the numbering/handout alignment fix. These are owner calls; this tracker and the curriculum map record them as unresolved, not decided.

---

## Gate 6 — Version manifest and documented release decision

**Gate text (verbatim):** "Version manifest and documented release decision."

**Interpretation applied:** Two deliverables. (1) A version manifest: a machine- and human-readable inventory of every file in the release, with a version label and a content hash per file, so the released artifact is uniquely identifiable and auditable. The gate text does not specify a hash algorithm or format; I note that interpretation here rather than imposing one. (2) A documented release decision: a written, dated decision record tying a specific manifest version to the satisfaction of Gates 1–5, naming who decided and what was reviewed. A release decision that is not tied to a specific manifest version does not satisfy this gate.

**What is actually present in the repo:**
- No version manifest exists.
- No release decision of any kind is documented. The current documented state is delivery-withheld (`PUBLIC_RELEASE_STATUS.md`: "Delivery authorization: None").
- Count inconsistency blocks a clean manifest: `_config.yml` describes a "77-session" curriculum while `Part-IV/IP_and_Usage_Rights.md` and session footers say 76 sessions. The verified file count is **76 numbered sessions + 1 portal page** (`Part-I/Session_12_Pilot_Portal.md`) = 77 session files. The labeling must be made consistent (recommend "76 sessions + 1 portal page," stated explicitly) before a manifest can be written.

**Remaining work:**
- Fix the 76/77 session-count labeling across `_config.yml`, session footers, and `IP_and_Usage_Rights.md`.
- Generate the version manifest (file inventory + version labels + content hashes).
- Document the release decision in writing, dated, tied to the manifest version, recording Gate 1–5 satisfaction evidence — only after Gates 1–5 are actually satisfied.

**Status:** `NOT STARTED`

**Reviewer / owner decision required:** Owner must pick the session-count labeling, approve the manifest format, and issue (or withhold) the release decision. No release decision exists; none is implied by this tracker.

---

## Gate status summary

| Gate | Required | Status |
|---|---|---|
| 1. Claim-level evidence register | Register with sources + reviewer documentation (7-field schema) | `IN PROGRESS` |
| 2. Independent clinical, legal/privacy, accessibility, site-implementation review | Four documented independent reviews | `NOT STARTED` |
| 3. Site-specific safety, escalation, confidentiality, records, referral procedures | Per-site procedures with named personnel and real pathways | `IN PROGRESS` |
| 4. Facilitator authorization, training, supervision, fidelity controls | Defined, evidenced, reviewed standards | `PENDING OWNER DECISION` |
| 5. Audience-separated participant, facilitator, internal, revision documents | Documented audience map + canonical lines | `IN PROGRESS` |
| 6. Version manifest and documented release decision | Manifest + written version-specific release decision | `NOT STARTED` |

**Gates satisfied: 0 of 6. Delivery remains withheld.**

---

## Known blocking items carried into this tracker

1. **Session 20 content-safety item** — `Part-I/Session_20_Acute_Psychological_Crisis_as_Transitional_Adaptation_Phase.md` frames suicidal ideation as a "necessary" transitional phase. Do not deliver or pilot Session 20 until independent clinical review resolves it. (Gates 1, 2, 3)
2. **Unsupported authority claims** — `Part-IV/Certification_Path.md` and `Part-IV/IP_and_Usage_Rights.md` §5.0 assert a certification board and federal-agency alignment with no supporting records in the repo. (Gates 1, 4)
3. **License conflict** — CC BY-NC 4.0 root `LICENSE` vs. All-Rights-Reserved session footers and `IP_and_Usage_Rights.md`. Requires documented legal review. (Gate 2)
4. **No canonical curriculum authority** — six parallel lines, no document stating which is authoritative for delivery. (Gate 5)

---

## Tracker maintenance

- Update this file as evidence lands in the repo. Each gate update must cite the specific file(s) and commit(s) added.
- Status may only move forward on the basis of evidence in the repo — plans, intentions, and work in progress never change a status.
- New blocking findings discovered during remediation must be appended under "Known blocking items" with the gates they affect.
