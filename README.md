
# Norman-Skill

你好，我是 **N同学(Norman)**，一名清华大学在读博士生。  
Hi, I'm **Norman (N同学)**, a PhD student at Tsinghua University.

科研过程中，我经常会遇到论文图片难编辑、PPT 制作耗时、科研工作流重复繁琐等问题。因此，我把自己日常使用和整理的一些方法逐渐做成了 **Norman-Skill**。

During my research, I often encounter time-consuming tasks such as editing figures from papers, preparing presentation slides, and repeating similar research workflows. To make these tasks easier, I started organizing the methods and tools I use in my daily research into **Norman-Skill**.

这里会持续更新科研制图、论文图片处理、PPT、AI 辅助科研等实用 Skill，希望让一些原本需要反复手动完成的工作变得更简单、更高效。

This repository will continuously provide practical Skills for scientific visualization, figure processing, PowerPoint creation, AI-assisted research, and other research workflows — making repetitive tasks simpler and more efficient.

如果这些 Skill 对你有帮助，欢迎 ⭐ Star 本项目。  
If you find these Skills useful, feel free to ⭐ **Star this repository**.

---

## 👋 关于我 | About Me

- 🎓 **清华大学在读博士生 | PhD Student at Tsinghua University**
- 📕 **小红书 | Xiaohongshu:** N同学
- 🎵 **抖音 | Douyin:** 耐心的N同学
- 📺 **B站 | Bilibili:** 耐心的N同学

平时主要分享：  
I mainly share content about:

- 科研效率工具 | Research productivity tools
- AI 辅助科研 | AI-assisted research
- 论文写作与科研绘图 | Academic writing & scientific visualization
- PPT 制作与优化 | Presentation design & optimization
- 数据分析与科研工作流 | Data analysis & research workflows
- 博士阶段的一些学习与科研经验 | PhD study & research experience

---

# 🧩 Norman-Skill

**Norman-Skill** 是一个持续更新的实用 Skill 项目。  
**Norman-Skill** is a continuously updated collection of practical Skills for research.

项目会围绕真实科研场景，逐步整理和发布可以直接使用的 Skill，让 AI 更好地参与论文制图、PPT、图像处理、科研写作以及其他科研工作流。

The project focuses on real-world research scenarios and provides reusable Skills that allow AI to participate more effectively in scientific visualization, presentations, image processing, academic writing, and other research workflows.

目前已经上线的 Skill：  
Currently available Skills:

| Skill | 功能 / Purpose | 使用说明 / Guide |
|---|---|---|
| [norman-fig2ppt](norman-fig2ppt/) · v1.3.1 | 论文图片转为可编辑 PowerPoint 图形 / Convert paper figures into editable PowerPoint shapes | [中英说明 / Bilingual guide](norman-fig2ppt/README.md) |
| [norman-paper-reading](norman-paper-reading/) · v1.4.0 | 研究过程重建、批判性证据审查、逐图精读与科研创新规划 / Research reconstruction, critical evidence evaluation, figure-by-figure analysis, and research innovation planning | [中英说明 / Bilingual guide](norman-paper-reading/README.md) |
| [norman-research-idea](norman-research-idea/) · v2.0.0 | 文献核查、创新点评估与可执行研究方案设计 / Literature review, novelty assessment, and actionable research proposal design | [中英说明 / Bilingual guide](norman-research-idea/README.md) |
| [norman-paper2ppt](norman-paper2ppt/) · v1.1.0 | 学术论文转中文研究汇报 PPT，含原文图、可选讲稿及可编辑版本 / Turn academic papers into Chinese research presentations with original figures, optional speaker notes and editable output | [中英说明 / Bilingual guide](norman-paper2ppt/README.md) |
| [norman-humanize](norman-humanize/) · v1.3.2 | 中英文写作去 AI 痕迹，保留原意与文风，支持可见增删和 Word 真实修订 / Edit Chinese and English prose while preserving meaning and voice, with visible edits and real Word tracked changes | [中英说明 / Bilingual guide](norman-humanize/README.md) |

### 下载与安装 | Download and Install

**🚀 简捷安装 | Quick Installation**

无需手动配置，只需将 Norman-Skill 的 GitHub 仓库链接发送给支持 Skill 安装的 AI 编程助手，并告诉它：

No manual setup needed. Simply share the Norman-Skill GitHub repository link with an AI coding assistant that supports Skill installation and say:

```text
帮我安装 Norman-Skill 仓库中的所有 Skill。

Install all Skills from the Norman-Skill repository.
```

AI 助手可根据仓库说明，自动完成下载、安装及依赖配置。安装完成后即可调用对应 Skill。

The AI assistant can follow the repository instructions to download, install, and configure the Skills. Once installed, the Skills are ready to use.

