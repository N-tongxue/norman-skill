# A research-question-driven reading workflow

For helper command examples below, replace `<engine>` with the complete platform invocation selected in SKILL.md: Windows `& "<skill-root>/bin/windows-x64/norman-reader.exe"`, or Mac `/bin/sh "<skill-root>/bin/norman-reader"`. Do not use a system Python or assume `norman-reader` is on PATH.


## Efficiency by task

Treat the stages below as a guide, not three mandatory complete rereads. quick uses the overall-picture stage and targeted checks, then a compact insight and next step; focused follows only the requested item and necessary context. deep covers the full main research storyline, relevant main figures, and decisive methods, then future research insights and a practical next-step plan. extend adds project transfer, detailed actions, and a staged roadmap using the necessary deep evidence; it does not automatically require new experiments or a duplicate whole-paper report.

Load only the references relevant to the mode. Consult script implementation only when execution fails or behavior is unclear. For a supplied full-text paper, use its contents before searching externally. Check relevant supplements when they affect a conclusion; broad novelty verification, whole-reference-list discovery, repository audits, and full translation are separate tasks unless requested. Limit any unverified novelty statement accordingly.

Reuse source text, image renders, and evidence after checking paper identity/version, fingerprint where available, and actual coverage. Existing images still require inspection if no reliable inspection record/context exists. Track pending pages/items so reuse never conceals omissions. Do not create saved artifacts for a chat-only answer.

For a lengthy deep/extend task, report a brief initial overview once enough source text supports it, stating what is author-reported versus already checked and what remains. Continue to the requested completion without asking the user whether to proceed. If only an abstract is available, label the overview accordingly and do not pretend the whole paper was read.

## 1. Source and reading scope

Record title, version/date, paper type, accessible pages, and supplements. Distinguish abstract, full text, preprint, and published version; do not mix results across versions. Begin when a specific paper is supplied without requiring a reader profile. With only a title, use host search to obtain source material; if retrieval fails, disclose the available scope and limit the assessment accordingly.

For saved reports, give each paper a separate directory containing `reading-note.md`, `evidence.json`, `source/source_map.json`, and `assets/`. Omit unnecessary files for chat and local explanations. Preserve the source PDF.

```text
<engine> extract "<paper.pdf>" --out "<output>/source"
<engine> render "<paper.pdf>" --pages 1,3-5 --out "<output>/assets/pages"
```

Source mappings include IDs such as `P0001-B0001`, bounding boxes, original text, and file fingerprints. Sorting is only a candidate reading order. Compare multicolumn text, multipage captions, equations, and tables with rendered pages. Embedded PDF images may be incomplete figure components.

For web or pasted text, use the same mapping structure: `source` contains `kind`, `title`, `url`, and `version`; `blocks` contains `id`, `kind`, `text`, and a verifiable `locator`. Without PDF pages, use section/paragraph/figure/URL locators rather than invented page numbers. A URL without retrieved content cannot count as inspected evidence.

## 2. First pass: overall picture

Read the abstract, key introduction gap, principal results, and conclusion; inspect the decisive figure/method overview needed to ground the summary. Use full-text search or source-map blocks to locate relevant passages rather than repeatedly reading the entire extraction. Build known → unknown → claim → design → evidence → boundary. List claims before checking whether results address them. In quick mode, give reasons for close reading, selective reading, background use, or deferral relative to the user's goal; priority is a reading recommendation, not a publication score.

## 3. Second pass: decisive evidence and methods

For deep/extend, inspect figures, tables, experiments, or propositions that determine the central conclusions, then read the necessary methods. For quick, verify only the results used in the concise summary; for focused, stop once the local question and boundary are supported. Record observations, IDs, and source locations during this reading instead of rebuilding them afterward. Use D IDs for important design choices and C/E IDs for claims/evidence. Explain module inputs, operations, outputs, connections, and why they may work rather than defining module names alone.

Capture a complete original image for every individually explained figure/table and place it before that item's analysis. Batch known figure-bearing pages at default DPI and inspect them once. Use a readable full page as the original when sufficient; confirm a crop or increase DPI only to resolve a specific readability/completeness problem. Preserve captions and panel coverage. See [figure-and-equation-reading.md](figure-and-equation-reading.md). If image retrieval or inspection fails, disclose the limitation locally and in the reading scope.

Check controls, metrics, statistical units, independent validation, data leakage, assumptions, and proof conditions according to [paper-types.md](paper-types.md). Actually read necessary supplements; if unavailable, retain the gap.

## 4. Third pass: reconstruction and boundaries

Explain decisive methods in your own words; add pseudocode or extended derivation when it resolves a real ambiguity or is requested. Mark source statements, implementation inferences, and missing details. This stage is unnecessary for a quick summary unless its conclusion depends on such a check. A virtual reconstruction is not a completed reproduction. Explain consequential choices and meaningful alternatives. In theory, inspect counterexamples or failure cases when assumptions are relaxed.

Write evidence cards for central claims: source, experiment/derivation, observation, conditions, degree of support, and alternative explanations. Do not force novelty, criticism, or mechanism claims.

## 5. Future research insights and planning

For whole-paper deep analysis, add distinct future-insights and next-step-plan sections by default. Quick gives a compact insight and first check; respect summary-only and focused scope. Follow [future-research-planning.md](future-research-planning.md) for deep/extend. Derive transferable principles and testable questions from checked contributions and gaps, not only from the authors' future-work paragraph. Prioritize the smallest useful check, give its method/control, supporting and weakening outcomes, resources, and deliverable, then link later work to that decision. Without a user project, label the plan general and state adaptation assumptions. Extend expands action cards and the roadmap and retains separate transfer conditions and reproduction checklist sections where relevant. Proposed planning does not authorize executing the work.

## 6. Verification and continued reading

Give page, section, figure/table, or source-block IDs for key conclusions. Disclose unread material, uncertain OCR, images not visually inspected, and missing parameters. Check key scientific evidence while reading/writing. At completion, reconcile scope and cross-check unresolved/high-risk claims; do not repeat already successful inspections without a specific reason. Run structural validation once after saved content/assets are ready, then rerun affected checks only after repairs. Use the selected mode's heading outline in [output-and-brand.md](output-and-brand.md).

Long papers can be developed section by section in the same note with pending coverage marked; partial reading is not full close reading. Reuse C/E/D/A IDs and source locations in follow-ups. When a judgment changes, record the reason for the revision.

## Fallbacks

- Abstract only: quick assessment; no invented figures or equations.
- Scanned PDF: render, then use the host's OCR/visual capabilities; failed pages remain missing.
- No visual inspection capability: give a provisional caption-based explanation, show an obtainable original if possible, and disclose that its content was not visually checked.
- No original image: disclose the missing figure/table image at its explanation; do not substitute a fabricated visual.
- No PyMuPDF: use the host's available PDF tools or supplied text.
- No supplements/code: explain what the main text establishes and list reproduction gaps.
- Unclear metadata: do not invent DOI, authors, year, recency, or first-ever claims.
