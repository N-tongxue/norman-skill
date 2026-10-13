# norman-paper-reading

**English** · [中文说明](#中文说明)

Created and maintained by **N同学**. Xiaohongshu: **N同学**. Douyin / Bilibili: **耐心的N同学**.

Read scientific papers from their research questions, reconstruct study design, inspect original figures, and connect checked evidence to future research insights and prioritized plans. Whole-paper analysis includes **future research insights** and a **next-step research plan** by default, with concrete methods, controls, deliverables, and decision points. Supports experimental, methods, theoretical, and review papers.

## Installation and invocation

Place the entire `norman-paper-reading` folder in a host skill directory supporting `SKILL.md`, preserving its structure, or explicitly supply its folder path in a conversation. This package does not automatically install itself globally.

```text
Use $norman-paper-reading to read this paper closely: [local PDF / DOI / arXiv / paper text].
Use $norman-paper-reading to assess whether this paper is worth a deep read.
Use $norman-paper-reading to explain only Figure 3, show the original, and cover each panel and its evidence boundary.
Use $norman-paper-reading to propose testable next steps for my project based on this paper.
Use $norman-paper-reading to guide me through the methods, asking one question at a time.
Use $norman-paper-reading for full English–Chinese parallel reading, retaining figures, equations, and source locations.
```

Choose modes through natural language; there is no required questionnaire. Skill instructions, references, templates, and reader navigation are English. Reports follow the user's language; when unspecified, the fallback is Chinese. Provide your research background in chat or copy `assets/reader-profile-template.yaml` into your project.

## Modes and visible outputs

Each main output appears under its own prominent heading, rather than inside one long paragraph. Reports use a title (`#`), major sections (`##`), and individual figures/tables/cards (`###`). HTML gives major headings larger type and distinct section cards.

| Intent | Mode | Major report headings |
|---|---|---|
| Summarize, main points, worth reading, what is it about, quick overview. | quick | Research question; Core design; Key results; Evidence gaps; Future research insights and next steps; Reading priority |
| Analyze this paper, close reading, detailed explanation, journal club, whole-paper understanding. | deep (default for whole-paper analysis) | Full research storyline; Key design decisions; Figures/tables or key theorems; Necessary equations; Evidence cards; Future research insights; Next-step research plan |
| Reproduction, project application, future research planning. | extend | Necessary deep evidence; Future research insights; Transfer conditions; Reproduction checklist; Research action cards; Prioritized research roadmap |
| One figure, equation, or passage. | focused | Requested item; Necessary context; Explanation; Evidence boundary |

**Original images are shown beside their explanations:** each individually explained figure/table gets its own heading, followed by the original source image, source locator, and analysis. Preserve relevant panels, axes, legends, scale bars, captions, and table footnotes. Use complete page renders or ordered parts if a crop would lose information. A redrawn chart is not an original. If the original cannot be obtained or inspected, disclose that limitation at the item.

## Required bilingual watermark

## Faster summaries and first results

An unqualified "summarize this paper" request uses **quick**, with a compact future insight and first useful check. "Analyze this paper" and close reading use **deep**, including separate future-insights and research-plan sections. Explicit research planning uses **extend** for a detailed roadmap. Summary-only requests and focused explanations retain their scope. Quick does not automatically generate a complete deep report, evidence JSON, or HTML; speed preferences do not reduce requested coverage.

Future insights explain which results or design principles are transferable, why they matter, and under which conditions. Plans prioritize useful checks, specify methods/controls, resources, deliverables, and supporting/weakening outcomes, and link later work to earlier decisions. Without project context, the skill gives a general plan with explicit adaptation assumptions. Calendar estimates require useful project information; a report's plan does not execute or schedule the work.

The skill loads supporting references only when needed, reuses matching-source extraction and inspected images, batches known figure pages, and uses a readable original full page before spending time on crops. It records evidence during reading and avoids repeating explanations/checks. For lengthy deep/extend work, a brief source-grounded overview comes first; detailed reading continues in the same task. HTML is built only when requested, after content is ready.

```text
Use $norman-paper-reading to summarize this paper's main question, method, results, and limitations.
Use $norman-paper-reading to analyze this paper, including future research insights and a practical next-step plan.
Use $norman-paper-reading to read this paper closely; give me a brief overview first, then complete the figure-by-figure analysis with original images.
```

These changes reduce avoidable work and time to the first useful result. Actual latency depends on paper length, scan quality, source access, and the host/model; no fixed speedup is guaranteed.

| System | Helper invocation | Runtime selection |
|---|---|---|
| Windows x64 | `bin/windows-x64/norman-reader.exe` | Windows executable |
| Mac Apple Silicon | `/bin/sh bin/norman-reader` | Automatically selects arm64 |
| Mac Intel | `/bin/sh bin/norman-reader` | Automatically selects x86_64 |

The skill chooses the system-specific invocation. The Mac launcher detects native Apple Silicon even under Rosetta. PDF extraction/rendering, evidence validation, and offline HTML use the same subcommands on all platforms.

Windows PowerShell:

```powershell
& "<skill-root>/bin/windows-x64/norman-reader.exe" version
& "<skill-root>/bin/windows-x64/norman-reader.exe" extract "<paper.pdf>" --out "<output>/source"
& "<skill-root>/bin/windows-x64/norman-reader.exe" render "<paper.pdf>" --pages 1,3-5 --out "<output>/assets/pages"
& "<skill-root>/bin/windows-x64/norman-reader.exe" validate "<output>/reading-note.md" --mode deep --evidence "<output>/evidence.json" --source-map "<output>/source/source_map.json"
& "<skill-root>/bin/windows-x64/norman-reader.exe" reader "<output>/reading-note.md" --lang zh-CN --out "<output>/reader.html"
```

Mac Terminal:

```bash
/bin/sh "<skill-root>/bin/norman-reader" version
/bin/sh "<skill-root>/bin/norman-reader" extract "<paper.pdf>" --out "<output>/source"
/bin/sh "<skill-root>/bin/norman-reader" render "<paper.pdf>" --pages 1,3-5 --out "<output>/assets/pages"
/bin/sh "<skill-root>/bin/norman-reader" validate "<output>/reading-note.md" --mode deep --evidence "<output>/evidence.json" --source-map "<output>/source/source_map.json"
/bin/sh "<skill-root>/bin/norman-reader" reader "<output>/reading-note.md" --lang zh-CN --out "<output>/reader.html"
```

Quote paths. Pages are one-based; crop coordinates use unrotated page points. The source PDF is never saved or modified. Generated output refuses overwriting by default. Scanned pages are flagged; no OCR engine is bundled. 
---

# 中文说明

`norman-paper-reading` 由 **N同学**制作和维护。小红书：**N同学**；抖音 / B站：**耐心的N同学**。

从科学问题出发，重建研究设计，逐图核对证据，把论文转化成未来研究启示和可验证的科研行动。整篇分析默认输出 **未来研究启示** 与 **下一步研究规划**，明确方法、对照、交付成果和支持或否定方向的判断依据。适用于实验、方法、理论及综述论文。

## 放置与调用

把整个 `norman-paper-reading` 文件夹放入支持 `SKILL.md` 的宿主技能目录，保留内部结构；也可以在对话中明确指定该文件夹路径。本包不会自动安装到全局目录。

```text
请用 $norman-paper-reading 精读这篇论文：[本地 PDF / DOI / arXiv / 正文]。
请用 $norman-paper-reading 快速判断这篇文章是否值得精读。
请用 $norman-paper-reading 只解释 Figure 3，附原图，覆盖每个子图及其证据边界。
请用 $norman-paper-reading 从这篇论文出发，为我的课题提出可检验的下一步研究。
请用 $norman-paper-reading 陪我读方法部分，一次问一个问题。
请用 $norman-paper-reading 做全文中英对照，保留图、公式和原文定位。
```

模式按自然语言选择，没有强制问卷。skill 指令、参考规范、模板和 HTML 导航为英文；实际报告跟随用户语言，未指定时默认中文。个人背景可通过对话提供，或复制 `assets/reader-profile-template.yaml` 到研究项目填写。

## 模式与大标题

主要输出各用一个醒目的大标题，报告采用总标题（`#`）、主要部分（`##`）、单张图表或卡片（`###`）。HTML 主标题增大字号，并用独立区块区分内容。

| 意图 | 模式 | 主要报告标题 |
|---|---|---|
| 总结、主要内容、值不值得读、讲什么、快速了解 | quick | 研究问题、核心设计、关键结果、证据缺口、简短启示与下一步、阅读优先级 |
| 分析这篇文章、精读、详细解读、准备组会、读懂整篇 | deep（默认整篇分析模式） | 全文研究主线、关键设计分叉点、逐图逐表 / 关键定理、必要公式、证据卡、未来研究启示、下一步研究规划 |
| 复现、用于我的课题、未来研究规划 | extend | 必要的 deep 证据、未来研究启示、迁移条件、复现清单、科研行动卡、分阶段研究路线图 |
| 仅解释一张图、一个公式或一段 | focused | 当前内容、必要上下文、具体解释、证据边界 |

**逐图逐表讲解附论文原图**：每张图或表单独设标题，下面先放原图和来源定位，再逐项解释。保留相关子图、坐标、图例、比例尺、图注和表格脚注；裁剪不完整时用整页，跨页内容按顺序展示。重新绘制的图不能当作论文原图。无法取得原图或无法目视核验时，在对应内容旁明确说明。

## 更快总结与先出概览

普通“总结这篇论文”请求使用 **quick**：读取原文、核对决定性结果，给出简明总结及简短启示与第一步验证。“分析这篇文章”和精读使用 **deep**，默认单列“未来研究启示”和“下一步研究规划”。明确要求研究规划时使用 **extend** 展开路线图。用户只要总结、明确不要拓展，或仅解释一张图时，遵循其范围；quick 不自动生成完整 deep 报告、证据 JSON 或 HTML，也不会因提速省略明确要求的覆盖范围。

启示从已核对的结果和设计出发，说明可借鉴什么、为什么有价值、适用及失效条件。规划按证据价值、资源和依赖排序，写清方法与对照、所需数据、交付成果、支持或否定假设的结果，以及下一阶段的决策。没有个人课题背景时，先给通用规划并标注迁移假设，不编造用户项目。阶段围绕验证结果安排；需要具体日程时再依据资源估算。报告中的规划不会自动执行实验或创建日程。

参考规范按需加载；已提取的文本、来源映射和原图在核对论文版本、来源及覆盖范围后复用。已知图表页批量渲染，清晰的整页原图可直接使用，需要时才裁剪或提高清晰度。阅读时同步记证据，后续用编号引用，减少重复解释和重复检查。较长的 deep / extend 任务先给简短、有来源依据的概览，再在同一任务中完成详细分析；只有请求时才生成 HTML。

```text
请用 $norman-paper-reading 总结这篇论文的主要问题、方法、结果和局限。
请用 $norman-paper-reading 分析这篇文章，给出未来研究启示和可执行的下一步规划。
请用 $norman-paper-reading 精读这篇论文，先给简短概览，再完成逐图讲解并附原图。
```

这些调整减少额外工作，让第一个有用结果更早出现。实际耗时取决于论文长度、扫描质量、原文获取和所用模型，不承诺固定的提速比例。

Windows PowerShell：

```powershell
& "<skill-root>/bin/windows-x64/norman-reader.exe" version
& "<skill-root>/bin/windows-x64/norman-reader.exe" extract "<paper.pdf>" --out "<output>/source"
& "<skill-root>/bin/windows-x64/norman-reader.exe" render "<paper.pdf>" --pages 1,3-5 --out "<output>/assets/pages"
& "<skill-root>/bin/windows-x64/norman-reader.exe" validate "<output>/reading-note.md" --mode deep --evidence "<output>/evidence.json" --source-map "<output>/source/source_map.json"
& "<skill-root>/bin/windows-x64/norman-reader.exe" reader "<output>/reading-note.md" --lang zh-CN --out "<output>/reader.html"
```

Mac 终端：

```bash
/bin/sh "<skill-root>/bin/norman-reader" version
/bin/sh "<skill-root>/bin/norman-reader" extract "<paper.pdf>" --out "<output>/source"
/bin/sh "<skill-root>/bin/norman-reader" render "<paper.pdf>" --pages 1,3-5 --out "<output>/assets/pages"
/bin/sh "<skill-root>/bin/norman-reader" validate "<output>/reading-note.md" --mode deep --evidence "<output>/evidence.json" --source-map "<output>/source/source_map.json"
/bin/sh "<skill-root>/bin/norman-reader" reader "<output>/reading-note.md" --lang zh-CN --out "<output>/reader.html"
```

路径加引号，页码从 1 开始；裁剪坐标采用未旋转页面的点坐标。不会保存或修改原始 PDF，默认拒绝覆盖输出。扫描页会提示需要 OCR，包内不含 OCR 引擎。