**📦 手动安装 | Manual Installation**

完整的本地技能位于 [norman-fig2ppt/](norman-fig2ppt/)、[norman-paper-reading/](norman-paper-reading/)、[norman-research-idea/](norman-research-idea/)、[norman-paper2ppt/](norman-paper2ppt/) 和 [norman-humanize/](norman-humanize/)。各技能的系统支持与使用要求见对应目录的中英双语说明。

The complete local skills are available in [norman-fig2ppt/](norman-fig2ppt/), [norman-paper-reading/](norman-paper-reading/), [norman-research-idea/](norman-research-idea/), [norman-paper2ppt/](norman-paper2ppt/), and [norman-humanize/](norman-humanize/). See each bilingual README for supported systems and requirements.

通过仓库的 **Code → Download ZIP** 下载并解压后，将需要的完整技能文件夹复制到支持 `SKILL.md` 的 AI 助手技能目录。不要只下载 `SKILL.md` 或单个可执行文件。

Download this repository using **Code → Download ZIP**, extract it, and copy the complete skill folder you need into the skills directory of an AI assistant supporting `SKILL.md`. Keep all bundled files together.

## 🎨 论文图片矢量化 | Paper Figure Vectorization

**模型设置提示：** 使用本技能时，请关闭模型的“快速模式（Fast mode）”。此设置与技能自身的 Quick / Advanced 重建模式分别选择。

**Model setting:** Keep the model's Fast mode disabled when using this skill. The skill's Quick / Advanced reconstruction modes remain separate choices.

将论文中的复杂图片转换为：

Convert complex figures from research papers into:

> **PowerPoint 中可编辑的矢量图形**  
> **Editable vector graphics in PowerPoint**

转换后的文字、线条、箭头、图标以及其他图形元素，都可以在 PowerPoint 中进一步修改、移动和重新排版。

Text, lines, arrows, icons, and other graphical elements can be further edited, moved, resized, and rearranged directly in PowerPoint.

适用于：  
Suitable for:

- 论文汇报 | Research presentations
- 文献讲解 | Paper presentations
- 科研绘图 | Scientific visualization
- PPT 制作 | PowerPoint creation
- Figure 重构 | Figure reconstruction
- 图形二次编辑 | Figure editing and reuse

---

## 🔍 效果展示 | Demo

### 原始图片 → 可编辑矢量图  
### Original Figure → Editable Vector Graphics

| 原始论文图片<br>Original Figure | Norman-Skill 矢量化结果<br>Vectorized Result |
| :---: | :---: |
| <img src="assets/originalfig.png" width="420"> | <img src="assets/vectorized-ppt.png" width="420"> |
| **原始论文图片**<br>Original paper figure | **PowerPoint 中可编辑的矢量元素**<br>Editable vector elements in PowerPoint |

---

## ✨ 矢量化后的编辑效果 | Editable Results

<p align="center">
  <img src="assets/vectorized-ppt2.png" width="90%">
</p>

<p align="center">
  <em>
  图中的文字、线条、箭头和图形元素均可在 PowerPoint 中进一步编辑。<br>
  Text, lines, arrows, and graphical elements can all be further edited in PowerPoint.
  </em>
</p>

---

## 📚 批判性文献精读与科研创新 | Critical Paper Reading & Research Innovation

**不盲从顶刊，不止于总结。以审稿人的眼光审视证据，以研究者的思维探索创新。**

**Read Like a Reviewer, Think Like a Researcher, Innovate Beyond the Paper.**

[norman-paper-reading v1.4.0](norman-paper-reading/) 不只是论文总结工具，而是一套以**研究过程重建、批判性证据审查和科研创新规划**为核心的文献精读 Skill，帮助研究者从读懂论文走向发现问题、设计研究。

[norman-paper-reading v1.4.0](norman-paper-reading/) goes beyond paper summarization, combining **research reconstruction, critical evidence evaluation, and research innovation planning** to transform paper reading into actionable scientific insights.

### 🔍 三大核心功能 | Three Core Features

- **研究过程重建 | Research Reconstruction**：梳理科学问题、研究假设与技术路线，识别数据、模型和实验设计中的关键决策及替代方案。 / Reconstruct scientific reasoning and examine critical methodological choices and alternatives.

- **批判性证据审查 | Critical Evidence Review**：逐图逐表分析核心结论的证据支撑、适用条件与局限，区分事实、解释和推断，不盲从顶刊结论。 / Evaluate claims against figures, tables, and evidence, identifying limitations and distinguishing facts from interpretations.

- **科研创新规划 | Research Innovation Planning**：将证据缺口转化为可检验的科学问题、研究假设、实验设计与判断标准，形成可执行的下一步研究方案。 / Turn evidence gaps into testable hypotheses, experimental designs, evaluation criteria, and actionable research plans.

