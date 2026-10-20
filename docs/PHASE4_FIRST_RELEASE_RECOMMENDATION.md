# WRH Phase 4 — First-Release Recommendation (Part A)

**Phase 4 document.** Baseline: `d4b3910f49e7e4420a4968b0bdd72783cf3b5210` (PR #4 audited head, branch `review/wrh-claim-inventory-phase3`, unmerged). Prepared on branch `review/wrh-release-development-phase4`. This document records the eight-topic working development scope and its options analysis. It does not authorize release, establish delivery authority, or satisfy any release gate. **Gates satisfied: 0 of 6. Delivery remains withheld.**

---

# WRH Phase 4 — Part A: First-Release Scope Options Analysis

**Status: EIGHT-TOPIC DEVELOPMENT SCOPE SELECTED UNDER OWNER DELEGATION — DELIVERY WITHDRAWN.** The choice assigns a working development role to Lane D; it does not declare the material approved, independently reviewed, ready, or suitable for delivery. Delivery remains withheld; 0 of 6 release gates are satisfied (see `docs/REMEDIATION_TRACKER.md` and `PUBLIC_RELEASE_STATUS.md`).

**Delegation update:** The owner subsequently authorized Muse to choose the development package and proceed with non-crisis drafting. That supersedes the earlier instruction to wait for the owner to choose among eight, sixteen, or seventy-six lessons. The received export contains a recommendation, not implementation of that later instruction. Its recommended eight-topic Lane D package is recorded here as the working development choice; the two missing companion files remain unwritten. The source-reading statements below are the submitting producer’s reported activity, not a full reading independently repeated by the receiving audit. See [PHASE4_IMPORT_VERIFICATION.md](PHASE4_IMPORT_VERIFICATION.md).

**Baseline inspected:** Repo clone `~/workspace/wrh-phase4`, branch `review/wrh-release-development-phase4`, HEAD `d4b3910f49e7e4420a4968b0bdd72783cf3b5210` ("Audit Phase 3 locations, repair stale references, and bound completeness claims"). This analysis is read-only with respect to that branch; no repo files were modified.

**Evidence standard applied:** Every statement below is limited to what was actually read in the files listed in §1. Where a characterization is structural (counts, headings, file presence) rather than a full content reading, that is stated explicitly. Estimates are labeled as estimates. No efficacy, safety, or clinical-suitability judgment is made about any lesson.

---

## 1. What was actually read — and what was only characterized structurally

### 1.1 Read in full (full text inspected for this analysis)

**Framing / inventory documents**
- `CURRICULUM_MAP.md` (lane definitions A–G, topic tables, owner-decision list)
- `docs/core-curriculum/README.md` (v2.0 governing rule, constraints, collection-relationship warning)
- `docs/PHASE3_REVIEW_BACKLOG.md` (themes T1–T8, P1/P2/P3 queues, editorial/legal/accessibility queues)
- `PUBLIC_RELEASE_STATUS.md` (six gate texts, delivery-withheld status)
- `docs/REMEDIATION_TRACKER.md` (gate-by-gate status; note in particular Gate 1 "Remaining": claims in participant lessons, workbooks, and guides "remain uninventoried")
- `docs/participant-workbooks/README.md` (workbook shell, batch plan, delivery guardrails)
- `docs/ACCESSIBILITY.md` (short baseline-practices note; no assessment record)
- `docs/LICENSING_ISSUES.md` (CC BY-NC 4.0 vs. "All Rights Reserved" conflict record)

**Lane D — capitalized four-track lessons (8 files, ~3,200 lines total)**
- `docs/core-curriculum/Lesson_01_What_Is_a_Survival_Response.md` (431 lines)
- `docs/core-curriculum/Lesson_02_Safety_vs_Familiarity.md` (409 lines)
- `docs/core-curriculum/Lesson_03_Fight_Flight_Freeze_Shutdown.md` (383 lines)
- `docs/core-curriculum/Lesson_04_Impact_vs_Intention.md` (409 lines)
- `docs/core-curriculum/Lesson_05_Perception_vs_Fact.md` (400 lines)
- `docs/core-curriculum/Lesson_06_Control_vs_Influence.md` (367 lines)
- `docs/core-curriculum/Lesson_07_Accountability_vs_Blame.md` (401 lines)
- `docs/core-curriculum/Lesson_08_Ownership_vs_Defense.md` (402 lines)

> **Filename note (correction to the task brief):** The brief referred to these as `Lesson_01.md`–`Lesson_08.md` and to Lane C as `lesson-01.md`–`lesson-16.md`. The actual filenames carry full title suffixes, as listed here and in §1.1 below. The files inspected are the eight capitalized and sixteen lowercase files in `docs/core-curriculum/`; there are no bare `Lesson_01.md` / `lesson-01.md` files in the repo.

Each Lane D file was confirmed to contain the same internal architecture: four track sections — **Corrections, Reentry, Veteran, Workplace** — each with the same eight subsections (1. Core Connection; 2. Environmental Translation; 3. Recognizable Scenario; 4. Seven-Step Application [Recognize → Name → Explain → Separate → Interrupt → Practice → Carry It]; 5. Accountability Check; 6. Boundary Check; 7. Next Action; 8. Carry-Forward). The core distinction is held constant across tracks; scenario and environmental translation vary by setting.

**Lane C — lowercase participant lessons (16 files, ~3,660 lines total)**
- `docs/core-curriculum/lesson-01-what-is-a-survival-response.md` (199 lines)
- `docs/core-curriculum/lesson-02-when-your-body-reacts-before-you-can-think.md` (192 lines)
- `docs/core-curriculum/lesson-03-fight-flight-freeze-and-shutdown.md` (209 lines)
- `docs/core-curriculum/lesson-04-understanding-dissociation.md` (169 lines)
- `docs/core-curriculum/lesson-05-the-threat-loop.md` (189 lines)
- `docs/core-curriculum/lesson-06-why-patterns-repeat.md` (189 lines)
- `docs/core-curriculum/lesson-07-why-knowing-better-doesnt-always-mean-doing-better.md` (171 lines)
- `docs/core-curriculum/lesson-08-shame-avoidance-and-reinforcement.md` (199 lines)
- `docs/core-curriculum/lesson-09-when-survival-behavior-gets-misread.md` (175 lines)
- `docs/core-curriculum/lesson-10-understanding-without-excusing.md` (167 lines)
- `docs/core-curriculum/lesson-11-where-can-the-loop-be-interrupted.md` (187 lines)
- `docs/core-curriculum/lesson-12-communication-when-your-system-wants-to-shut-down.md` (179 lines)
- `docs/core-curriculum/lesson-13-stabilization-and-the-next-small-action.md` (341 lines)
- `docs/core-curriculum/lesson-14-agency-accountability-and-boundaries.md` (330 lines)
- `docs/core-curriculum/lesson-15-identity-after-survival.md` (362 lines)
- `docs/core-curriculum/lesson-16-building-something-different.md` (400 lines)

Lessons 1–12 share a uniform seven-part structure (1. Recognize ["Have you ever…"]; 2. Name; 3. Explain; 4. Separate; 5. Interrupt; 6. Practice; 7. Carry It), written in second-person narrative voice with embedded writing prompts. Lessons 13–16 are materially longer (330–400 lines vs. 167–209) and include additional sections such as "Before You Begin," "Why This Matters," "Common Misunderstandings," "Permission," "Reflection Questions," "Key Takeaways," and (13–15) "Next Lesson." That format break inside Lane C is a file-level fact, not an interpretation, and is treated as a gap in §3.

**Lane E — participant workbook (1 file)**
- `docs/participant-workbooks/Workbook_Lessons_01_04.md` — read in full. Fifteen numbered sections per lesson following Recognize → Name → Explain → Separate → Interrupt → Practice → Accountability → Boundary → Next Action → Carry It, plus a 0/1/2 Recognize/Own/Change self-assessment and an optional reflection explicitly marked "OPTIONAL — NO FORCED DISCLOSURE REQUIRED." Covers Lane D topics 1–4 only (see §2.3).

**Lane F — facilitator guide (1 file)**
- `docs/facilitator-guides/Facilitator_Guide_Lessons_05_08.md` — read in full. Per lesson: Facilitator Anchor (core trap, reframe, anchor line, pushback script), Room Dynamics & De-escalation scripts, Scoring & Self-Assessment rubric, Five-Minute Practicum; plus a quick-reference card and a seven-step redirect sequence. Covers Lane D topics 5–8 only (see §2.3). There is no README in `docs/facilitator-guides/` (directory listing confirmed: the guide file is the only file present).

### 1.2 Searched for Lane C companion materials — what was found and not found

Searches performed: full-text grep across the repo (excluding `archive-imports/`) for `lesson-09`…`lesson-16` references; grep of `docs/core-curriculum/README.md`, `docs/participant-workbooks/`, `docs/facilitator-guides/`, and `docs/index.html` for workbook/facilitator/handout references; directory listings of `docs/participant-workbooks/`, `docs/facilitator-guides/`, `Part-IV/Participant-Materials/`, `Part-IV/Facilitator-Toolkit/`, and `new-system/handouts/` / `new-system/sessions/`.

**Found:**
- The only references to Lane C lessons 9–16 outside the lesson files themselves are in `docs/core-curriculum/README.md` and `CURRICULUM_MAP.md`. No workbook, facilitator guide, or handout anywhere in the repo is keyed to Lane C topics or numbering.
- `docs/participant-workbooks/README.md` plans a second workbook file, `Workbook_Lessons_05_08.md` (Batch 2, Lane D topics 5–8), explicitly recorded as "file not present." It also states: "Batch 1 should be verified across Corrections, Reentry, Veteran, and Workplace settings before production moves to Lessons 9–16" — i.e., the workbook roadmap itself assumes the Lane D eight-topic spine first, with "Lessons 9–16" as a later, undefined extension.
- `Part-IV/Participant-Materials/` contains Plan B / safety cards (`PLAN-B-HANDOUT.md`, `Plan_B_Wallet_Card.md`, `Digital_Plan_B_Card.md`, `Mobile_Plan_B_View.md`, `Safety_and_Participation_Rules.md`) and `Part-IV/Facilitator-Toolkit/` contains facilitator rules/readiness/decompression files. These are Lane A / Part IV operational materials, **not** companions to Lane C or Lane D lessons; the map and tracker treat Part IV as withdrawn operational source.
- Lane B (`new-system/`, 14 facilitator scripts + 13 handouts) is a separate rewrite sequence with its own numbering and a concordance (`new-system/CONTENT_CONCORDANCE.md`); per the map it "does not cover every master session" and is not a companion set for Lane C or Lane D. It is out of scope for the three options compared here except as a possible future source the owner has not assigned to any package.

**Not found:**
- No workbook for Lane C (any lessons). No workbook for Lane D lessons 5–8. No facilitator guide for Lane D lessons 1–4. No facilitator guide for Lane C (any lessons). No participant handouts keyed to Lane C or Lane D. No document in the repo that formally associates the workbook or the guide with either lane — both READMEs and the map record title correspondence only and state that formal association is unapproved / an owner decision.

### 1.3 Characterized structurally only (NOT content-read for this analysis)

**Lane A — the 76 master facilitator scripts** (`Part-I/` Sessions 01–26 + Session 12 Pilot Portal; `Part-II/` Sessions 27–56; `Part-III/` Sessions 57–75; `Part-IV/` Session 76), plus Part IV operational files. For Option 3 (§4) this collection is characterized from `CURRICULUM_MAP.md`, `docs/PHASE3_REVIEW_BACKLOG.md`, `docs/PHASE3_FINDINGS_REPORT.md`, and `docs/REMEDIATION_TRACKER.md` — counts, claim-inventory totals, and blocker locations. **The 76 scripts were not re-read for this analysis, and no content-quality judgment about them is made here.** The Phase 3 ledger reports prior full-text reading of the master sessions by the Phase 3 producer; that is a producer-reported record, cited as such, not re-verified here.

---

## 2. Option 1 — Eight-topic core package (Lane D authoritative)

### 2.1 Intended audience(s), as the materials state them

- `CURRICULUM_MAP.md`, Lane D row: "Participants in Corrections, Reentry, Veteran, Workplace tracks."
- `docs/core-curriculum/README.md`: the four-track files are "settings-specific translations of the core lesson content," and the directory's participant-facing standard is quoted as: written at an "8th-grade reading level," "zero clinical jargon," "no forced disclosure," "non-diagnostic: participants do not need to accept a label or agree with a framework to recognize a pattern and decide what to do next."
- The workbook's closing standard (`Workbook_Lessons_01_04.md`, "Batch 1 — Participant Workbook Standard") states: "The **core lesson does not change by population**. The Corrections, Reentry, Veteran, and Workplace applications belong in the **Systems Application Layer**, preserving the architectural firewall." This is an architectural assertion inside the material itself; whether that firewall claim holds is a reviewer question, not established by this analysis.
- Reading the eight files confirms the stated structure in practice: identical core distinctions across tracks (e.g., Lesson 5, Workplace: "Perception is an interpretation. Fact is what can be established."), with scenarios localized (Corrections: staff/consequence scenarios; Workplace: supervisor email — "See me when you get a chance"; Reentry/Veteran analogues). No file states an age range, literacy prerequisite beyond the README standard, exclusion criterion, or mandated-vs-voluntary status. Audience separation for mandated settings is therefore not defined in the materials — it is a Gate 3/Gate 5 gap, not a detail this analysis can supply.

**Topics (Lane D):** 1 What Is a Survival Response? · 2 Safety vs. Familiarity · 3 Fight, Flight, Freeze & Shutdown · 4 Impact vs. Intention · 5 Perception vs. Fact · 6 Control vs. Influence · 7 Accountability vs. Blame · 8 Ownership vs. Defense.

### 2.2 Proposed authoritative source collection

Working development choice under the owner’s delegation: `docs/core-curriculum/Lesson_01_…`–`Lesson_08_…` (Lane D), with Lane E and Lane F as proposed matching development layers. **Baseline history:** before this delegated choice, the repository had not assigned these roles. `docs/core-curriculum/README.md` states the two collections' relationship is "currently undocumented" and records an owner decision as needed on "which is canonical"; `CURRICULUM_MAP.md` owner-decision items 1–3 and Gate 5 in the tracker leave facilitator-lane authority, collection relationships, and workbook/guide association all open. The delegated development choice now assigns working roles; content alignment and delivery authorization remain separate, outstanding questions.

### 2.3 Existing matching materials — exact files and coverage gaps

| Component | Exists | Coverage | Gap |
|---|---|---|---|
| Participant lessons | `Lesson_01`–`Lesson_08` (Lane D) | 8/8 topics, 4 tracks each (32 track-sections) | None at lesson level |
| Participant workbook (Lane E) | `docs/participant-workbooks/Workbook_Lessons_01_04.md` | Topics 1–4 only | **`Workbook_Lessons_05_08.md` absent** (planned as Batch 2 in the workbook README; file not present) |
| Facilitator guide (Lane F) | `docs/facilitator-guides/Facilitator_Guide_Lessons_05_08.md` | Topics 5–8 only | **No facilitator guide for topics 1–4 exists anywhere in the repo** |
| Handouts | None keyed to Lane D | — | No Lane D handout set exists; Lane B's 13 handouts belong to a different sequence and cannot be assumed to transfer |
| Workbook track coverage | Workbook is written as a single generic participant text | The workbook README requires Batch 1 to be "verified across Corrections, Reentry, Veteran, and Workplace settings" | No per-track workbook variants exist; whether one generic workbook serves four mandated/voluntary settings is unverified |

The asymmetry is exact and worth stating plainly: **the workbook covers the first half, the guide covers the second half, and neither covers the whole eight.** A deliverable eight-topic package today would ship a workbook with no facilitator support for its lessons, and a facilitator guide whose lessons have no workbook.

### 2.4 Missing components (concrete, file-level)

1. **Author:** `docs/participant-workbooks/Workbook_Lessons_05_08.md` (topics 5–8), following the 15-section shell in `docs/participant-workbooks/README.md`.
2. **Author:** a facilitator guide for topics 1–4 (no planned filename exists in the repo; use `Facilitator_Guide_Lessons_01_04.md` as the working counterpart filename; no such file was delivered in this patch).
3. **Decide + document:** formal association of Lane E and Lane F with Lane D (currently title correspondence only), including a fidelity check that workbook/guide wording matches the Lane D lesson wording track by track.
4. **Numbering alignment:** Lane D numbering (1–8) collides with Lane C numbering (1–16) on different topics from Lesson 2 onward (Lane D 2 = Safety vs. Familiarity; Lane C 2 = When Your Body Reacts…). Until the owner resolves §2.2, any package manifest must carry lane-qualified identifiers to prevent the exact mispairing the Phase 1 map originally made and Phase 1 had to correct.
5. **Claim inventory:** per the tracker (Gate 1, Remaining), the claims in Lane D, the workbook, and the guide are **uninventoried** — no entries in `docs/EVIDENCE_REGISTER.md` cover them. A claim-level inventory of 8 lessons × 4 tracks + workbook + guide is required before Gate 1 can advance for this package.
6. **Accessibility work:** Gate 2 accessibility review is entirely outstanding (backlog: "No accessibility assessment was performed in Phase 3"). `docs/ACCESSIBILITY.md` lists aspirations (plain language, large print, mobile-friendly, paced participation) with no assessment record, no reading-level verification of the Lane D files, and no large-print/mobile renditions in the repo.
7. **Site/facilitator infrastructure:** no site-specific safety/escalation/confidentiality/records/referral procedures (Gate 3), no facilitator authorization/training/supervision/fidelity controls (Gate 4) exist for this package; the Lane F guide is an execution matrix, not a training or authorization standard.

### 2.5 Review dependencies

- **Gate 1 inventory first:** this package drags in no existing backlog entries directly (its claims were never inventoried), so its first dependency is new inventory work, then disposition by qualified reviewers.
- **Correction to the brief's premise on T6:** the task brief stated that "lane D's diagnostic reclassification language falls under backlog T6." On full-text inspection and targeted grep (diagnos*, disorder, PTSD/CPTSD, "system mismatch," symptom-relabeling patterns), **no diagnostic-reclassification language of the T6 form was found in the eight Lane D files.** The files are, as written, behavioral and plain-language (e.g., Lesson 3, Corrections: patterns are "patterns to recognize—not permanent boxes or excuses"). T6's 109 diagnostic-tagged entries are inventoried in the **master sessions (Lane A)**, per `docs/PHASE3_REVIEW_BACKLOG.md`. This analysis therefore does **not** assign T6 to Lane D. What Lane D does require is (a) confirmation by a qualified clinical reviewer that its physiology-adjacent framing (survival response, body-reacts-first) is acceptable as psychoeducation — a Gate 2 clinical-review question, currently unasked because the material is uninventoried — and (b) consistency review against whatever disposition T6 receives for Lane A, so the two collections do not teach contradictory framings of the same phenomena if both survive. Recording this correction matters: assigning T6 to Lane D would overstate Lane D's known risk and understate that its actual status is *unexamined*, which is a different problem.
- **T3-adjacent check (minor):** Lane D's Interrupt steps include brief directive prompts (e.g., pause/breath-type actions appear in the workbook's interruption checklists: "Take one slow breath"). These are not the scripted Anchor protocols of T3 (which are Lane A session-opening scripts), but a clinical reviewer should confirm where the line sits; flagged here as a question, not a finding.
- **Licensing/legal queue:** the CC BY-NC 4.0 vs. "All Rights Reserved" conflict (`docs/LICENSING_ISSUES.md`) applies repo-wide and therefore to this package's files; Gate 2 legal review is a dependency regardless of scope choice.

