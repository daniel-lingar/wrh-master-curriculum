# Phase 4 receiving audit and development handoff

**Scope:** Patch/source integrity, selected primary-source checks, and correction of the development-status record. This is not independent clinical/legal/accessibility/site review, a systematic literature review, or approval of proposed wording.

## Transfer

| Artifact | Verified SHA-256 |
|---|---|
| ZIP | `0e74eb2902bcafcc911b022b57b79d5af01bb9d4742ecff26fdc41e178735a15` |
| Patch 0001 | `7e0065705cce9b5a6e9c56f27c2d436801d4b13e32455868fc52e71b16ecb514` |
| Patch 0002 | `6f4614e21a20e1ca330e5766a6cbd178d0695bd0a9aa4c6c5fe0715d58be67d3` |

The patches apply cleanly to `d4b3910f49e7e4420a4968b0bdd72783cf3b5210` and reproduce submitted tree `23599eba21c11cb69a391c96daa59a42ae1ffd08`. The original two commits are retained, followed by receiving-audit corrections. Connector publication changes commit metadata/IDs; published trees must match their corresponding audited local trees.

## Development choice and unfinished implementation

The later owner instruction delegated the package choice and authorized non-crisis drafting; it superseded the proposal-only package-selection restriction. The received archive still contained recommendations and proposals only. Its eight-topic Lane D recommendation is now recorded as the working development choice, with Lane E/F companion drafting roles, D-01…D-08 identifiers, and Lane C preserved as deferred source. This does not declare any audience/site suitable or approve delivery. Lane A, including Sessions 20 and 76 and the Crisis Package, remains withdrawn and outside the first package.

**Still missing:** `Workbook_Lessons_05_08.md` and `Facilitator_Guide_Lessons_01_04.md`. The eight lessons and existing companions remain baseline source; the authorized implementation has not been delivered in this archive. Muse can proceed with that delegated work without requesting the owner to choose the package again. Existing material also needs its own claim inventory, evidence-informed revisions, fidelity checks, and qualified review.

The scope comparison was qualified: existing Lane A toolkits are support material; filename/title differences do not prove topic absence; four track sections per Lane D topic prevent treating eight versus sixteen titles as a twofold review-effort difference. Unsupported numerical effort multipliers were removed. Missing companions are required before final package sign-off, not before any early consultation with reviewers.

## Selected source rechecks

Inspection below is the receiving audit's depth, distinct from the producer's reported inspection in the dossier. Other source records remain producer-reported and were not all independently revalidated.

| Source | Receiving inspection and bounded finding |
|---|---|
| [Szulczewski 2019](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218550) | Abstract, procedure, and relevant results. Six of sixteen healthy adults were below 30 mmHg during the day-1 ten-minute task. The study used four-second inhalation/six-second exhalation without a hold; WRH uses counts with an unspecified hold. This is a study-specific physiological observation, not a WRH harm rate or proof of the exact script's first-use effect. |
| [Balban et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873947/) | Abstract, daily pre/post results, discussion of acute effects, and eligibility/debriefing passages. The dossier's blanket exclusion of single-use effects was too broad: the study assessed daily acute changes as well as practice across a month. It does not establish first-use effects of a brief WRH group opener. The optional debriefing's negative-experience percentage is not a WRH adverse-event rate or complete harms surveillance. |
| [Torre & Lieberman 2018, article PDF copy](https://static1.squarespace.com/static/651b09f505bc433349d85ab7/t/651d2f2843e6d165beeccb23/1696411432954/Torre%25282018%2529ER.pdf) | Article identity, abstract, and Possible Mechanisms section. The speculative-mechanism characterization is present in this 2018 review. Its date matters: it does not by itself establish the state of all mechanism research in 2026. |
| [Nook et al. 2021](https://link.springer.com/article/10.1007/s42761-021-00036-y) | Abstract and selected methods. The reported naming-before-regulation findings concern aversive-image experiments, not a general verdict on naming or WRH delivery. |
| [Wolfe & Isaacowitz 2023](https://doi.org/10.1093/geroni/igad104.0112) | Publisher/PMC metadata and publisher abstract text exposed in search retrieval; repeated full-page retrievals were unreliable. This is an *Innovation in Aging* supplement abstract, 7(Supplement_1), 33–34, not an inspected full research report. The DOI and source type were added; it should not be given the same evidentiary weight as a fully assessed report. |
| [Ariely et al. 2026](https://link.springer.com/article/10.1007/s42761-026-00362-z) | Publisher abstract and metadata. Directional findings are reported for two image-viewing studies; the submitted preregistration assertion was not established by its abstract-only inspection and was removed. No allegation that the study was unregistered is made. |
| [Trask author publication list](https://www.trasklab.com/publications), [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC4943327/) | Author bibliography and PMC publication metadata retrieved in search; full PMC access was unreliable. The paper is Trask, Schepers & Bouton **2015**, *Revista Mexicana de Análisis de la Conducta*, 41(2), 187–210; PMC availability in 2016 is a separate date. The submitted year/journal were corrected. Animal operant-extinction findings do not directly falsify a person's speech/recovery narrative. |
| [Beutler et al. 2022](https://pubmed.ncbi.nlm.nih.gov/36340007/) | Published abstract exposed through official PMC/PubMed search retrieval. The producer inspected selected introductory full-text sections, not the whole review/results. That distinction is now retained in the proposals; no claim of full independent receiving inspection is made. |
| [VA/DoD PTSD index](https://www.healthquality.va.gov/guidelines/MH/ptsd/) | Official index page listing the 2023 guideline. This is a version-listing check, not an exhaustive currency search or a full guideline review. |

The proposals' claim that WRH borrowed terminology from Damasio was narrowed: shared terminology does not establish provenance or intent. The dossier already acknowledged that limit. A historical critique of somatic-marker theory also cannot, by itself, establish current scientific consensus. The proposed preservation of “It kept you alive” now acknowledges that it is an individual causal assertion as well as a narrative sentence. “Some people find it helps” remains an empirical benefit statement requiring support; conditional proposals do not validate it.

## Artifact and regression checks

The [Phase 4 checker](verification/verify_phase4_artifacts.py) verifies 26 immutable source URLs/ranges, all 25 representative proposal quotations, 13 proposal identifiers, 24 reported lesson line counts, and byte identity of the 260 protected baseline files. Four quotation presentations were repaired: one slash-joined three-line excerpt was split into separately pinned exact lines, and three passages had their baseline punctuation restored. The evidence register, session sources, participant materials, crisis procedures, LICENSE, explorer, catalog, and existing scripts remain unchanged.

The Phase 3 checker is run against its pinned Phase 3 snapshot, where its phase-specific allowed-path rule applies; it is not disabled or misreported as passing against new Phase 4 documents. Both catalog-withdrawal regression tests pass, the actual builder reproduces the unchanged empty catalog, and `git diff --check` passes. No full site build, hosted-site audit, or qualified review was performed.

**Gates satisfied: 0 of 6. Delivery remains withheld.**
