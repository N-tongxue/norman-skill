# Output structure and brand

For helper command examples below, replace `<engine>` with the complete platform invocation selected in SKILL.md: Windows `& "<skill-root>/bin/windows-x64/norman-reader.exe"`, or Mac `/bin/sh "<skill-root>/bin/norman-reader"`. Do not use a system Python or assume `norman-reader` is on PATH.


## Prominent report headings

Use one `#` report title. Put each major output under its own `##` heading with blank lines around it. Use `###` for individual figures, tables, theorems, decisions, claims, or actions; use `####` for explanatory questions inside an item. Bold inline labels may identify fields but must not substitute for major headings. In HTML, keep the main sections visually distinct and include them in the table of contents.

The following outlines name the main outputs, not mandatory filler. Translate their headings into the user's report language, adapt them to paper type, and omit unsupported or irrelevant material with an explanation where it affects coverage. Do not present the four modes as four report sections; use the outline for the selected task.

### quick

Use separate `##` headings for **Research question**, **Core design**, **Key results**, **Evidence gaps**, **Future research insights and next steps**, and **Reading priority**. Keep the insights/steps section compact; omit it for an explicit summary-only request or a strict scope constraint. Open with a concise recommendation if helpful. Explain whether to read closely, read selectively, use as background, or defer, in relation to the user's goal.

### deep

Use separate `##` headings for **Core assessment and reading scope**, **Full research storyline**, **Key design decisions**, **Figures and tables, item by item** (or **Key theorems and proofs**), **Necessary equations**, **Evidence cards**, **Open questions and unread material**, **Future research insights**, **Next-step research plan**, and **Sources and reading record**. The final two analytical sections are default outputs unless the user excludes extensions. Follow [future-research-planning.md](future-research-planning.md); connect the plan to checked evidence and identify the first useful action. Each figure/table gets its own `###` heading and an original image directly underneath, followed by explanation. Do not bury equations inside a figure paragraph when they require substantial explanation.

### extend

Establish the necessary deep evidence, reusing an existing verified reading when available. Then add separate `##` headings for **Future research insights**, **Transfer conditions**, **Reproduction checklist**, **Research action cards**, and **Prioritized research roadmap**. Explain differences between the paper's conditions and the user's project, prerequisites, missing resources, controls, and observable outcomes. The roadmap orders actions by dependencies and evidence value, with deliverables, milestones, and stop/pivot conditions; it references action cards rather than repeating them. If no grounded action is available, state why and prioritize acquiring the necessary evidence rather than inventing advice.

### focused

Use a clear `##` heading naming the requested figure, table, equation, or passage, then only the necessary **Context**, **Explanation**, and **Evidence boundary** subheadings. For a figure/table, insert its original image immediately below the item heading. Do not generate a whole-paper report for a local question.

## Deliver the useful content early

For an unqualified summary request, use quick. Give a concise paragraph or short list under each relevant heading, with decisive results, conditions, source locations, and a compact future insight/next step unless excluded. For an unqualified whole-paper analysis request, use deep with future insights and a next-step plan. Do not add deep's complete figure-by-figure analysis, equation derivations, design alternatives, JSON, or HTML to quick unless requested. A separately explained figure/table still requires its original image.

In lengthy deep/extend work, give a short, source-grounded initial overview before image refinement, evidence serialization, or packaging. State coverage and whether results are only author-reported; continue all requested reading in the same task. The final report still contains the required detailed sections and original visuals. If the user requests a single saved report, place the concise overview first in that report and keep progress commentary brief.

Explain each result thoroughly once and use C/E/D/A cross-references in subsequent cards instead of repeating whole explanations. Group similar panels while naming coverage. Avoid repeating definitions and generic caveats. Build saved Markdown/evidence and requested HTML from the same checked content; do not independently rewrite the scientific analysis for each format. Run the note validator after content/assets are ready, not after every paragraph or image.

## Original images next to explanations

For every figure or table explained individually, embed the original source image in that item's section before the analysis. Include a source line giving figure/table number, panel coverage, PDF page or web locator, and source-block ID when available. Figures and tables discussed only as brief cross-references do not need duplicate images; link to their explanation instead. All substantially explained main figures/tables need an image or an explicit local missing-image disclosure.

For saved notes, keep images inside the note output directory, such as `assets/figures/fig-1.png`, and use relative Markdown links. For chat, use the host's native image display or an absolute local path that actually renders; filenames alone are insufficient. For multipage tables or figures, show all parts in order. Do not replace source images with recreated charts or tables. See [figure-and-equation-reading.md](figure-and-equation-reading.md) for capture and inspection rules.

## Brand

Product: **Norman Paper Reading**. Skill: **norman-paper-reading**. Creator and Xiaohongshu: **N同学**. Douyin / Bilibili: **耐心的N同学**. Keep account names unchanged; do not invent URLs, affiliations, partnerships, or contact details. Branding describes the tool and never replaces paper authors, references, or method names.

After each completed analysis in any mode, add this required bilingual watermark block exactly once at the end of chat, Markdown, or HTML, after results, sources, file links, and any delivery or verification notes. Always include both lines, Chinese first and English second, regardless of the report language. Use a visible line break (a Markdown hard break or separate paragraphs; HTML uses `<br>`):

```text
分析采用 norman-paper-reading 技能｜作者：N同学｜小红书：N同学｜B站/抖音：耐心的N同学
Analysis performed using the norman-paper-reading skill | Author: N同学 | Xiaohongshu: N同学 | Bilibili/Douyin: 耐心的N同学
```

HTML generates the same bilingual footer and removes an identical note watermark, earlier single-line watermarks, or the previous brand footer to avoid duplication. Include the watermark on completed focused answers as well; omit it from progress updates and unfinished guided-reading turns. The watermark is mandatory and cannot be disabled by a reader profile. HTML `--no-brand` hides only the reader's product banner; the required bilingual footer remains.

## Delivery and verification

quick/focused can be answered directly. Saved deep/extend notes include evidence JSON; comparisons identify each paper's sources and IDs. If extend yields no viable action, explain why and record `action_status` rather than inventing one.

```text
<engine> validate "<output>/reading-note.md" --mode deep --evidence "<output>/evidence.json" --source-map "<output>/source/source_map.json"
<engine> reader "<output>/reading-note.md" --lang en --out "<output>/reader.html"
```

Repair broken links and source references. If source material is unavailable, change its inspection status and disclose the gap; do not invent sources to pass validation. Check version, numbers, symbols, statistical units, original images, inference labels, and grounds for actions during analysis. At delivery, resolve outstanding checks and validate structure; do not repeat completed inspection steps without a new issue. State completed scope and material unfinished items at delivery.

HTML is an offline reader with navigation, search, and embedded local images. It does not change the note, execute source scripts, fetch remote images, or typeset LaTeX. Images must be within the note output directory; paths outside it are not embedded. External sources remain links. Missing images cause an error by default; `--allow-missing-images` is for an intentionally incomplete draft with visible missing-image notices. Use `--lang zh-CN` for a Chinese report or the appropriate tag for other languages. Navigation, notices, and script messages are English.