### 2.6 Relative completion effort — ESTIMATE

**Estimate (reasoned, not a commitment): smallest of the three options.** Rationale: the lesson layer is complete (8/8); exactly two companion files are missing (workbook 5–8; guide 1–4), both with an existing template/shell to follow (the workbook README's 15-section shell; the Lane F guide's per-lesson format); claim-inventory surface is bounded (10 files). The dominant cost is not authoring but the shared gate work (inventory → clinical/legal/accessibility review → site procedures → facilitator controls → version manifest), which no option avoids. Relative to Option 2: fewer topic titles, but four track sections per topic; file/topic counts alone do not quantify reviewer effort. Relative to Option 3: an as-yet-uninventoried claim surface, whose size cannot be numerically compared with Lane A’s register (see §4.6).

---

## 3. Option 2 — Sixteen-lesson participant package (Lane C authoritative)

### 3.1 Intended audience(s), as the materials state them

- `CURRICULUM_MAP.md`, Lane C row: audience "Participants"; description "Draft participant sequence."
- `docs/core-curriculum/README.md`: the lowercase files are "the standalone participant-facing lessons," under the same directory standard quoted in §2.1 (8th-grade reading level, zero clinical jargon, no forced disclosure, non-diagnostic).
- Unlike Lane D, **Lane C states no setting or population segmentation at all** — no Corrections/Reentry/Veteran/Workplace tracks, no setting-specific scenarios as a system. Scenarios are general-life (work, family, phone calls, driving, meetings). The materials do not state whether the sequence is intended for the same four settings as Lane D, for general/community use, or for self-guided use. That silence is itself a finding: the intended delivery setting for Lane C is undefined in the repo, which blocks Gate 3 (site procedures) and Gate 5 (audience separation) scoping for this option until the owner defines it.
- Voice note (observed, file-level): Lessons 1–12 use informal second-person narrative including occasional profanity in quoted inner speech (e.g., Lesson 7: *"Yeah. I fucking know."*; Lesson 2: *"Why the hell couldn't I say that five minutes ago?"*). Whether that register is appropriate for any given setting (particularly mandated Corrections settings) is an owner/reviewer decision; it is recorded here because it is a concrete difference from Lane D's register, which contains no such language in the files inspected.