支持快速总结、全文精读、逐图讲解（附论文原图）、公式解析及离线 HTML 阅读报告。

Supports quick summaries, critical full-paper reading, original-figure analysis, equation explanations, and offline HTML reports.

### 💡 使用示例 | Usage Examples

```text
请用 $norman-paper-reading 总结这篇论文：[PDF / DOI / arXiv / 正文]。

请用 $norman-paper-reading 批判性精读这篇论文，重建研究过程，逐图审查证据，并提出可检验的创新研究方案。

Use $norman-paper-reading to critically review this paper, analyze original figures, identify evidence gaps, and develop testable research ideas.
```

本包已内置 Python 与 PDF 处理依赖，无需额外安装或首次下载组件；扫描 PDF 会被标记，不含 OCR 引擎。

Python and PDF dependencies are bundled. No additional installation or first-run downloads are required. Scanned PDFs are flagged; OCR is not included.

完整说明：[中英使用说明](norman-paper-reading/README.md)。

Full guide: [Bilingual README](norman-paper-reading/README.md).

---

## 💡 科研选题与创新方案 | Research Ideas and Study Design

[norman-research-idea v2.0.0](norman-research-idea/) 从研究方向、具体问题、初步构想或论文集合出发，检索和核对相关文献，比较相近工作，识别研究缺口，并设计有证据支撑的可执行方案。

[norman-research-idea v2.0.0](norman-research-idea/) starts with a research direction, question, early concept, or paper set; it searches and checks the literature, compares close prior work, identifies research gaps, and designs evidence-grounded studies.

| 研究阶段 / Stage | 技能提供的内容 / What the skill provides |
|---|---|
| 文献梳理 / Literature mapping | 检索基础论文、近期研究和相近工作，并核对关键文献信息。 / Searches foundational, recent, and closely related work and checks key reference details. |
| 思路筛选 / Idea selection | 比较候选思路的差异、实施条件和潜在贡献。 / Compares candidate ideas by their differences, feasibility, and potential contribution. |
| 方案设计 / Study design | 明确问题、假设、方法、对照、预期观察和首个行动。 / Specifies the question, hypothesis, method, controls, expected observations, and first action. |
| 阅读与可视化 / Reading and visualization | 整理必读论文，并为优先方案绘制研究流程图。 / Curates essential papers and creates a workflow diagram for the leading proposal. |

```text
请用 $norman-research-idea 围绕我的研究方向梳理已有工作，筛选创新点，并设计可执行的研究方案：[研究方向 / 论文]。

Use $norman-research-idea to map prior work, evaluate research ideas, and design an actionable study: [direction / papers].
```

完整说明：[中英使用说明](norman-research-idea/README.md)。

Full guide: [Bilingual README](norman-research-idea/README.md).

---

## 📑 学术论文转研究汇报 PPT | Academic Paper to Research Presentation

[norman-paper2ppt](norman-paper2ppt/) 将学术论文 PDF 整理为中文研究汇报 PPT，围绕科学问题、研究方法与核心结果组织叙事，优先使用论文原图。支持 5 / 10 / 15 分钟三种汇报模式，默认输出 16:9 图片版 PPT，可选逐页讲稿和文字、图片可编辑版本。

Turn academic paper PDFs into Chinese research presentations built around the scientific question, methods, and key findings, prioritizing original paper figures. Choose a 5-, 10-, or 15-minute presentation, with a 16:9 image-based PPTX and optional speaker notes and editable text/image output.

```text
请用 $norman-paper2ppt 将这篇论文制作成 10 分钟中文文献汇报，附逐页讲稿和可编辑 PPT：[PDF]。
```

完整说明：[中英使用说明](norman-paper2ppt/README.md)。已内置 Windows / Mac / Linux 本地运行组件，制作幻灯片还需当前 AI 环境提供图像生成工具及可用的 PPT 生成与渲染工具。

Full guide: [Bilingual README](norman-paper2ppt/README.md). Windows / Mac / Linux runtimes are bundled; slide production also requires image-generation tools and an available presentation backend and renderer in the host AI environment.

---
## ✍️ 中英文写作去 AI 痕迹 | Chinese & English Writing Revision

[norman-humanize v1.3.2](norman-humanize/) 用于论文、报告、正式事务、自媒体和日常文字的语言修改，处理空泛表述、机械句式、重复和格式残留，保留原意、事实、术语、引用与作者文风。支持轻度、标准和深度修改；粘贴文字默认展示可见增删，完整 Word 文档交付可接受或拒绝的真实修订稿。

[norman-humanize v1.3.2](norman-humanize/) revises academic, professional, social media, and everyday writing in Chinese and English. It addresses empty phrasing, mechanical sentences, repetition, and formatting residue while preserving meaning, facts, terminology, citations, and voice. Choose light, standard, or deep editing, with visible edits for pasted text and real tracked changes for complete Word documents.

