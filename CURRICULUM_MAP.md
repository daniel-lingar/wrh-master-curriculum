# WRH Curriculum Map

**Repository:** https://github.com/daniel-lingar/wrh-master-curriculum
**Branch:** `review/wrh-remediation-phase1` · **Created:** 2026-10-19 (Phase 1 Repository Remediation)
**Status context:** The repository is in a controlled-release / withdrawn state (`PUBLIC_RELEASE_STATUS.md`, effective 2026-09-04; delivery authorization: none). This map is an inventory of what exists in the tree. **It declares nothing canonical or approved for delivery** — canonical-authority decisions are listed under "Unresolved authority questions" and belong to the owner.

All file counts below were verified by listing directories on 2026-10-19; READMEs were not trusted on their own.

---

## Session-count note (stated explicitly)

The curriculum contains **76 numbered sessions + 1 portal page** = 77 session files:

| Part | Sessions | Files verified |
|---|---|---|
| Part I — "26 Laws of Survival" | Sessions 01–26 | 26 numbered + `Session_12_Pilot_Portal.md` (portal page) |
| Part II — behavioral systems | Sessions 27–56 | 30 files |
| Part III — institutional / systems navigation | Sessions 57–75 | 19 files |
| Part IV — facilitator toolkit + crisis protocols | Session 76 | 1 file |

`_config.yml` currently labels the curriculum "77-session" while `Part-IV/IP_and_Usage_Rights.md` and session footers say 76. Both numbers are defensible only if stated precisely: **76 numbered sessions plus the Session_12 portal page.** Owner decision needed on which label to use consistently.

---

## Lane A — Master sessions 01–76 (Parts I–IV)

**Location:** `Part-I/`, `Part-II/`, `Part-III/`, `Part-IV/`
**Audience:** Facilitators (full timed facilitator scripts).
**Numbering scheme:** `Session_NN_<Topic_Title>.md`, zero-padded two-digit numbers 01–76, one file per session.
**Actual coverage:** 76 numbered sessions, all substantive (~5–7 KB each). Part I: 01–26 (26 files) + `Session_12_Pilot_Portal.md` portal page (2.5 KB, contains a "Placeholder - Coming Soon" participant worksheet and a dead link to a nonexistent `presentation/engineering_problem.html` deck). Part II: 27–56 (30 files). Part III: 57–75 (19 files). Part IV: Session 76 only (crisis response + safety protocols), plus the Part-IV operational/toolkit layer (see "Supporting infrastructure" below).
**Format:** v5.0 "Stabilized" timed 75-minute facilitator scripts: Anchor → Episode → Mechanism → Mirror → Shift + Cliffhanger. Carries "NOT THERAPY. NO DISCLOSURE." banners.
**Documented status:** Retained in-repo "for preservation and remediation," not a delivery package (`PUBLIC_RELEASE_STATUS.md`).
**Relationship to other lanes:** The flagship content line. The new-system rewrite (Lane B) re-sequences its numbering; the core lessons, four-track lessons, and workbooks (Lanes C–E) restate its topics in participant-facing form; the facilitator guides (Lane F) support the core lessons, not these scripts.

### Known numbering divergence — Lane A vs. Lane B

