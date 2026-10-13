# From a paper to future research insights and a plan

## Scope and depth

Whole-paper deep analysis includes separate **Future research insights** and **Next-step research plan** sections by default. Extend develops these into action cards and a staged roadmap tailored to the known project. Quick includes one compact insight and first check when useful, without requiring this reference. Explicit summary-only requests and focused figure/equation explanations keep their requested scope.

Use the evidence already checked in the reading. A plan should help the reader choose and begin useful work, not merely repeat the discussion's future-work paragraph. When source access is limited, label the directions provisional and prioritize obtaining the missing evidence. No project questionnaire is required before an initial useful plan.

## Future research insights

Select directions by scientific value, evidence support, and feasibility rather than filling a fixed quota. A deep report will often benefit from two or three strong directions, but fewer are better than unsupported ideas. Look for:

- A supported method or design principle that could transfer to another setting.
- A limitation or alternative explanation whose resolution would change the main conclusion.
- A new hypothesis suggested by a result pattern or unresolved comparison.

For each direction, connect **source result/gap → research insight → why it matters → transfer conditions → testable next question**. Cite the original section, figure, or E ID. Say whether the idea comes from the authors or is an analyst proposal. Explain both applicability and likely failure conditions. Distinguish established evidence, inference, and an untested hypothesis.

Avoid generic recommendations such as “use more data,” “combine AI,” or “improve interpretability.” Identify which data or comparison is needed, what uncertainty it resolves, and what scientific conclusion would change. Do not claim a publishable or first-ever direction from reading a single paper; targeted related-work checking can be a planned prerequisite.

## Next-step research plan

Lead with the highest-priority action and why it should come first. Rank actions using their expected information value, prerequisites, cost, and feasibility. Link substantive actions to A IDs and checked evidence. A compact deep plan can use a table:

| Priority / stage | Question and hypothesis | Method and comparison | Deliverable | Decision and next step |
|---|---|---|---|---|
| First useful check | The uncertainty that matters most | Data, procedure, baseline/control | A concrete analysis, figure, dataset, or protocol | What supports/weakens the idea; what follows in each case |

Include resources and missing prerequisites in the table or nearby prose. For each substantive action, make clear:

- **Grounding:** result or gap and source/E IDs.
- **Question:** a testable hypothesis or explicitly exploratory question.
- **Execution:** required data, method, baseline or control, and validation design.
- **Decision:** observable supporting and weakening outcomes; justified metrics and thresholds if known.
- **Output:** a concrete deliverable that can be inspected.
- **Feasibility:** available/missing resources, dependencies, and why its priority is appropriate.

Unknown sample sizes, effect sizes, thresholds, compute budgets, or completion times need estimation. Do not invent improvement percentages or treat failure to reject a null hypothesis as proof of equivalence. For exploratory analyses, state which observations would justify a confirmatory test.

## Stage the work around decisions

Prefer stages tied to evidence and dependencies rather than an arbitrary calendar:

1. **Near term: establish the premise.** Obtain key missing material, verify labels and splits, reproduce a decisive baseline, or perform the smallest informative check. Deliver an evidence check or pilot result.
2. **Next: test the promising direction.** Run the controlled comparison or targeted validation only after its prerequisites are met. Deliver comparative results and an uncertainty assessment.
3. **Later: extend if supported.** Test external generalization, a mechanism, a new setting, or a practical application. State the earlier milestone that permits this stage; narrow or replace the direction if the premise fails.

These are adaptable stages, not mandatory three-part filler. In deep, a compact sequence is enough. Extend should clarify dependencies, milestones, stop/pivot conditions, and the first concrete task the reader can start. Provide calendar estimates only when the user asks or project information makes them useful, labeling estimates and assumptions. Never create schedules or execute the proposed work merely because a report includes a plan.

## Project fit and evidence boundaries

Use supplied project goals, datasets, skills, and resource constraints when available. Otherwise label the output **General research plan; project adaptation assumptions** and state the few conditions that matter. Do not infer the user's affiliation, current experiments, equipment access, or project from the paper authors or filenames. Optional clarification may improve later tailoring but must not block a grounded general plan.

Preserve the paper's original sample unit and validation setting. Model-generated labels call for independent measurements when the goal is real-world accuracy; association-based findings call for suitable causal or mechanistic evidence when the proposed claim is causal. Adapt checks to the study type rather than applying every possible control.

## Deliver and check

In Chinese reports, normally use **未来研究启示** and **下一步研究规划**; a detailed extend roadmap may use **分阶段研究路线图**. Explain findings once in the analysis and cross-reference them here. Keep the first action explicit and distinguish recommendations from completed work.

For saved deep/extend notes, record substantive proposals in `actions[]` using the existing action schema. Optional `priority`, `phase`, `dependencies`, `deliverable`, and `milestone` fields can retain planning details. If no grounded action is possible, record `action_status` and explain what evidence must be obtained first. Check that each proposal is traceable, feasible under its stated conditions, and has an observable outcome; structural validation does not establish scientific novelty or feasibility.
