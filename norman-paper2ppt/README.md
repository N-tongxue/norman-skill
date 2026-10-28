# Norman Paper2PPT 使用说明 / User Guide

## 技能用途 / Purpose

Norman Paper2PPT 将科研论文 PDF 制作成适合中文科研汇报的 PowerPoint 演示文稿。
Norman Paper2PPT turns a research paper PDF into a PowerPoint presentation for a Chinese research talk.

它围绕原论文的研究问题、方法、核心结果和启示组织内容，并把论文原始图表放入幻灯片。
It organizes slides around the paper’s question, methods, core results, and implications and places original paper figures on the slides.

## 在 Codex 中使用 / Use in Codex

上传论文 PDF，并输入“使用 `$norman-paper2ppt` 为这篇论文制作科研汇报 PPT”。
Upload the paper PDF and ask “Use `$norman-paper2ppt` to make a research presentation from this paper.”

| 模式 / Mode | 中文说明 | English explanation | 时长与页数 / Duration and slides |
| --- | --- | --- | --- |
| A | 简要概览。 | Brief overview. | 约 5 分钟，5–7 页。 / About 5 minutes, 5–7 slides. |
| B | 标准解读。 | Standard reading. | 约 10 分钟，8–12 页。 / About 10 minutes, 8–12 slides. |
| C | 深度解读。 | Deep reading. | 约 15 分钟，12–16 页。 / About 15 minutes, 12–16 slides. |

随后选择是否加入逐页讲稿，以及是否额外制作可编辑版本。
Then choose whether to include slide-by-slide speaker notes and whether to create an additional editable version.

如果已经在请求中写明模式、讲稿和可编辑版本，技能会直接使用这些选择。
If your request already states the mode, notes, and editable output choice, the skill uses those selections directly.

例如，输入“使用 `$norman-paper2ppt` 制作 B 模式汇报，附逐页讲稿，并提供可编辑 PPTX”。
For example, ask “Use `$norman-paper2ppt` in Mode B, include slide-by-slide speaker notes, and provide an editable PPTX.”

## 制作流程 / Production workflow

第一步，技能通读论文 PDF，整理研究背景、技术路线、数据方法、结果、局限和结论。
First, the skill reads the paper PDF and organizes the background, approach, data, methods, results, limitations, and conclusions.

第二步，技能记录各结果对应的原始图表、页码、关键数字和统计说明。
Second, the skill records the original figures, page locations, key numbers, and statistical details associated with each result.

第三步，技能规划封面、背景与方法、核心结果，以及创新与启示四个部分。
Third, the skill plans four parts: cover, background and methods, core results, and innovation and implications.

第四步，技能逐页制作 16:9 幻灯片，将论文原始图表插入版面，并完成演示文稿组装。
Fourth, the skill creates 16:9 slides, inserts original paper figures into the layout, and assembles the presentation.

第五步，如选择讲稿，技能会为每页写入适合口头讲述的说明和过渡语。
Fifth, if notes are selected, the skill adds spoken explanations and transitions for each slide.

## 交付内容 / Deliverables

| 交付物 / Deliverable | 中文说明 | English explanation |
| --- | --- | --- |
| 图片版 PPTX / Image-based PPTX | 每页包含一张完整的最终幻灯片图像。 | Each slide contains one complete final slide image. |
| 可编辑版 PPTX / Editable PPTX | 标题、正文、结论和页码等为可编辑对象，论文图表为图片对象。 | Titles, body text, conclusions, and page numbers are editable objects, while paper figures remain image objects. |
| 逐页讲稿 / Speaker notes | 提供逐页讲稿文件，并在适用的演示文稿中写入演讲者备注。 | Provides a slide-by-slide script and presenter notes where supported. |

## 本地命令 / Local commands

复制完整技能文件夹后，在 Windows PowerShell 中运行内置程序查看指南和资源。
After copying the complete skill folder, use the bundled executable in Windows PowerShell to read its guide and resources.

```powershell
& "<skill-root>/norman-paper2ppt.exe" guide
& "<skill-root>/norman-paper2ppt.exe" list
& "<skill-root>/norman-paper2ppt.exe" read references/local-execution.md
```

| 命令 / Command | 中文用途 | English use |
| --- | --- | --- |
| `prepare-image-batch` | 集中准备逐页图像提示词。 | Prepares slide image prompts together. |
| `validate` | 检查内容记录与图片。 | Checks content records and images. |
| `audit` | 检查 PPTX 文件结构。 | Inspects the PPTX file structure. |
| `fig2ppt` | 为可编辑版本调用内置重建工具。 | Calls the bundled reconstruction tool for editable output. |

需要制作可编辑版本时，同一程序还提供 `fig2ppt` 子命令和对应的内置说明。
For editable output, the same executable also provides the `fig2ppt` subcommand and its bundled instructions.

```powershell
& "<skill-root>/norman-paper2ppt.exe" read vendor/norman-fig2ppt/guide.md
& "<skill-root>/norman-paper2ppt.exe" fig2ppt probe
```

把 `<skill-root>` 换成技能文件夹路径，并用具体子命令的 `--help` 查看参数。
Replace `<skill-root>` with the skill folder path, and use each subcommand’s `--help` option for its arguments.

macOS 和 Linux 用户选择与系统及处理器匹配的同名可执行文件。
On macOS and Linux, choose the executable that matches the operating system and processor.

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。
