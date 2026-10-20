# WRH Phase 3 — Findings Report: Complete Master-Session Reading and Claim Inventory

**Branch:** `review/wrh-claim-inventory-phase3` · **Baseline:** `9ee354b42f622dcdc789f017ca8dc189bb649f0c` (verified Phase 2 head; draft PR #3 unmerged at time of branching; Phase 3 stacks against `review/wrh-evidence-phase2`). Do not merge. Nothing in this phase constitutes clinical approval, legal clearance, or delivery readiness.

## What this phase is

A completed **reading inventory** of the numbered master sessions, producing an expanded claim register whose new entries carry **verified quotations and no evidence conclusions**. It is distinct from completed evidence verification: Phase 3 entries are marked "not investigated in Phase 3" and must not be read as supported, unsupported, theoretical, or disproven.

## Coverage (exact)

- **73 numbered master sessions read in full in Phase 3:** Sessions 02–19 and 21–75 (Part-I, Part-II, Part-III). See [PHASE3_READING_LEDGER.md](PHASE3_READING_LEDGER.md) for per-session path, baseline blob hash, line count, reader batch, prelim-verification counts, and findings.
- **Gap scan (full-text re-read)** of Sessions 01, 20, and 76 and `Part-IV/Crisis_Package.md`, which had only targeted Phase 2 coverage. Cross-reference of ER-001–015 against the original baseline `e6d350e4300d2fa10a10db15b44a56e3d770eb9c`: **15 of 15 quotations confirmed verbatim.** Two line-reference discrepancies were found in the existing register and are recorded below; ER-001–015 were preserved unchanged per the phase instructions.
- **Not read in this phase:** the `new-system/` rewrite, core participant lessons, workbooks, facilitator guides, Part IV operational documents, historical imports, and the Session 12 pilot portal's claim content (the portal was read for characterization only; see ledger).
- With Phase 2's targeted reading, **all 76 numbered master sessions have now been read in full across Phases 2–3.** That sentence is the full extent of the coverage claim.

## Inventory counts

- Preliminary unverified worklist (local branch `review/wrh-full-read-phase3`; treated as a worklist only, never as a source of truth): 526 entries. Re-verification against the baseline: **525 verified verbatim, 1 corrected** (Session 11, lines 84–87: the worklist had flattened four separate lines into one string; the corrected line-by-line form is inventoried), **0 not found**.
- New claims found by the full read beyond the worklist: **263** in the 73 sessions, **29** in the Sessions 01/20/76/Crisis Package gap scan — **292 new claim records** in total.
- Claim records processed: **818**. Grouped by identical verbatim wording (meaning and scope genuinely matching; every occurrence retained; near-identical variants kept separate): **782 new register entries, WRH-ER-016–WRH-ER-797**, representing **1,067 inventoried occurrences**. 186 entries have more than one occurrence.
- By inventory priority: **P1 = 255, P2 = 445, P3 = 82.**
- By kind: empirical-assertion 525, pedagogical-framing 140, metaphor-implied-mechanism 70, normative-guidance 36, lived-experience 8, metaphor-no-mechanism 3.
- Notable families (entry counts; occurrence counts): "one second of air" refrain 53/132; "somatic markers of this law" 21/43; Anchor protocol scripts 3/67; 23 safety-instruction entries; 36 numerical; 129 treatment-effect; 109 diagnostic; 177 universal-deterministic.

## Research actually completed

**No external source was inspected in Phase 3** — no web search, no literature retrieval, no guideline review. The research work of this phase is verification of the inventory itself:

1. **Quotation verification (programmatic):** all 1,067 occurrence quotations were checked as verbatim (whitespace-normalized) substrings of their cited baseline lines. Result: **1,067/1,067 passed, 0 failures.** Script: `phase3-scratch/verify_quotes.py` (not committed).
2. **Blob integrity:** all 76 numbered session files were compared blob-by-blob between the original baseline `e6d350e` and the Phase 3 baseline `9ee354b`: 74 of 77 session-related files byte-identical; only Session 20, Session 76, and the pilot portal differ (Phase 1 warning/link repairs). Session 01 is byte-identical, so Phase 3 line numbers for the 73 sessions and Session 01 are directly comparable with ER-001–015's numbering.
3. **Line-anchor spot checks on hosted GitHub:** the sampled blob URLs at the Phase 3 baseline returned HTTP 200 for Session 01 and for the Crisis Package (pattern-identical URLs serve the rest).
4. **Register-internal cross-references:** where a Phase 3 quote is a substring of an ER-001–015 quote or vice versa, field 2 names the related entry.
5. **Regression tests:** the two catalog-withdrawal tests pass (`Ran 2 tests ... OK`). Running the actual catalog builder produced the unchanged withdrawn catalog (`count: 0`, `status: withdrawn_pending_independent_review`); the checked-in catalog file is byte-identical before and after.
6. **Diff review:** changed vs baseline: `docs/EVIDENCE_REGISTER.md` (appends + header note; ER-001–015 byte-identical) and five new documents — `docs/PHASE3_READING_LEDGER.md`, `docs/PHASE3_REVIEW_BACKLOG.md`, `docs/PHASE3_PROPOSED_EDITORIAL_ACTIONS.md`, `docs/PHASE3_FINDINGS_REPORT.md` (this file), and the updated `docs/REMEDIATION_TRACKER.md`. Zero changes to `LICENSE`, `PUBLIC_RELEASE_STATUS.md`, `curriculum/`, `scripts/`, `assets/`, all Part directories, and `new-system/`. `git diff --check` clean.

## Recorded line-reference discrepancies (ER-001–015 preserved as-is)

- **ER-009** related passage: stated line 159, actual line **157** at `e6d350e` (line 159 is "**Pause.**").
- **ER-008** stated range 109–113: the quoted passage is all on line 110 (line 109 is the section header, line 112 is "**Pause.**"); the range contains the quote but overstates its span.
- Both are recorded for a future correction decision; the entries were not edited in this phase per instruction.

## Coordinator judgment calls (for future review)

1. **UEI/CAGE footers** ("Proprietary Intellectual Property of Capitol Contracts LLC. All Rights Reserved. UEI: HH77KN5AV5X7 | CAGE: 9ZFJ6") on every session footer were inventoried once as a repeated element, not 76 register entries: identifiers are not empirical claims, and the substantive conflict is already tracked in `docs/LICENSING_ISSUES.md`.
2. **Mantras/affirmations** carried in the worklist were kept; the full read added no further pure normative-guidance lines (no factual assertion = outside the material-claim definition).
3. **Facilitator-purpose/structural lines** (e.g., "Mechanism Purpose" labels) were excluded as non-assertive metadata except where the wording itself asserts a claim (deterministic headings were included).
4. **Borderline narrative numbers** (e.g., remembered heart rates in the Architect narrative) were included with their narrative context; reviewers should expect borderline calls and re-examine them.
5. **Session 37's segment title** reproduces a well-known published book title without attribution in the file — flagged to the editorial queue, not asserted as plagiarism.
6. **Session 26's conclusion** missequences the curriculum ("Part III" next, skipping Part II) — a script inconsistency, not a claim.

## Limitations (what this phase does not establish)

- A full read is one pass; extraction judgments on borderline material are the coordinator's, recorded above.
- Reader agents worked in parallel batches; cross-batch consistency was enforced by scripted verification of every quotation, not by re-reading.
- Collections other than the numbered master sessions remain unin­ventoried; the portal's certification/compliance assertions await a future inventory.
- No accessibility assessment was performed (Gate 2 accessibility review remains outstanding).
- No independent reviewer has seen any of this; all reviewer fields are PENDING.

## Tracker status

Gate 1 (evidence register) remains `IN PROGRESS`: register coverage of the numbered sessions is complete **as an inventory**; no new entry has been evidence-verified. All other gate statuses unchanged. **Gates satisfied: 0 of 6. Delivery remains withheld.**
