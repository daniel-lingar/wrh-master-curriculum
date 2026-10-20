# Phase 3 import verification

**Status: DOCUMENT AND SOURCE-INTEGRITY AUDIT ONLY — NO RELEASE APPROVAL.** Baseline: `9ee354b42f622dcdc789f017ca8dc189bb649f0c`. This audit checks the supplied artifacts; it does not attest to the submitting readers' activity, certify exhaustive extraction, validate every triage judgment, or investigate the scientific claims.

## Transfer and history

| Artifact | Verified SHA-256 |
|---|---|
| ZIP archive | `231c3833c5fdea52dc68b6f1869fa9d29cf08daa2cb875df1014b6f92472dff0` |
| Patch 0001 | `e378c41c051278b1c173fc2df1f6c8a6b866efffbe6014b4d23be5b900a0e0fd` |
| Patch 0002 | `b743e874d888d1852393fd8ee3c723a164cb19e7caed5d3898b67024b41e7dff` |

Both patches applied cleanly to the exact baseline, reproducing the declared tree `5d2fb59d719df2e590f9f7db2bc002ac08b8df4f`. Two imported commits preserve that content; a separate correction commit records repairs. GitHub connector publication creates different commit metadata/IDs; published trees must match their locally audited counterparts.

## Counts and quotation checks

All 1,067 submitted citations matched their cited text with whitespace normalized, but this check missed 223 duplicate citations in 179 entries. Deduplication uses the actual source character span within each entry, rather than equality of line-range labels. Removing those duplicates and adding 133 previously unlisted exact-wording matches in eight existing entries yields **977 entry-location records**, 782 new entries, and 797 total entries. No register entry IDs or quotation wording were changed.

All 977 final records match the baseline; 976 contain the quotation without whitespace normalization, and one multiline quotation matches with whitespace normalized. No same-entry duplicate source spans remain. A scan for already-inventoried quote strings across all 76 numbered sessions and Crisis Package finds no unlisted exact-wording matches. That bounded check cannot discover claims whose wording has not been inventoried, establish equivalent meaning across contexts, or certify exhaustive extraction. Different entries can overlap a passage.

All 78 ledger hashes match: 76 numbered sessions, Crisis Package, and portal. Line counts on the 73-session table match. ER-001–015 remain byte-identical. Every new entry retains seven fields, uninvestigated status, and pending reviewer and revision fields. Priority, kind, and tag totals were recomputed without endorsing individual classifications.

## Reference repairs

Each reference was checked against its described session and quotation:

| Session | Stale preliminary ID(s) | Final ID(s) |
|---|---|---|
| 04 | 031 | 043 |
| 08 | 058 / 039 | 057 (same wording in both sessions) |
| 11 | 078 | 112 |
| 24 | B2-95 | 222 |
| 32 | 211 | 303 |
| 41 | 272 / 274 | 392 / 394 |
| 56 | 360 | 524 |
| 63 | 422 | 621 |
| 64 | 432 / 433 / 434 | 636 / 638 / 641 |
| 65 | 441 / 442 / 443 | 653 / 655 / 658 |
| 66 | 451 / 452 / 453 | 669 / 671 / 674 |

The proposed-actions epigenetics goal is ER-022, not ER-016. Identical wording is now a navigation grouping, not proof of identical meaning or applicability. Session 37's heading is an attribution-review question without an unverified exact-book-title allegation. Findings and tracker qualify completeness and reading claims to what this audit establishes.

## Reproduction and protected content

From a checkout containing the baseline Git object:

```bash
python docs/verification/verify_phase3_inventory.py
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/build_session_catalog.py
git diff --check
```

The checker verifies the properties above and rejects modifications outside the allowed Phase 3 review-document paths. The two existing tests pass; the actual catalog builder produces the unchanged withdrawn JSON (`count: 0`, empty sessions, withdrawn status). This proves preservation relative to Phase 2, not approval or safety of earlier content. No full site build or deployment check was performed. No clinical, legal, accessibility, or site reviewer decision is recorded. **Zero of six release gates are satisfied.**
