# Norman Paper Reading 使用说明 / User Guide

## 技能用途 / Purpose

Norman Paper Reading 用于阅读指定科研论文，梳理研究问题、设计、证据、图表、公式和后续研究方向。
Norman Paper Reading reads a specified research paper and explains its question, design, evidence, figures, equations, and possible next steps.

它可以做快速概述、完整精读、面向复现的延伸分析，也可以只解释一张图、一条公式或一段文字。
It can produce a quick overview, a full close reading, a reproduction-oriented analysis, or an explanation of one figure, equation, or passage.

## 在 Codex 中使用 / Use in Codex

上传论文 PDF 或提供论文链接，并在请求中写出技能名和希望的阅读深度。
Upload the paper PDF or provide a paper link, and name the skill and desired reading depth in your request.

例如，输入“使用 `$norman-paper-reading` 精读这篇论文，重点解释图 2 和研究设计”。
For example, ask “Use `$norman-paper-reading` for a close reading of this paper, focusing on Figure 2 and the study design.”

| 阅读方式 / Mode | 适用请求 / When to use | 主要内容 / Main content |
| --- | --- | --- |
| 快速总结 / Quick | 想抓住研究问题、方法、主要结果和阅读价值。 / You want the question, method, main results, and reading value. | 核心设计、关键结果和阅读重点。 / Core design, key results, and reading priorities. |
| 完整精读 / Deep | 想理解论文全貌及关键实验、方法或理论。 / You want the full paper and its key experiments, methods, or theory. | 研究故事、图表、公式和证据边界。 / Research storyline, figures, equations, and evidence boundaries. |
| 延伸分析 / Extend | 想把论文用于自己的课题。 / You want to apply the paper to your project. | 迁移条件、复现清单和研究计划。 / Transfer conditions, reproduction checklist, and research plan. |
| 局部解释 / Focused | 只关心一张图、一条公式或一段文字。 / You need one figure, equation, or passage explained. | 指定内容、必要背景和解释。 / Requested item, essential context, and explanation. |

## 阅读结果 / Reading outputs

完整精读会把关键设计选择、原始图表和必要公式放入同一条研究脉络中解释。
A close reading explains key design choices, original figures, and necessary equations within one research storyline.

解释单张图时，结果会说明图的用途、阅读顺序、各面板的观察结果及其支持的结论。
For a single figure, the response explains its purpose, reading order, panel observations, and supported conclusions.

如需保存，可以指定 Markdown 报告和图片目录；如需网页阅读版，可以明确要求 HTML。
If you want saved files, specify a Markdown report and image folder; explicitly request HTML if you want a web reading version.

## 本地命令 / Local commands

复制完整技能文件夹后，先运行对应系统的程序并读取内置指南。
After copying the complete skill folder, run the executable for your system and read its bundled guide first.

```powershell
& "<skill-root>/norman-paper-reading.exe" guide
& "<skill-root>/norman-paper-reading.exe" list
& "<skill-root>/norman-paper-reading.exe" read references/reading-workflow.md
```

| 命令 / Command | 中文用途 | English use |
| --- | --- | --- |
| `extract` | 提取 PDF 文字和来源位置。 | Extracts PDF text and source locations. |
| `render` | 生成原始图表的页面图或局部图。 | Renders pages or crops of original figures. |
| `validate` | 检查已保存的报告和资源。 | Checks saved reports and assets. |
| `reader` | 将准备好的内容制作成 HTML 阅读版。 | Builds an HTML reading version from prepared content. |

通过 `extract --help`、`render --help`、`validate --help` 和 `reader --help` 查看各命令参数。
Use `extract --help`, `render --help`, `validate --help`, and `reader --help` to see their arguments.

该技能的本地程序适用于 Windows x64 和 macOS 的 Apple Silicon 或 Intel 机型。
The skill’s local executable supports Windows x64 and macOS on Apple Silicon or Intel.

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。
