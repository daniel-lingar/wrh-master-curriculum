# WRH Master Curriculum — Licensing Issues Note

**Date:** 2026-10-19 (WRH Phase 1 Repository Remediation)
**Scope:** This note documents the licensing conflict observed in this repository. It changes nothing: the root `LICENSE` and all existing licensing terms are untouched. This is a factual record for qualified legal review — it contains **no legal conclusions**.

## 1. The conflict as observed

Two incompatible licensing postures coexist in this repository:

1. **Root `LICENSE` (CC BY-NC 4.0):** The repository-root `LICENSE` file grants a **Creative Commons Attribution-NonCommercial 4.0 International** license — permitting sharing, redistribution, remixing, and adaptation for non-commercial purposes with attribution. (Added in commit `5d686c4`, "Add CC-BY-NC-4.0 LICENSE for WRH Master Curriculum".)
2. **"All Rights Reserved" session footers and proprietary claims:** Ninety-five (95) Markdown files outside `new-system/` carry footers such as:
   > *Proprietary Intellectual Property of Capitol Contracts LLC. All Rights Reserved.*
   
   Additionally, `Part-IV/IP_and_Usage_Rights.md` asserts that the curriculum is the "exclusive and proprietary intellectual property of Capitol Contracts LLC," that "all rights… are expressly reserved," and grants only a "limited, non-exclusive, non-transferable, and revocable license" to institutional purchasers — with restricted redistribution, content-integrity, and non-commercial-use conditions that conflict with the CC BY-NC 4.0 permissions.

These postures are unreconciled: one invites broad non-commercial reuse, the other forbids redistribution and reserves all rights to a single company.

## 2. Affected files / categories

| Category | Count / location | Assertion present |
|---|---|---|
| Part-I session files | 28 files | "All Rights Reserved" footer |
| Part-II session files | 31 files | "All Rights Reserved" footer |
| Part-III session files | 20 files | "All Rights Reserved" footer |
| Part-IV documents | 15 files (including `index.md`, `field-card.md`, Session 76, `IP_and_Usage_Rights.md`, `Glossary.md`, `Pricing_and_Tiers.md`) | "All Rights Reserved" footer |
| `archive-imports/what-really-happened-site/` | 1 file | "All Rights Reserved" footer |
| Root `LICENSE` | 1 file | CC BY-NC 4.0 grant |
| `docs/REMEDIATION_TRACKER.md` (lines 52, 56, 180) | 1 file | Already flags this conflict as an unresolved Gate 2 item requiring legal review |

## 3. Note on Creative Commons irrevocability

Creative Commons licenses are **irrevocable for recipients who received the material while the CC license was valid and remain compliant with its terms**. This is a factual property of the CC BY-NC 4.0 license, stated for awareness only:

- Removing or replacing the root `LICENSE` (or deleting the repository) would **not** retroactively revoke the permissions already granted to compliant recipients of versions distributed under the CC license.
- Any future change to the licensing posture can only govern **newly distributed** versions; it cannot claw back permissions that compliant earlier recipients already hold.

No legal conclusion is drawn about which recipients, versions, or uses are covered — that is a question for legal review.

## 4. Questions requiring qualified legal review

1. Which licensing posture — CC BY-NC 4.0 or the "All Rights Reserved" proprietary regime — reflects the owner's actual intent, and what should govern future distribution?
2. What is the full distribution history of CC-licensed versions of this repository (public site, GitHub releases, forks, clones), and which permissions survive for prior recipients under the CC irrevocability rule?
3. Are the "All Rights Reserved" session footers and `IP_and_Usage_Rights.md` proprietary claims enforceable as written, given the contemporaneous CC BY-NC 4.0 grant at the repository root?
4. What consistent labeling should appear across the root `LICENSE`, session footers, and `IP_and_Usage_Rights.md` once the intent is settled — and who has authority to make that change?
5. Are there any third-party rights, trademark registrations, or existing institutional licenses (e.g., to federal purchasers) that constrain the resolution?

## 5. Status

This conflict is tracked as an unresolved **Gate 2** item in `docs/REMEDIATION_TRACKER.md`. No licensing terms were modified during this remediation pass.
