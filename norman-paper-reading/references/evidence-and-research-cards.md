# Traceable evidence and research actions

## Separate source records from judgments

`source_map.json` records source material actually obtained. PDF blocks have page numbers and bounding boxes; web/text blocks have locators. `evidence.json` records research judgments made from source text and images.

Stable IDs: C for claims, E for evidence, D for design decisions, A for actions. Prefix IDs for multiple papers, such as `P1-C01`, and display them in the note. Direct observations, author interpretations, and analyst inferences do not automatically have equal certainty.

## Record once, reuse appropriately

Capture source locations, observations, and stable IDs during reading; use those records for the note, evidence JSON, and action cards. Reference an already explained figure by ID instead of repeating its full interpretation in every card. Reuse records only for the same source/version and covered material; revise affected links when conclusions change. Chat-only quick/focused answers need no serialized JSON or empty schema scaffold. Saved deep/extend notes retain the full contract below.

## JSON contract, schema_version = 1

Top-level fields: `paper`, `claims`, `evidence`, `links`, `branches`, `actions`; the last two may be empty.

- `paper`: `title`; add known `version`, `url`, `source_sha256`, and `scope` (actual reading coverage).
- `claims[]`: `id`, `statement`, `origin`, where origin is paper_fact / author_interpretation / analyst_inference / hypothesis; use `caveat` for uncertainty.
- `evidence[]`: `id`, `kind` (text/figure/table/equation/experiment/proof/code), `locator`, `source_ids`, `observation`, `inspection` (verified/not_visual_checked/unavailable). Optional `quote` contains only actual source text. Register supplements/code as separate source blocks with file/URL information; do not point to unrelated main-text blocks.
- `links[]`: `claim_id`, `evidence_id`, `relation` (supports/limits/contradicts/mixed), `strength` (strong/moderate/weak/uncertain), `rationale`. Strength is an analytical judgment, not a statistical score.
- `branches[]`: `id`, `choice`, `problem`, `rationale`, `origin` (author/analyst/unknown), `evidence_ids`, `alternative`, `possible_effect`. Author rationale needs direct grounding; analyst inference is not author intent.
- `actions[]`: `id`, `gap`, `question`, `hypothesis`, `method`, `controls`, `decision_rule`, `resources`, `feasibility` (ready/requires_resources/exploratory), `evidence_ids`. Explain when controls do not apply. Saved deep/extend plans record substantive proposals here. Optional `priority`, `phase`, `dependencies`, `deliverable`, and `milestone` retain roadmap details without changing schema_version; existing validators do not check these optional fields.

Evidence locations must connect to IDs in source-map `blocks`. A URL without read content cannot be marked verified. For figures/tables, verified means the original was actually viewed, not merely that a PNG was generated; structural scripts cannot establish this. Text quotes must occur in referenced text blocks; purely visual measurements belong in `observation`, not invented quotes. Keep original images next to the corresponding note explanations, following [figure-and-equation-reading.md](figure-and-equation-reading.md).

## Three card types

**Evidence card:** claim, corresponding result, source, conditions, support level, and conclusions that cannot be drawn. Association does not automatically establish causality; simulation does not establish real-world validity; training fit does not establish external generalization; a case does not establish universality.

**Design decision:** choose decisions affecting results, interpretation, or reproduction. Separate source explanations from benefits inferred by the analyst; say when a rationale is unstated. Alternatives address the same problem and disclose resource/assumption costs.

**Research action:** derive a question, method, controls, and outcomes supporting or weakening a hypothesis from a checked result or evidence gap. State a concrete deliverable, priority, prerequisites, and the next decision. Mark unknown thresholds/sample sizes as requiring estimation rather than inventing improvement percentages or p-values. Explain condition differences in cross-domain transfer. Readiness is not a paper ranking. See [future-research-planning.md](future-research-planning.md) for the default deep plan and detailed extend roadmap.

Retain open questions when grounding is insufficient; do not force card counts. Template and demonstration numbers must never enter real-paper conclusions. If no grounded action is feasible, explain why and add a nonempty top-level `action_status` in evidence JSON.
