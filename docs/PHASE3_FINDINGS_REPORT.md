# WRH Phase 3 — Master-Session Claim Inventory Findings

**Branch:** `review/wrh-claim-inventory-phase3`. **Baseline:** `9ee354b42f622dcdc789f017ca8dc189bb649f0c` (Phase 2 head; PR #3 unmerged at import). This is draft review material. Nothing here constitutes clinical approval, legal clearance, or delivery readiness. Do not merge or restore delivery access.

## Coverage and its limits

The submitting producer reports full-text reading of Sessions 02–19 and 21–75 (73 sessions), plus full-text gap scans of Sessions 01, 20, 76 and `Part-IV/Crisis_Package.md`. The [reading ledger](PHASE3_READING_LEDGER.md) records those activities, source paths, baseline hashes, and reader notes. The portal is a separate document, characterized but not claim-inventoried. The rewrite, participant lessons, workbooks, facilitator guides, other Part IV operational documents, and imports remain outside this inventory.

The receiving audit independently checked every ledger source hash and every new register quotation. It did not observe the seven reader batches, receive their transcripts or preliminary worklist, or repeat a full reading of all 76 sessions. **The ledger covers all numbered sessions; exhaustive extraction of every material claim has not been independently established.** Text matching cannot certify completeness or consistent interpretation across readers.

## Corrected inventory counts

- **797 register entries total:** ER-001–015 from earlier phases, preserved byte-identical; **782 new entries**, ER-016–797.
- **977 verified entry-location records** for the new entries. A record pairs one entry's quotation with one physical source location. Overlapping ranges pointing to the same text within an entry count once. Different entries can quote overlapping fragments of a passage, so this is not a count of independent claims or disjoint passages.
- **22** new entries have multiple recorded locations. All additional locations have immutable baseline links.
- Priorities, unchanged by locator repairs: **P1 255 / P2 445 / P3 82**. These are submitted triage judgments, not evidence findings.
- Submitted kinds: empirical-assertion 525; pedagogical-framing 140; metaphor-implied-mechanism 70; normative-guidance 36; lived-experience 8; metaphor-no-mechanism 3. Counts were recomputed; individual classifications were not independently validated.
- The “one second of air” family has **53 wording entries and 139 entry-location records covering 72 distinct literal phrase positions**. Shorter fragments overlap longer variants. The “somatic markers of this law” family has **21 entries / 22 locations**. Three Anchor instruction entries have **99 entry-location records**: ER-023 44, ER-278 27, ER-332 28; different instructions can share an opening.

## Import corrections

The original submitted tree is preserved in the first two commits. The follow-up audit found that all **1,067 submitted citations** contained their quoted text after whitespace normalization, but **223 citations in 179 entries counted the same physical text twice**, commonly a range ending at a quoted line plus a separate citation to that line. That left 844 entry-location records.

A scan of the already-inventoried quotation wording across the 76 numbered sessions and Crisis Package then found **133 unlisted exact-wording locations in eight entries**. These were added with baseline links: ER-023 +32, ER-030 +69, ER-096 +1, ER-099 +1, ER-133 +1, ER-134 +1, ER-260 +1, ER-332 +27. Their source contexts were checked for the same quoted instruction or assertion. Identical words still do not establish identical applicability or permit a review decision to transfer between contexts. Thus **1,067 − 223 + 133 = 977**. No new claim ID or evidence conclusion was created by these repairs.

Stale preliminary IDs in the reading notes were replaced with the corresponding final register IDs, checked against the quoted source and session. The proposals' epigenetics-goal reference was corrected to ER-022. Claims of an exact published-book-title match for Session 37 were replaced with an attribution-review question; this phase establishes no such match or infringement. The portal's hash was added to its ledger row.

## Producer-reported processing history

The producer reports a preliminary worklist of 526 entries (525 quotations verified, one Session 11 multiline quotation corrected), plus 292 additional input records (263 in the 73-session read and 29 in the gap scans), yielding 818 input records grouped into 782 new entries. Those are **reported historical processing counts**, distinct from the corrected location counts. The preliminary worklist and reader transcripts were not delivered, so the receiving audit cannot independently reconstruct that history. Preliminary identifiers have no authority in the final register.

## Verification and research actually performed

No external evidence investigation was performed for new Phase 3 claims. All remain **not investigated in Phase 3**, with independent reviewer and implemented-decision fields pending. The [import verification](PHASE3_IMPORT_VERIFICATION.md) and its reproducible checker record the receiving audit's narrower checks: baseline hashes, all quoted text and locators, same-entry duplicate detection, exact-wording repeat coverage, seven fields, IDs, preserved earlier entries, and protected-file comparisons.

The two existing catalog-withdrawal tests pass; the actual builder reproduces the checked-in empty catalog. All changes are review documentation. Session sources, participant material, crisis procedures, license, release restrictions, explorer, catalog, and builder remain byte-identical to Phase 2. No full site build, hosted-site audit, or qualified review was performed.

## Earlier line-reference observations

ER-001–015 remain unchanged. At original baseline `e6d350e4300d2fa10a10db15b44a56e3d770eb9c`, ER-009's related passage is at line 157 rather than its stated line 159, and ER-008's quoted text is on line 110 within the broader cited range 109–113. These are locator observations, not changes to the earlier scientific assessments.

## Review backlog and status

The [backlog](PHASE3_REVIEW_BACKLOG.md) separates clinical, legal, accessibility, site, and editorial review inputs; [editorial actions](PHASE3_PROPOSED_EDITORIAL_ACTIONS.md) remain unapproved proposals. Priority counts do not establish the correctness of every tag or risk judgment. Existing Session 20 blockers remain pending qualified review. All collections outside the inventory still require claim extraction; further missed claims may also remain inside the numbered sessions.

**Gate 1 remains IN PROGRESS. Gates satisfied: 0 of 6. Delivery remains withheld.**
