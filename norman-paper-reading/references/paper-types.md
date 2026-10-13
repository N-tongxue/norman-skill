# Select analysis units by research type

| Type | Analysis units | Main checks | Do not require |
|---|---|---|---|
| Experimental / discovery / mechanism | Experiments, composite figures, discovery-to-validation steps | Independent samples, technical/biological replicates, controls, measurements, alternative mechanisms, statistical hierarchy, extrapolation | A causal explanation for every association |
| Algorithm / method / model | Inputs/outputs, modules, objectives, validation | Data splitting/leakage, baseline and budget fairness, ablations, variance, generalization, cost | Wet-lab or clinical validation |
| Theory | Assumptions, definitions, propositions, proofs | Quantifiers, conditions, lemmas, proof gaps, counterexamples, boundary cases | Experimental proof |
| Dataset / benchmark / resource | Collection, labeling, protocols | Coverage, bias, quality, accessibility, evaluation constructs, contamination | A new algorithm |
| System | Bottlenecks, components, workloads | Realism, throughput/tail latency, failures, cost, scale, deployment | Accuracy as the sole criterion |
| Review / perspective | Selection scope, classification, synthesis claims | Inclusion rules, representativeness, contrary findings, time coverage, evidence levels | New experiments/proofs |

For mixed studies, combine checks around the core contribution. A missing item does not automatically invalidate the study; explain which conclusion it affects. Adapt report headings to the analysis units while keeping major outputs visually prominent.

## Domain checks only when relevant

Remote sensing/spatiotemporal work: independent spatial and temporal splits, regional transfer, resolution, ground validation. Biomedical work: patient/animal/sample/cell hierarchy, discovery and validation cohorts, technical replicates. Materials/physics: instrument conditions, calibration, units, model assumptions, measurement uncertainty. Activate these only when relevant; do not insert another reader's fixed research project.

## Novelty

Distinguish claimed novelty, differences from the paper's baselines, and contributions verified through additional related work. Without field checks, avoid first-ever or revolutionary claims. Venue and citation counts can supply context but do not establish correctness.