The `new-system` rewrite inserts a brand-new Session 10 ("Physiological Stress Response and Bodily Signaling") with no counterpart in the old map, shifting everything after it: e.g., new-system Session 13 covers dissociation, which is master Session 10's topic area. Additionally, new-system **handouts** misalign with new-system **sessions** by topic (verified): handout 10 covers dissociation (the rewritten Session 13's topic) and handout 13 covers freeze misclassified as noncompliance (the rewritten Session 14's topic) — and the offset is not constant, so this cannot be fixed by renumbering alone. A content-verified concordance (sessions ↔ handouts, verified by content, not number) is required; owner decision needed on whether to renumber the rewrite lane (e.g., `NS-` prefix) or correct the handout numbering.

---

## Lane B — New-system rewrite (`new-system/`)

**Location:** `new-system/sessions/` (14 files), `new-system/handouts/` (13 files), `new-system/framework/` (3 docs), plus `README.md` and `SESSION-INDEX.md`.
**Audience:** Facilitators (rewrite of the master scripts).
**Numbering scheme:** `session-NN.md` and `handout-NN.md`, zero-padded, independent of Lane A's numbering.
**Actual coverage:** Rewritten scripts for sessions 01–14 (complete in the new format) + participant handouts 01–13. **Sessions 15–76 have no rewrite.** Framework docs: `WRH-NEW-SYSTEM-RULES.md`, `GOAL-AND-MISSION-BEHIND-SESSIONS.md`, `CAPITOL-CONTRACTS-MISSION.md`.
**Format:** Standardized 16-element structure (Facilitator Notes → Purpose → Takeaway → Scope Boundary → Opening → Grounding → Teaching ×2 → Lived-Pattern Anchor → Mechanism Map → Reflection → Tool → Integration → Closing → Cliffhanger), plain-language teaching titles, risk ratings, "NOT READ ALOUD" facilitator notes.
**Documented status:** Per `new-system/README.md`: "The old WRH structure is the curriculum map: session titles, architecture, and topic sequence. The new WRH structure is the delivery system: complete word-for-word facilitator scripts that can be read consistently in any location." — This paragraph does not mention Lanes C–F at all, so it does not establish a repo-wide canonical lane.
**Relationship to other lanes:** A rewrite of Lane A, covering only sessions 01–14. Numbering diverges from Lane A (see above). Participant handouts pair with the rewritten sessions by intent but misalign by topic at 10 and 13 (see above).

### Known index staleness

`new-system/README.md`'s "Folder Structure" section documents only sessions through `session-05.md` and omits `handouts/`; `new-system/SESSION-INDEX.md` lists session 14 as "Next after Session 13" while `new-system/sessions/session-14.md` already exists. Indexes must be regenerated from the directory listing.

---

## Lane C — Core participant lessons, v2.0 (lowercase)

**Location:** `docs/core-curriculum/lesson-01..16` (16 files) + `README.md`.
**Audience:** Participants (plain language, 8th-grade reading level, zero clinical jargon, no forced disclosure, non-diagnostic).
**Numbering scheme:** `lesson-NN-<topic-slug>.md`, zero-padded two-digit numbers 01–16.
**Actual coverage:** All 16 lessons present: 1 What Is a Survival Response? · 2 When Your Body Reacts Before You Can Think · 3 Fight, Flight, Freeze & Shutdown · 4 Understanding Dissociation · 5 The Threat Loop · 6 Why Patterns Repeat · 7 Why Knowing Better Doesn't Always Mean Doing Better · 8 Shame, Avoidance & Reinforcement · 9 When Survival Behavior Gets Misread · 10 Understanding Without Excusing · 11 Where Can the Loop Be Interrupted · 12 Communication When Your System Wants to Shut Down · 13 Stabilization and the Next Small Action · 14 Agency, Accountability & Boundaries · 15 Identity After Survival · 16 Building Something Different.
**Format:** The governing instructional rule "Show it → Name it → Explain it → Separate it → Interrupt it → Practice it → Carry it."
**Documented status:** Complete 16-lesson spine (added August 2026).
**Relationship to other lanes:** Participant-facing restatement of curriculum topics, intended to pair with the participant workbooks (Lane E) and facilitator execution guides (Lane F). **Unresolved:** its relationship to the four-track lessons (Lane D) sharing the same folder is undocumented — `docs/core-curriculum/README.md` documents only this 16-lesson set and never mentions Lane D.

---

## Lane D — Four-track baseline lessons (capitalized)

**Location:** `docs/core-curriculum/Lesson_01..08` (8 files).
**Audience:** Participants, track-adapted: each file contains four audience-track sections — **Corrections, Reentry, Veteran, Workplace** (verified: all 8 files contain exactly 4 `## <Track> Track` sections).
**Numbering scheme:** `Lesson_NN_<Title>.md`, zero-padded two-digit numbers 01–08. There are **not** separate files per track — each lesson file holds all four tracks.
**Actual coverage:** All 8 lessons present: 1 What Is a Survival Response? · 2 Safety vs. Familiarity · 3 Fight, Flight, Freeze & Shutdown · 4 Impact vs. Intention · 5 Perception vs. Fact · 6 Control vs. Influence · 7 Accountability vs. Blame · 8 Ownership vs. Defense.
**Format:** Per track: Core Connection → Environmental Translation → Recognizable Scenario → Seven-Step Application → Accountability/Boundary checks.
**Documented status:** Complete, but **undocumented** — the folder `README.md` never mentions this set, so a reader cannot tell which set is canonical or how the two sets relate.
**Relationship to other lanes:** Overlaps Lane C's topics in participant-facing form, adapted per delivery setting. **Unresolved:** whether this set supplements, replaces, or duplicates Lane C; whether the four tracks are intended as alternative versions or as setting-specific supplements to the 16 core lessons.

---

## Lane E — Participant workbooks

**Location:** `docs/participant-workbooks/` (`README.md` + `Workbook_Lessons_01_04.md`, 24 KB).
**Audience:** Participants (practical application layer for the core spine: Recognize → Name → Explain → Separate → Interrupt → Practice → Carry It, plus self-assessment scales).
**Numbering scheme:** Batches keyed to Lane C lesson numbers: `Workbook_Lessons_01_04.md` = lessons 1–4.
**Actual coverage:** Batch 1 (lessons 1–4) present. Batch 2 (`Workbook_Lessons_05_08.md`) and batches for lessons 9–16 are missing.
**Documented status:** The `README.md` status table says `Workbook_Lessons_01_04.md` is "Pending approved content" and will be added when supplied — but the file **exists** (added 2026-08-22). The README is stale. Batch 2 is listed as "Pending Batch 1 verification."
**Relationship to other lanes:** Implementation layer for Lane C (the 16 core lessons). Pairing with the Lane D four-track lessons is undocumented.

---

## Lane F — Facilitator execution guides

**Location:** `docs/facilitator-guides/` (`Facilitator_Guide_Lessons_05_08.md` only).
**Audience:** Facilitators (execution matrix for the core lessons).
**Numbering scheme:** Guides keyed to Lane C lesson numbers.
**Actual coverage:** Only the lessons 5–8 guide exists. **The lessons 1–4 guide is missing.**
**Documented status:** Draft-state Phase 3 execution matrix; incomplete coverage.
**Relationship to other lanes:** Supports Lane C delivery. No equivalent guide layer exists for Lanes A, B, or D.

---

## Lane G — Historical imports (`archive-imports/`)

**Location:** `archive-imports/` — 8 predecessor-source directories.
**Audience:** Internal / remediation reference only. **Not part of the current curriculum structure.**
**Actual coverage:** `What-Really-Happened` (facilitator-manual.md), `What-Really-Happened-Manual` (IMPORT-INVENTORY.md), `What-Really-Happened-The-True-Story` (README.md, WRH_FULL_PILOT_MANUAL.md, Plan_B_Wallet_Cards.md), `archive-ready-repos` (CPTSD-STRAIGHT-FACTS-AND-LESSON-COLLECTION.md), `cptsd-education-portal` (IMPORT-INVENTORY.md), `thin-shell-repos` (IMPORT-INVENTORY.md), `what-really-happened-site` (README.md, Sample-Sessions_Crisis-Protocol.md), `wrh-master-platform` (IMPORT-INVENTORY.md). Four of eight carry `IMPORT-INVENTORY.md` provenance notes; all are marked historical, not current structure.
**Documented status:** Historical material preserved for consolidation reference. Good provenance hygiene — each source states what it was and its status.
**Relationship to other lanes:** Predecessor material only; must not be treated as current structure or delivery content.

---

## Supporting infrastructure

| Component | Location | Audience / role |
|---|---|---|
| Release-control docs | `docs/EVIDENCE_BASE.md` (placeholder, not a register), `docs/SAFETY_AND_ESCALATION.md`, `docs/DEPLOYMENT_CHECKLIST.md`, `docs/IMPLEMENTATION_GUIDE.md`, `docs/OUTCOMES_AND_MEASURES.md`, `docs/ACCESSIBILITY.md`, `docs/ARCHITECTURE_STANDARD.md` | Internal / remediation |
| Legacy architecture docs | `docs/Curriculum-Architecture/` (11-lecture public-education sequence, 12-session rhythm) | Historical reference |
| Commercialization layer | `docs/executive/` (brand, buyer, deployment, federal, identity, program, sales systems + navigation + document hierarchy) | Internal / buyer-facing |
| Part-IV operational layer | `Part-IV/Crisis_Package.md`, `Protocols_and_Reporting.md`, `Adverse_Event_Reporting.md`, `adverse_events_template.csv`, `Certification_Path.md`, `Facilitator_Prerequisites.md`, `Compliance_and_Risk_Management.md`, `Safety_Language_Template.md`, `field-card.md`, `IP_and_Usage_Rights.md`, `Pricing_and_Tiers.md`, `Delivery_Tier_Implementation.md`, `Administrative_and_Checklist.md`, `Glossary.md`, `Facilitator-Toolkit/`, `Participant-Materials/`, `Glossary/`, `Staff-Tools/` | Facilitators / internal — note: certification and federal-alignment claims in `Certification_Path.md` and `IP_and_Usage_Rights.md` §5.0 are unsupported (no board charter or agency records in the repo) |
| Public site | Root `index.html`, `curriculum/`, `public-site/`, `resources.html`, `start-here.html`, etc. — session explorer withdrawn (`assets/data/sessions.json` gutted to withdrawn stub) | Public (informational only, delivery withheld) |
| Build tooling | `scripts/build_session_catalog.py` (now outputs the withdrawn stub) | Internal |

**Index gaps in Part IV:** `Part-IV/index.md` does not link `Facilitator-Toolkit/`, `Participant-Materials/`, `Glossary/`, `Staff-Tools/`, `Compliance_and_Risk_Management.md`, `Facilitator_Prerequisites.md`, `Safety_Language_Template.md`, or `field-card.md` — they are discoverable only by browsing the tree.

---

## Lane relationship summary

| Lane | Location | Audience | Numbering | Coverage verified | Status |
|---|---|---|---|---|---|
| A. Master sessions | `Part-I/`–`Part-IV/` | Facilitators | `Session_NN_*`, 01–76 | 76 sessions + 1 portal page | v5.0 "Stabilized"; retained for preservation/remediation |
| B. New-system rewrite | `new-system/` | Facilitators | `session-NN`, `handout-NN` (independent) | 14 scripts, 13 handouts (sessions 01–14 only) | In rewrite; sessions 15–76 missing |
| C. Core participant lessons v2.0 | `docs/core-curriculum/lesson-*` | Participants | `lesson-NN`, 01–16 | 16/16 | Complete |
| D. Four-track lessons | `docs/core-curriculum/Lesson_*` | Participants (4 tracks) | `Lesson_NN`, 01–08 | 8/8, each with 4 track sections | Complete but undocumented |
| E. Participant workbooks | `docs/participant-workbooks/` | Participants | Batches keyed to Lane C | Batch 1 only (lessons 1–4) | Incomplete; README stale |
| F. Facilitator execution guides | `docs/facilitator-guides/` | Facilitators | Keyed to Lane C | Lessons 5–8 guide only | Incomplete; 1–4 guide missing |
| G. Historical imports | `archive-imports/` | Internal / remediation | Predecessor | 8 source directories | Historical; not current structure |

---

## Unresolved authority questions (owner decisions needed)

Nothing below is decided by this map. Each requires an explicit owner decision, recorded in writing:

1. **Which lane is canonical for facilitator delivery?** Lane A (v5.0 master scripts, complete 76) or Lane B (new-system rewrite, standardized format, only sessions 01–14)? `new-system/README.md` describes old-as-map / new-as-delivery-system but does not bind the repo and ignores Lanes C–F.
2. **Which participant line is authoritative?** Lane C (16 core lessons), Lane D (8 four-track lessons), and Lane E (workbooks) overlap without a documented relationship — supplement, replace, or duplicate?
3. **Numbering fix for Lane B:** renumber the rewrite lane (e.g., `NS-` prefix) vs. correct the handout numbering vs. keep both and publish a content-verified concordance. Master session numbers must be frozen as the reference numbering.
4. **Session-count labeling:** "76 sessions + 1 portal page" vs. "77-session" — pick one definition and apply it everywhere (`_config.yml`, session footers, `IP_and_Usage_Rights.md`).
5. **Index and link repairs:** stale `new-system/README.md` folder structure, stale `new-system/SESSION-INDEX.md` (session 14), stale `docs/participant-workbooks/README.md` status table, dead presentation-deck link in `Session_12_Pilot_Portal.md`, undocumented Lane D in `docs/core-curriculum/README.md`, Part-IV index orphans, visible TEMPLATE — DO NOT DELIVER UNFILLED headers on unfilled safety-adjacent fields.
6. **Unsupported authority claims:** `Certification_Path.md` and `IP_and_Usage_Rights.md` §5.0 must either be supported with records or relabeled draft/aspirational (also tracked in `docs/REMEDIATION_TRACKER.md`, Gates 1 and 4).
7. **License posture:** CC BY-NC 4.0 root `LICENSE` vs. All-Rights-Reserved session footers and `IP_and_Usage_Rights.md` — requires documented legal review (also tracked in `docs/REMEDIATION_TRACKER.md`, Gate 2).

---

*Map maintenance: regenerate counts from directory listings when files change; never trust READMEs alone. This map does not pass any release gate (see `docs/REMEDIATION_TRACKER.md`).*