**Topics (Lane C):** 1 What Is a Survival Response? · 2 When Your Body Reacts Before You Can Think · 3 Fight, Flight, Freeze & Shutdown · 4 Understanding Dissociation · 5 The Threat Loop · 6 Why Patterns Repeat · 7 Why Knowing Better Doesn't Always Mean Doing Better · 8 Shame, Avoidance & the Reinforcement Loop · 9 When Survival Behavior Gets Misread · 10 Understanding Without Excusing · 11 Where Can the Loop Be Interrupted? · 12 Communication When Your System Wants to Shut Down · 13 Stabilization & the Next Small Action · 14 Agency, Accountability & Boundaries · 15 Identity After Survival · 16 Building Something Different.

The sequences differ in topic ordering and titles. Shared numbering does not establish pairing. Related themes also appear under different titles, including Lane C Lessons 10 and 14; this analysis does not establish absence of every Lane D topic from Lane C or vice versa. Content fidelity requires a passage-level comparison, not a title comparison.

### 3.2 Proposed authoritative source collection

Proposed (not decided): `docs/core-curriculum/lesson-01-…`–`lesson-16-…` (Lane C) as the authoritative participant source. **Flag:** same undecided status as §2.2 — the README's owner-decision note covers this collection directly. Choosing Lane C also forces a second undecided question Lane D does not: what happens to the existing Lane E workbook and Lane F guide, whose titles match Lane D topics and which the map states "cannot be assigned to Lane C by number alone." Under Option 2 those two files become orphans requiring retirement, rework, or reassignment by explicit owner decision.

