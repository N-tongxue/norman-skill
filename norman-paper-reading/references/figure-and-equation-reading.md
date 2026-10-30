# Reading figures, tables, and equations

## Capture and show the original

Each individually explained figure or table must appear as an original source image directly below its own heading, before the explanation. This applies to chat, Markdown notes, and HTML, including focused requests. A source locator or link alone is not a substitute when an image can be obtained. Keep original captions near the image, preserving their scientific wording; translations or commentary must be labeled separately.

For a local PDF, inspect a complete page first to locate the actual figure/table and caption; a textual "Fig." reference is not the figure location. Confirm the bounding box visually before cropping with `render_pages.py`. For composite vector figures, render the full region rather than extracting only the largest embedded raster. Capture multipage figures/tables in ordered parts. Preserve panel letters, axes, units, legends, scale bars, annotations, table headers, footnotes, and captions. If a complete crop is uncertain, show the full page and identify the relevant region.

For web papers, use the actual publisher/source figure or a faithful source screenshot available through the host. Inspect it and retain a traceable locator. Do not generate, redraw, recolor, or reconstruct a figure and label it as the paper's original. If an original is unavailable, state **Original image unavailable** in that item, give the reason and available locator, and limit the explanation to accessible text/captions. Missing visual access must not be labeled verified.

`render_pages.py` uses one-based page numbers and unrotated PyMuPDF page coordinates, with a top-left origin and points as units. Confirm coordinates using that script's full-page output and source-map bounds. Rotation is normalized in memory only; the source PDF is unchanged. The manifest records PDF fingerprint, page, bounding box, DPI, and path; multiple named crops merge into the same manifest. Rendering a PNG does not establish visual inspection: use `not_visual_checked` until it has actually been inspected.

For saved notes, store source images within the output directory and embed them as, for example:

```markdown
### Figure 2 — Does the effect hold in an independent cohort?

![Original Figure 2, panels a–f](assets/figures/fig-2.png)

Source: Figure 2, PDF page 5, panels a–f and original caption; source block P0005.

#### Why was this done?

Explain the question left open by the preceding result.
```

Use the actual paper's numbering, page, coverage, path, and source ID; the example is only a format. In chat, use a native image display or a renderable absolute local path. If a table is too dense to read at once, include a complete original plus useful enlarged regions. An optional transcribed table supplements the original and must be checked against it.

## Efficient image handling

Locate needed figures/tables from available text/source maps, then batch their known page numbers in one `render_pages.py --pages` call. Use the default 144 DPI first; increase it only if labels or details are unreadable. A clear, inspected complete page is a valid original image and avoids an unnecessary render–crop–inspect loop. Crop when surrounding text makes the image hard to read, an enlargement is needed, or the user requests it; confirm the bounding box first.

Reuse matching-source images and inspection records, processing only missing/changed items. A file's presence or manifest state alone is not proof of visual inspection. Pages containing several figures may share one original page image with clear figure locations; link subsequent brief cross-references to it. Every individually explained item still has its original image in its own section. Do not extract all embedded images, rerender completed pages, or refine harmless whitespace just for presentation. Essential labels, captions, coverage, and legibility always take precedence.

## Six questions for a figure

1. **Motivation:** What did the previous result leave open, and how does this analysis follow?
2. **Method:** What data, samples/repeats, controls, interventions, statistics, and necessary parameters were used?
3. **How to read it:** Explain panel types, axes and units, colors, symbols, and reference groups.
4. **Observation:** Cover relevant panels and verifiable directions, numbers, effect sizes, and intervals. Label visually estimated values as estimates.
5. **Interpretation and boundary:** Distinguish measured, calculated, predicted, associated, and mechanistic/causal findings. Check alternative explanations, statistical units, and extrapolation.
6. **Next question:** What does this figure establish, what does it leave open, and why is the next analysis needed?

Group repetitive panels by scientific question while naming the covered panels. Include supplementary figures when they determine an important judgment, control, or reproduction requirement. Do not prescribe a fixed number of lines. Use `####` question headings when explanations are substantial.

## Tables

Show the original table image first. Check columns, units, bolding rules, missing values, aggregation, and comparison conditions. Explain what comparison the table supports and its limits. Differences in metric direction, budget, or uncertainty can make direct ranking invalid. Preserve all parts and footnotes of multipage tables.

## Equations

Explain purpose → symbols and units/dimensions → operations → intuition → assumptions → method role → implementation or derivation limits. Clarify indices, sums/expectations, normalization, and constraints. Label demonstration data as demonstrations.

Distinguish original transcription, equivalent rearrangement, and added derivation; state additional assumptions. Similar-looking symbols do not prove equivalence. Do not confuse a training objective, estimator, and evaluation metric. Numerical checks are not general proofs.

Use `$...$` / `$$...$$` in Markdown. This bundle's HTML does not typeset LaTeX, so show important equations as original source crops with explanations. If transcription is unclear, retain the image and uncertainty rather than guessing exponents, symbols, or subscripts.
