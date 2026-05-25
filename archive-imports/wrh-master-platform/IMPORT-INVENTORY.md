# Import Inventory: WRH Master Platform

Source repository: `Mave9055/wrh-master-platform`

Review date: 2026-05-25

Status: **valuable, but split across destinations**

This repo is not a thin shell. It contains business, procurement, capability, roadmap, and past-performance material. Most of that content should not be merged directly into the master curriculum repo because it belongs in the company/business system.

## Files Reviewed

- `README.md`
- `CAPABILITY_STATEMENT.md`
- `CONTRACTOR_READINESS_GAP_ANALYSIS_2026-04-14.md`
- `PAST_PERFORMANCE_TEMPLATE.md`

## What It Contains

### Business / Procurement Material

- capability statement
- government readiness roadmap
- federal identifiers and contracting data block
- NAICS / PSC positioning
- service language
- readiness checklist
- pilot evidence-generation plan
- past-performance narrative template

Recommended destination:

- `Mave9055/capitol-contracts`

### Curriculum / WRH Material

- WRH master platform framing
- Wounded Blueprint / pattern-recognition positioning
- Plan B protocol reference
- pilot structure references
- facilitator standardization references

Recommended destination:

- `Mave9055/wrh-master-curriculum` for curriculum framing only
- `Mave9055/WRH-Pilot-Deployment-Package` for pilot implementation references

## Split Decision

| Material | Destination |
|---|---|
| Capability statement | `capitol-contracts` |
| contractor readiness roadmap | `capitol-contracts` |
| federal data block | `capitol-contracts` |
| past-performance template | `capitol-contracts` and/or `WRH-Pilot-Deployment-Package` |
| Wounded Blueprint concept | `wrh-master-curriculum/docs/` |
| Plan B reference | already harvested into `Part-IV/Participant-Materials/PLAN-B-HANDOUT.md` |
| pilot evidence-generation language | `WRH-Pilot-Deployment-Package` |

## Important Correction Needed Before Public Reuse

The capability statement in the source repo identifies Daniel as CEO. Current company-positioning guidance should keep the majority owner / CEO role aligned with Capitol Contracts' ownership and control structure.

Before reusing any capability statement language publicly, verify title and control language against the current business structure.

## Do Not Blindly Merge

Do not import the entire repo into `wrh-master-curriculum`.

Reason:

- the curriculum repo should remain instructional
- the company repo should hold procurement and business materials
- the pilot repo should hold implementation and evidence-generation material

## Recommended Final Action

After harvesting useful business documents into `capitol-contracts` and useful pilot references into `WRH-Pilot-Deployment-Package`, the source repo can be archived or redirected with a README pointer.
