# WRH Curriculum Map

**Status:** Development inventory; every collection remains withdrawn from delivery under [PUBLIC_RELEASE_STATUS.md](PUBLIC_RELEASE_STATUS.md). No collection is declared canonical, approved, or clinically reviewed by this map.

**Scope:** File counts reflect the Phase 1 branch. Presence and headings establish inventory, not completeness, readability, efficacy, or delivery readiness. The original Phase 1 contributor reported full reading of the 14 rewritten scripts and 13 handouts; the [concordance](new-system/CONTENT_CONCORDANCE.md) records those proposed pairings. This is not a full content review of the 76 master sessions.

## Collections and relationships

| Lane | Location | Audience | Coverage present | Status and relationship |
|---|---|---|---|---|
| A. Master sessions | `Part-I/` through `Part-IV/` | Facilitator source | 76 numbered scripts plus one Session 12 portal | Preservation/remediation source. Not an approved delivery package. |
| B. Rewrite | `new-system/sessions/`, `new-system/handouts/` | Facilitator scripts; participant handouts | 14 scripts, 13 handouts | Working rewrite with an independent sequence; does not cover every master session. See concordance for topic pairings. |
| C. Lowercase participant lessons | `docs/core-curriculum/lesson-*.md` | Participants | 16 lesson files | Draft participant sequence. Relationship to Lane D requires owner decision; shared numbers do not imply shared topics. |
| D. Capitalized four-track lessons | `docs/core-curriculum/Lesson_*.md` | Participants in Corrections, Reentry, Veteran, Workplace tracks | Eight files, four track sections per file | Distinct eight-topic sequence. Topic coverage differs from Lane C. |
| E. Participant workbook | `docs/participant-workbooks/Workbook_Lessons_01_04.md` | Participants | Lessons 1–4 source exists; 5–8 workbook absent | Its lesson titles match Lane D's first four topics. Formal association, setting applicability, and fidelity remain unapproved. It cannot be assigned to Lane C by number alone. |
| F. Facilitator guide | `docs/facilitator-guides/Facilitator_Guide_Lessons_05_08.md` | Facilitators | Lessons 5–8 guide exists; 1–4 guide absent | Its lesson titles match Lane D's last four topics. This establishes topic correspondence, not approval or full content equivalence. |
| G. Historical imports | `archive-imports/` | Internal research/remediation | Eight predecessor directories | Historical source collection. Four directories contain `IMPORT-INVENTORY.md`; provenance and content depth vary. Not a current delivery package. |

### Master session count

| Part | Numbered sessions | Additional portal |
|---|---|---|
| I | 01–26 (26) | `Session_12_Pilot_Portal.md` |
| II | 27–56 (30) | None |
| III | 57–75 (19) | None |
| IV | 76 (1) | None |

Total: **76 numbered sessions + 1 portal page**. Phase 1 corrected the earlier 77-session labels in `_config.yml`, `curriculum/index.html`, and `site.webmanifest`. A portal is not an additional numbered session.

### Distinct participant topic sequences

| Lesson | Lane C: lowercase sequence | Lane D: four-track sequence |
|---|---|---|
| 1 | What Is a Survival Response? | What Is a Survival Response? |
| 2 | When Your Body Reacts Before You Can Think | Safety vs. Familiarity |
| 3 | Fight, Flight, Freeze & Shutdown | Fight, Flight, Freeze & Shutdown |
| 4 | Understanding Dissociation | Impact vs. Intention |
| 5 | The Threat Loop | Perception vs. Fact |
| 6 | Why Patterns Repeat | Control vs. Influence |
| 7 | Why Knowing Better Doesn't Always Mean Doing Better | Accountability vs. Blame |
| 8 | Shame, Avoidance & the Reinforcement Loop | Ownership vs. Defense |

Lane C also has lessons 9–16. No owner decision establishes an obligation to extend Lane D to sixteen lessons.

### Rewrite pairings

Rewritten Session 10 introduces bodily signaling; no handout for that topic exists in the 13-handout collection. Rewritten Session 13 pairs topically with handout 10 (dissociation), and rewritten Session 14 with handout 13 (noncompliance misclassification). Files have not been renamed; use the [content concordance](new-system/CONTENT_CONCORDANCE.md), not matching numbers.

Rewritten Session 10 has no same-title counterpart in the master inventory. This filename/title check does not establish that the topic is absent from every master session. Master Session 14 (a second dissociation topic) has no identified rewrite counterpart in the 01–14 rewrite set. The rewrite's count is not a 14-of-76 one-to-one coverage measure.

## Supporting infrastructure

- [Part IV index](Part-IV/index.md): withdrawn operational source, safety templates, certification/pricing/IP drafts, facilitator resources, participant materials, glossary, and survey. Directory resources are linked to individual files; index inclusion does not authorize use.
- [Evidence status and schema](docs/EVIDENCE_BASE.md), [starter register](docs/EVIDENCE_REGISTER.md), [release tracker](docs/REMEDIATION_TRACKER.md), and [licensing questions](docs/LICENSING_ISSUES.md): internal remediation records, not approval evidence.
- `docs/executive/`: internal/commercial source documents. Their agency, certification, and sales assertions require review; this map does not verify them.
- `docs/Curriculum-Architecture/`: predecessor architecture reference; its authority relative to current collections is unresolved.
- Public information pages and the withdrawn explorer/catalog remain under the existing release controls. No participant delivery package is restored.

## Completed Phase 1 documentation repairs

The rewrite README/index now list the existing 14 scripts and 13 handouts; the workbook README distinguishes source presence from approval; the core README distinguishes the two participant sequences; Part IV resources are linked; the nonexistent deck link is neutralized; selected safety templates are visibly withdrawn. These repairs do not complete any release gate. Workbook/guide associations above correct an erroneous Lane C assignment in the imported Phase 1 map.

## Owner and independent-review decisions still required

1. Choose the future facilitator reference lane and its relationship to the master inventory; no delivery authority is implied.
2. Define whether the two participant sequences supplement, replace, or serve different purposes from each other.
3. Confirm workbook/guide associations and required content alignment, beyond the title correspondence recorded here.
4. Choose whether to rename handouts or retain a documented concordance; decide how a missing bodily-signaling handout will be handled.
5. Decide Session 20's disposition after independent clinical review.
6. Supply supporting records for certification/agency claims, or retain unapproved-draft labels and commission appropriate revision/review.
7. Resolve forward licensing scope and prior distribution history with qualified legal review.
8. Define intended delivery settings, audience separation, version manifest, reviewer responsibilities, and the eventual version-specific release decision.

**Catalog regeneration control:** The inherited catalog builder previously serialized master-session source despite the empty checked-in catalog. The Phase 1 follow-up changes ordinary catalog builds to emit only the withdrawn stub; two regression tests cover clean builds and replacement of a populated catalog. The checked-in catalog and explorer remain unchanged. This closes a regeneration path, not a release gate.

**Gates satisfied: 0 of 6.** See the [release tracker](docs/REMEDIATION_TRACKER.md).