```text
请用 $norman-humanize 轻度修改这段论文，保留术语、数据和引用，显示全部增删：[文字]。

请用 $norman-humanize 处理这篇完整 Word，交付真实修订稿：[本地 DOCX]。
```

内置 Windows、Mac 与 Linux 运行程序，无需另装 Python 或首次下载依赖。实际语言修改由可执行本地命令的 AI 客户端完成，包内不包含 AI 模型。完整说明：[中英使用说明](norman-humanize/README.md)。

Windows, Mac, and Linux executables are bundled, with no separate Python installation or first-run dependency downloads. Language editing is performed by an AI client able to execute local commands; the package does not include an AI model. Full guide: [Bilingual README](norman-humanize/README.md).

---

## 🚀 为什么做 Norman-Skill？ | Why Norman-Skill?

很多科研工作其实并不难，但非常耗时间。  
Many research tasks are not technically difficult — they are simply repetitive and time-consuming.

例如：  
For example:

- 一张论文 Figure 想重新编辑，却只有 PNG；  
  You want to edit a figure from a paper, but only have a PNG image.

- 一张复杂流程图想复用，却需要重新画一遍；  
  You want to reuse a complex diagram, but have to redraw everything from scratch.

- PPT 中的大量元素需要手动调整；  
  Many elements in presentation slides need to be adjusted manually.

- 同样的科研任务需要反复操作；  
  The same research workflow needs to be repeated again and again.

- AI 能完成任务，但每次都需要重新写提示词和流程。  
  AI can help, but prompts and workflows often have to be recreated every time.

因此，我希望把这些重复性的工作逐渐整理成 Skill。

That is why I want to gradually turn these repetitive workflows into reusable Skills.

目标很简单：  
The goal is simple:

> **让 AI 真正进入科研工作流，而不只是回答问题。**  
> **Bring AI into real research workflows — not just use it to answer questions.**

---

## 🛠️ 后续会更新什么？ | What's Coming Next?

后续会持续更新更多科研相关 Skill，包括但不限于：  
More research-related Skills will be added, including but not limited to:

- 📊 论文图片矢量化  
  Paper figure vectorization

- 🎨 科研绘图与美化  
  Scientific visualization and figure enhancement

- 📑 PPT 自动生成与优化  
  Automated presentation generation and optimization

- 🧩 论文 Figure 拆解与重构  
  Paper figure decomposition and reconstruction

- 🖼️ 图片元素提取与编辑  
  Image element extraction and editing

- ✍️ 论文写作辅助  
  Academic writing assistance

- 📚 文献整理与阅读  
  Literature organization and reading

- 🤖 AI 辅助科研工作流  
  AI-assisted research workflows

- 💻 数据分析与代码辅助  
  Data analysis and coding assistance

- 🛠️ 更多提高科研效率的小工具  
  More tools for improving research productivity

更多 Skill 会陆续更新。  
More Skills are coming soon.

---

# 📱 关注我 | Follow Me

如果你对科研工具、AI Skill、论文写作、科研绘图以及博士阶段的学习与科研经验感兴趣，可以在下面的平台找到我。

If you're interested in research tools, AI Skills, academic writing, scientific visualization, or PhD research and study experiences, you can find me on the following platforms.

<table>
  <tr>
    <td align="center" width="220">
      <strong>📕 小红书<br>Xiaohongshu</strong>
      <br><br>
      <img src="assets/xiaohongshu-qr.png" width="170">
      <br><br>
      <strong>N同学</strong>
    </td>
    <td align="center" width="220">
      <strong>🎵 抖音<br>Douyin</strong>
      <br><br>
      <img src="assets/douyin-qr.png" width="170">
      <br><br>
      <strong>耐心的N同学</strong>
    </td>
    <td align="center" width="220">
      <strong>📺 B站<br>Bilibili</strong>
      <br><br>
      <img src="assets/bilibili-qr.png" width="170">
      <br><br>
      <strong>耐心的N同学</strong>
    </td>
  </tr>
</table>

---

## ⭐ Support

如果 Norman-Skill 对你的科研或学习有所帮助，欢迎：  
If Norman-Skill helps with your research or study, feel free to:

- ⭐ **Star 本项目 | Star this repository**
- 🍴 **Fork 并尝试自己的工作流 | Fork it and build your own workflow**
- 📢 **分享给有需要的同学 | Share it with others**
- 📱 **关注我的小红书 / 抖音 / B站 | Follow me on Xiaohongshu / Douyin / Bilibili**

<p align="center">
  <strong>
  更多 Skill 持续更新中 🚀<br>
  More Skills are coming soon 🚀
  </strong>
</p>
