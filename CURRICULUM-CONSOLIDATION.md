# WRH Master Curriculum Consolidation Map

This repository is the source of truth for the **What Really Happened (WRH) Master Curriculum**.

Older curriculum, lecture, presentation, portal, and education-site repositories should be reviewed, harvested for useful files, and consolidated here only when they strengthen the master structure.

## Purpose of This Repo

`wrh-master-curriculum` should hold the complete WRH instructional system:

- 75-session curriculum architecture
- session sequence and lesson files
- facilitator scripts and delivery standards
- participant materials
- staff tools and decision guides
- glossary / vocabulary system
- implementation documentation
- scope boundaries and non-clinical usage language
- curriculum-adjacent public-site assets only when they support the master curriculum

This repo should not become a junk drawer. It is the organized master system.

## Official Destination Structure

Use this structure as the target when importing useful files from older repositories.

```text
wrh-master-curriculum/
  Part-I/
    Sessions 1-26: Laws of Survival / System Logic Map
  Part-II/
    Sessions 27-56: Core Operational Journey / Pilot Program
  Part-III/
    Sessions 57-75: Advanced System Specialization
  Part-IV/
    Facilitator Toolkit
    Staff Tools
    Participant Materials
    Glossary
    Commercial / Procurement Materials
  docs/
    Scope Boundaries
    Implementation Notes
    Curriculum Architecture
    Quality / Fidelity Notes
  public-site/
    Optional site assets supporting the curriculum
  archive-imports/
    Temporary holding area for reviewed legacy material
```

## Repositories to Consolidate Into This Repo

| Source Repo | Action | Destination |
|---|---|---|
| `trauma-recovery-curriculum` | Review and import any session, framework, or participant material | `Part-I`, `Part-II`, `Part-III`, or `Part-IV/Participant Materials` |
| `cptsd-education-portal` | Review for public education pages and glossary material | `public-site/` or `Part-IV/Glossary` |
| `cptsd-presentation-web` | Review for slides, speaking structure, or visual explanation assets | `Part-IV/Facilitator Toolkit` or `docs/` |
| `betalectures` | Review for lecture drafts and usable sequence logic | `Part-IV/Facilitator Toolkit` or session folders |
| `What-Really-Happened-Manual` | Review for manual language, definitions, facilitator standards | `Part-IV/Facilitator Toolkit`, `docs/`, or `Part-IV/Glossary` |
| `CPTSD-Straight-Facts` | Review for plain-language explanation blocks | `docs/` or `Part-IV/Participant Materials` |
| `lesson-collection-site` | Review for individual lessons and learning-objective material | session folders or `archive-imports/` |
| `wrh-portal` | Review for navigation/site shell ideas only | `public-site/` if still useful |
| `wrh-master-platform` | Review for platform language and structure | `docs/` or `public-site/` |

## Import Rules

1. **Do not import duplicates just because they exist.**
2. **Import only files that improve the master curriculum.**
3. **Keep source attribution in commit messages or import notes.**
4. **Separate curriculum from company/business material.** Business-facing material belongs in `capitol-contracts` or the pilot package unless it directly explains the curriculum.
5. **Separate full pilot delivery from master curriculum.** Field-ready pilot materials belong primarily in `WRH-Pilot-Deployment-Package`; only shared framework pieces should live here.
6. **Keep private/personal research out of this repo.** Investigation, dossier, OSINT, and personal archive material should not be imported here.
7. **Do not delete or archive a source repo until useful content has been checked.**

## What Belongs Here

Good fit:

- session files
- facilitator scripts
- scope boundaries
- glossary terms
- diagrams explaining WRH mechanisms
- staff decision tools
- plain-language curriculum definitions
- sequence maps
- fidelity/quality-control notes

Poor fit:

- personal disputes
- legal/investigation files
- gambling/sweepstakes experiments
- unrelated business brands
- unfinished AI-generated shells
- duplicate websites with no unique curriculum value
- book-production exports that belong in the book repo

## First Consolidation Pass

The first pass should not move everything. It should identify and preserve the best material.

### Pass 1: Inventory

For each source repo:

- Check README and top-level folders.
- Identify unique files worth saving.
- Mark whether the repo should be merged, archived, renamed, or ignored.

### Pass 2: Import

Move useful files into one of these places:

- `Part-I/`
- `Part-II/`
- `Part-III/`
- `Part-IV/`
- `docs/`
- `public-site/`
- `archive-imports/<source-repo-name>/`

### Pass 3: Clean Up

After useful content is protected:

- update the source repo README with a pointer to `wrh-master-curriculum`, or
- archive the source repo, or
- delete only if it is empty/no longer useful and there is no reason to preserve history.

## Current Decision

This repo remains the master curriculum home.

The pilot package remains separate.

The company repo remains separate.

The memoir/book production repos remain separate.

That separation keeps the public system understandable.