### 3.3 Existing matching materials — exact files and coverage gaps

| Component | Exists | Coverage | Gap |
|---|---|---|---|
| Participant lessons | `lesson-01`–`lesson-16` (Lane C) | 16/16 topics | Format break at Lesson 13 (see §3.4) |
| Participant workbook | **None for Lane C** | 0/16 | Entire workbook layer absent; Lane E workbook is keyed to Lane D topics 1–4 and cannot be reassigned by number |
| Facilitator guide | **None for Lane C** | 0/16 | Entire facilitator layer absent; Lane F guide is keyed to Lane D topics 5–8 |
| Handouts | **None for Lane C** | 0/16 | No handout set exists |
| Setting tracks | None | — | No Corrections/Reentry/Veteran/Workplace variants exist for any Lane C lesson |

In short: Option 2's lesson layer is the most complete of any lane (16 topics), and its support layer is **empty** — the inverse of Option 1's position.

### 3.4 Missing components (concrete, file-level)

1. **Author from scratch:** a participant workbook covering 16 lessons (no shell exists for Lane C; the Lane E 15-section shell could be proposed for reuse, but that reuse is itself an owner decision because the shell was written for Lane D's architecture, including its Accountability/Boundary phase).
2. **Author from scratch:** a facilitator guide covering 16 lessons (format could follow Lane F's anchor/dynamics/scoring/practicum structure — again a proposal, not an existing plan; no document in the repo plans a Lane C guide).
3. **Format unification inside Lane C:** Lessons 13–16 (341/330/362/400 lines) carry "Before You Begin," "Why This Matters," "Common Misunderstandings," "Permission," "Reflection Questions," and "Key Takeaways" sections that Lessons 1–12 (167–209 lines) lack, and use title case headings where 1–12 use all-caps. Either 1–12 must be extended or 13–16 trimmed, or the difference documented as intentional — an ordinary editorial development decision, and a version-manifest complication until resolved.
4. **Numbering collision resolution:** as §2.4(4), but worse under this option — adopting Lane C as authoritative makes Lane D's identically numbered files the collision risk, and the existing workbook/guide (Lane D titles) become actively misleading if left in place unretired.
5. **Claim inventory:** all 16 lessons uninventoried (Gate 1), same as Lane D but double the lesson count.
6. **Setting definition + accessibility:** delivery setting undefined (§3.1); accessibility review outstanding repo-wide; reading-level verification outstanding; no large-print/mobile renditions exist.
7. **Register review:** the profanity-in-inner-speech noted in §3.1 requires an explicit owner/reviewer decision per intended setting before any mandated-setting use could be contemplated.

### 3.5 Review dependencies

- **Dissociation content (Lesson 4) — the heaviest single dependency in either participant lane.** Lesson 4 names and teaches "Dissociation" as a participant-facing concept and, in its Interrupt/Practice sections, delivers a directive grounding-style exercise: "**Name five things you can see.** … **Where are my feet?** … **Five things I can see.** … That's your anchor." Whatever the merits, this is an instructed technique delivered to participants, structurally closer to the T3 question (scripted regulation instructions: "what role, optionality, contraindication screening, and escalation boundary apply") than anything in Lane D. It requires qualified clinical review before any delivery consideration. This analysis makes no judgment about the exercise's appropriateness — only that it is a delivered instruction, not mere description, and therefore cannot ride on an editorial-only queue. Lesson 4's driving passage ("If you're driving and realize you aren't fully focused, **safety comes first**") likewise belongs in the clinical/site review set.
- **Lesson 2 breathing prompt:** "Take one breath" appears as an Interrupt step — minor, but belongs in the same clinical-review batch as the Lesson 4 exercise for a consistent disposition on instructed regulation techniques in participant materials (cf. §2.5).
- **Identity content (Lesson 15):** "Identity After Survival" teaches a learn-vs-identity distinction ("A person can learn anger without being an angry person… Survival shaped you. It does not have to own you."). This is identity-framing psychoeducation; it is **not** the T6 diagnostic-reclassification pattern (no symptoms are relabeled, no diagnosis is displaced), but a clinical reviewer should confirm that boundary rather than this analysis asserting it.
- **No crisis content found:** targeted grep found no suicide/self-harm/hotline/crisis-procedure content in Lane C; Lesson 13's only "emergency" reference is figurative ("stop treating every problem like an emergency"). Lane C therefore does **not** drag in T1/T2 (Session 20 / Session 76 / Crisis Package) — a genuine advantage over Option 3. It still requires the repo-wide legal/licensing review and Gate 2 accessibility review.

### 3.6 Relative completion effort — ESTIMATE

**Qualitative estimate: more companion-authoring work than Option 1; no numerical effort ratio established.** Rationale: lesson layer complete (16/16) but support layer is 0/16 on both workbook and facilitator sides (vs. Option 1's 4/8 + 4/8 with templates on both sides); plus a format-unification pass across 16 files; plus the Lesson 4 clinical-review dependency, which is a scheduling risk (qualified reviewer availability) rather than an authoring cost. Offsetting factor: only one audience definition is needed if the owner scopes Lane C to a single setting type — but the repo currently defines none, so that scoping work is net-new.

---

## 4. Option 3 — Full 76-session package (Lane A authoritative)

> **Structural characterization only.** Per §1.3, the 76 master scripts were not re-read for this analysis. Everything in this section derives from `CURRICULUM_MAP.md`, `docs/PHASE3_REVIEW_BACKLOG.md`, `docs/PHASE3_FINDINGS_REPORT.md`, and `docs/REMEDIATION_TRACKER.md`. No content-quality judgment about individual sessions is made or implied.

### 4.1 Intended audience(s), as the materials state them

- `CURRICULUM_MAP.md`, Lane A row: audience "Facilitator source"; status "Preservation/remediation source. Not an approved delivery package."
- Composition (map, verified against directory listing): Part I Sessions 01–26, Part II Sessions 27–56, Part III Sessions 57–75, Part IV Session 76 — **76 numbered scripts plus one additional page**, `Part-I/Session_12_Pilot_Portal.md` (a portal, not a 77th session; Phase 1 corrected earlier "77-session" labels).
- The audience the scripts address in delivery (participants in the sessions' scenarios) is not characterized here, because that would require reading the scripts. What the framing documents establish is narrower: these are facilitator-delivered scripts, with Part IV adding operational material (crisis package, certification path, pricing/tiers, IP terms, facilitator toolkit, participant Plan B materials).

### 4.2 Proposed authoritative source collection

Proposed (not decided): Lane A (`Part-I/`–`Part-IV/`) as authoritative facilitator source. **Flag:** `CURRICULUM_MAP.md` owner-decision item 1 — "Choose the future facilitator reference lane and its relationship to the master inventory" — is undecided, and Lane B (the 14-script rewrite) exists precisely as an unassigned alternative/companion. The tracker (Gate 5) repeats that no authoritative collection has been established. Option 3 therefore requires the largest authority decision of the three options, not the smallest, despite Lane A being the historical "master."

### 4.3 Existing matching materials — exact files and coverage gaps

| Component | Exists | Coverage | Gap |
|---|---|---|---|
| Facilitator scripts | 76 numbered + 1 portal | Full sequence present as source files | Presence is inventory, not readiness (map: headings/presence "establish inventory, not completeness, readability, efficacy, or delivery readiness") |
| Participant materials authored for the 76 | **None** | 0/76 | No participant lessons, workbooks, or handouts were authored against the master sequence. The only participant-facing sets in the repo belong to Lane C (16 lessons), Lane D/E (8 topics / workbook 1–4), and Lane B (13 handouts against a different 14-session rewrite sequence, per the concordance) — none is a participant layer for Lane A |
| Facilitator guides | Part IV toolkit/prerequisites/certification drafts | Draft source only | Certification pathway is labeled an unapproved draft; IP document's compliance/agency assertions are flagged unverified with no supporting records found in this repo (tracker, Gate 4) |
| Operational/safety | Session 76, `Part-IV/Crisis_Package.md`, safety templates | Present as withdrawn source | Templates carry unfilled placeholders and withdrawal notices; no site-specific procedures exist (Gate 3) |

### 4.4 Missing components

1. **An entire participant layer:** lessons/workbooks/handouts for 76 sessions do not exist and would have to be authored or explicitly waived by an owner decision that a facilitator-only package is the intent (which then re-opens Gate 5 audience-separation design).
2. **Disposition of Session 20** (see §4.5) — a precondition, not a component.
3. **Disposition of Session 76 + Crisis Package operational content** — clinical + site review of procedures, not just claims.
4. **Certification/agency substantiation or removal:** supporting records for the certification and agency claims in Part IV / the Session 12 portal, or revision to remove them (map owner-decision item 6; backlog editorial queue item 4 notes the portal also lacks the withdrawal header other withdrawn materials carry).
5. **Claim disposition at scale:** 782 Phase 3 entries (977 entry-location records) plus the 15 Phase 2 entries, all with reviewer fields PENDING; 255 are P1.
6. **Accessibility, site procedures, facilitator controls, version manifest:** all six gates, at 76-session scale.

### 4.5 Review dependencies (the decisive section for this option)

Option 3 drags in **every** backlog theme, because the backlog was built from Lane A:

- **T1 — Session 20 crisis framing (CLINICAL, blocking):** blocking entries WRH-ER-001–004 plus 7 further Phase 3 gap claims (including the "Deconstruction Loop" whiteboard mechanism, the group "Rebirth Protocol" instruction, and a temporariness affirmation). Backlog instruction: these "must be dispositioned together with ER-001–004 by a qualified suicide-prevention clinician." No replacement wording exists. **This alone blocks a full-76 release regardless of all other work.**
- **T2 — Session 76 + Crisis Package (CLINICAL + SITE):** 12 + 4 gap claims including lethal-means-related instructions, an SPI trigger definition, a 7-day follow-up obligation (ER-797), and institutional claims (ER-782, ER-793) that also sit in the legal queue. All 23 safety-instruction-tagged entries repo-wide belong to this queue.
- **T3 — Anchor protocols (CLINICAL):** 3 entries at 99 entry-location matches — scripted breathing/grounding instructions read aloud at session openings across the curriculum.
- **T4 — "One second of air" refrain (CLINICAL):** 53 entries / 139 location records / 72 literal positions, with an internal "one second" vs. "three seconds" inconsistency in Session 50.
- **T5 — "Somatic markers of this law" family (CLINICAL, blocking relationship):** 21 entries / 22 locations extending ER-001's blocking question curriculum-wide.
- **T6 — Diagnostic reclassification (CLINICAL):** 109 diagnostic-tagged entries (e.g., "You are reacting to the system mismatch, not just your own symptoms"; "System-Mismatched" as an identity label). **This is where T6 actually lives** — in Lane A (see the correction in §2.5).
- **T7 — Deterministic permanence (CLINICAL):** a subset of 177 universal-deterministic entries stating permanence as biological fact.
- **T8 — Promised treatment effects (CLINICAL):** 129 treatment-effect-tagged entries, including named protocols (Translation Protocols, Parts Audit, Witness Install, New Story Protocol) with assured outcomes and, per the backlog, no evaluating source in any phase.
- **P2/P3 tail:** 425 physiology-mechanism + 343 causal tags, 36 numerical claims, 30 recovery predictions, unattributed polyvagal constructs, and 82 P3 entries — dispositionable partly by family decisions, but only after the P1 families are decided.
- **Legal queue:** ER-782/ER-793, portal certification assertions, and the footer/license conflict (95 files carry "All Rights Reserved" footers against the root CC BY-NC 4.0 grant).

No subsetting trick avoids this: releasing "the full 76" means every family above is in scope by definition. A reduced master-session subset would be a different option (a variant of Option 1 thinking applied to Lane A), not Option 3 as defined.

### 4.6 Relative completion effort — ESTIMATE

**Qualitative estimate: largest overall remediation scope; no numerical effort multiplier established.** Rationale: claim-disposition surface is 797 register entries (255 P1) vs. a to-be-created inventory for 8–16 short lessons in Options 1–2; two blocking clinical questions (T1, and T5's blocking relationship) require a qualified suicide-prevention clinician whose disposition may require redesign, not editing; Session 76/Crisis Package require site-implementation review in addition to clinical review; an entire participant layer is missing; certification/agency claims require records or removal. Reviewer-hours and elapsed time have not been estimated from a documented effort model; family grouping, four-track review, and reviewer availability may change relative effort. This is an estimate of relative effort only; no timeline is offered, because reviewer availability — the binding constraint — is unknown.

---

## 5. Side-by-side summary

| Dimension | Opt. 1: Lane D 8-topic | Opt. 2: Lane C 16-lesson | Opt. 3: Full 76 (Lane A) |
|---|---|---|---|
| Lesson/script layer | Complete (8/8, 4 tracks) | Complete (16/16, format break at 13) | Present as source (76+portal), not delivery-ready |
| Workbook | 4/8 (topics 1–4) | 0/16 | 0/76 (none authored) |
| Facilitator guide | 4/8 (topics 5–8) | 0/16 | Draft Part IV source only, unapproved |
| Audience as stated | 4 named settings tracks | "Participants," setting undefined | Facilitator source |
| Claim inventory status | Uninventoried | Uninventoried | Inventoried (797 entries), 0 dispositioned |
| Blocking clinical items | None identified in the files as read | None crisis-related; Lesson 4 grounding instruction needs clinical review | T1 (Session 20) + T5 blocking relationship; T2 crisis operations |
| Backlog themes dragged in | None directly; consistency-with-T6-disposition check | T3-type question via Lesson 4 (by analogy — flagged as a question, not a backlog assignment) | T1–T8, all queues, in full |
| Missing authoring | 2 files (workbook 5–8; guide 1–4) | 2 layers × 16 lessons + format unification | Entire participant layer (76) |
| Relative effort (qualitative only) | Least missing companion authoring; four-track review remains | More companion authoring; scope-sensitive review | Broadest source and operational remediation; no multiplier quantified |

---

## 6. Working development path — eight-topic Lane D package

**Use Option 1 (the eight-topic Lane D package) as the first-release development scope under the owner’s delegation.** This records the working choice, not a delivery decision.

Reasons, each grounded in the files read:

1. **It has existing workbook and guide files with matching topic titles.** Lane E and Lane F — flawed and half-covering as they are (§2.3) — exist only for Lane D topics. Lane A also has operational/toolkit material, so this is not an absence-of-all-support finding for that lane. Option 1 has partial companion coverage whose templates, shells, and standards are already written down (workbook README shell; Lane F guide format).
2. **Its lesson files explicitly separate four setting tracks.** Four named settings tracks with localized scenarios give Gate 3 (site procedures) and Gate 5 (audience separation) something concrete to be written against. Lane A also names institutional settings in its wider materials; facilitator-source status does not establish an absence of audience definition. Every option still needs explicit audience and site boundaries.
3. **It excludes the already-identified master-session crisis blockers from the development package.** Lane D, the workbook, and the guide still need their own complete claim inventory and review; this analysis does not certify absence of clinical concerns or implied effect claims. Its review dependency is prospective (inventory + clinical confirmation), whereas Option 3's is retrospective and blocking (T1/T2/T5), and Option 2 carries one genuine clinical-review item (Lesson 4's instructed grounding exercise).
4. **Its numbering, if adopted, resolves the collision in the safer direction.** The existing workbook/guide titles already match Lane D; adopting Lane C instead would orphan the only two support files the repo has.

**Conditions (part of the recommendation, not afterthoughts):**
- **Condition A — Lane C is preserved, not deleted.** Designate Lane C explicitly as a deferred second sequence (or as source material for a later expansion), with its Lessons 9–16 topics recorded as the candidate expansion set. The workbook README's own roadmap ("before production moves to Lessons 9–16") gestures at this; the owner should make it a recorded decision so Lane C's 16 files are not left as a competing, identically numbered authority.
- **Condition B — complete the two missing companion files before final package sign-off**, so reviewers can ultimately assess a complete package (lessons + workbook 1–8 + guide 1–8) rather than fragments: `Workbook_Lessons_05_08.md` and `Facilitator_Guide_Lessons_01_04.md`. Qualified reviewers may be consulted earlier during development; this condition does not bar early review.

**What this recommendation is not:** it is not a finding that Lane D is clinically sound, evidence-supported, or deliverable. Lane D's claims are uninventoried and unreviewed; Gates 1–6 all remain unsatisfied under every option, including this one. The recommendation is solely about which scope gives the owner the smallest, best-defined path to a reviewable package.

**Variant considered and not recommended as the primary path:** an Option 1+2 hybrid (Lane D 8 topics now, Lane C lessons 9–16 topics ported later). Rejected as a *first*-release scope because it imports Lane C's format break, its Lesson 4-type questions do not arise in 9–16 but its support layer is still zero, and dual-authority numbering risk persists until Condition A is decided. It remains available to the owner as a later development scope after the first release decision.

---

## 7. Owner decisions needed next

### 7.1 Working development decisions under owner delegation

1. Use Lane D’s eight-topic sequence as the development spine, with D-01…D-08 as package identifiers. Preserve source filenames and distinguish these IDs from Lane C and the master sessions.
2. Preserve Lane C as deferred source; do not delete it or silently treat its later lessons as an approved extension of Lane D.
3. Associate the existing workbook 1–4 and facilitator guide 5–8 with Lane D for development, subject to full content-alignment checks. Author the missing workbook 5–8 and guide 1–4 under the counterpart filenames above.
4. Use the existing Lane F format as a working guide template, improving it where the package’s actual delivery needs require. The format alone does not establish adequate facilitator training or execution detail.
5. Lane A, including Sessions 20 and 76 and the Crisis Package, is excluded from the first development package and remains withdrawn. Lane B is preserved; its scripts and handouts do not automatically join the package.
6. Keep the current plain-language register as the drafting default. Audience suitability, accessibility, and required factual revisions remain review questions. Routine drafting and numbering choices do not require another package-selection approval.

**Implementation gap:** None of the above authoring is present in the supplied Phase 4 patches. The eight lessons and existing companions are still baseline source, and the two missing companion files are still absent. The delegated drafting work remains to be completed and verified.

### 7.2 Decisions requiring counsel or qualified reviewers (owner commissions; cannot self-disposition)

1. **Licensing intent and scope (legal counsel):** resolve CC BY-NC 4.0 vs. "All Rights Reserved" / `Part-IV/IP_and_Usage_Rights.md` for the package files; establish the prior-distribution history and surviving CC grants before any new terms are set (`docs/LICENSING_ISSUES.md` questions 1–5; Gate 2 legal queue). Also: licensing intent for the first release specifically (who may receive it, under what terms) must be counsel-reviewed, not inferred from the root LICENSE.
2. **Clinical review scope (qualified clinical reviewer(s)):** commission (a) claim-level inventory and disposition for the Option 1 package files (Gate 1); (b) explicit review of Lane D's physiology-adjacent framing and of the workbook/guide interruption prompts (§2.5); (c) if Lane C remains a live expansion candidate, review of Lesson 4's instructed grounding exercise and Lesson 15's identity framing so a later decision is informed. Reviewer qualifications and scope must be documented per Gate 2.
3. **Audience/setting suitability (clinical + site-implementation reviewers):** confirm the four settings (Corrections, Reentry, Veteran, Workplace) as the intended delivery settings, audience separation between mandated and voluntary contexts, and whether a single generic workbook is suitable across them (workbook README's own verification requirement). Site-specific safety, escalation, confidentiality, records, and referral procedures (Gate 3) require named sites and qualified leads — they cannot be drafted from the repo alone.
4. **Facilitator authorization model (qualified reviewers + owner):** define authorization, training, supervision, and fidelity controls for whoever delivers the package (Gate 4); Part IV's draft certification material must not be relied on without the supporting records or revision the tracker requires.
5. **Accessibility review (qualified accessibility reviewer):** reading-level verification of the package files against the stated 8th-grade standard, format assessment, and production of any required renditions (Gate 2; currently entirely outstanding).
6. **Session 20 / Lane A disposition (suicide-prevention clinician; deferred but not optional forever):** not required for an Option 1 first release, but the owner should record explicitly that Lane A — including Session 20 (T1) and Session 76/Crisis Package (T2) — remains withdrawn and out of scope, so the first-release decision cannot be misread as covering it.

---

## 8. Limitations of this analysis

- Lane A characterization is structural (from the map, backlog, findings report, and tracker), not a re-reading; no statement here should be cited as a fresh assessment of any master session's content.
- Lane C and Lane D content statements rest on the full-text inspection listed in §1.1, including targeted greps for diagnostic, crisis, and instructed-technique language; absence claims ("no X was found") mean *not found by that inspection in those files*, not a guarantee about every other file in the repo.
- No independent reviewer has assessed any material discussed here. All reviewer fields in the evidence register remain PENDING, and all six release gates remain unsatisfied, as of the baseline commit inspected.
