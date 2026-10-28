# Norman Research Idea 使用说明 / User Guide

## 技能用途 / Purpose

Norman Research Idea 根据研究方向、具体问题、初步构想或论文集合，发展有文献依据的研究方案。
Norman Research Idea develops literature-grounded research proposals from a direction, specific question, early concept, or collection of papers.

它会检索相关研究、识别证据缺口、比较相近工作，并设计可执行的研究路径。
It searches relevant work, identifies evidence gaps, compares close prior studies, and designs an actionable research path.

## 在 Codex 中使用 / Use in Codex

输入研究方向或问题，并在请求中写出“使用 `$norman-research-idea` 发展研究思路”。
Enter a research direction or question and ask “Use `$norman-research-idea` to develop research ideas.”

| 可提供的输入 / Possible input | 中文用途 | English use |
| --- | --- | --- |
| 研究方向或问题 / Direction or question | 确定要探索的主题。 | Defines the topic to explore. |
| 已有论文或草案 / Papers or draft proposal | 帮助定位相近工作和现有设想。 | Helps identify close prior work and the current concept. |
| 数据或实验条件 / Data or research resources | 帮助设计可实施的研究路径。 | Helps design a feasible research path. |

例如，输入“使用 `$norman-research-idea`，围绕城市热岛与老年人健康提出可实施的研究方案，并列出必读论文”。
For example, ask “Use `$norman-research-idea` to propose feasible studies on urban heat islands and older adults’ health, with essential reading.”

如果方向很宽泛，可以进一步说明学科、研究对象、可用数据、方法偏好和时间范围。
If the direction is broad, add the discipline, study population or object, available data, preferred methods, and time frame.

如果你已有一个设想，可以要求重点检查与最接近论文的区别、关键对照和可能推翻假设的结果。
If you already have an idea, ask it to focus on differences from the closest papers, critical controls, and outcomes that could weaken the hypothesis.

## 研究流程 / Research workflow

第一步，技能围绕主题、同义词、相关方法和竞争解释检索基础论文、近期研究及相近工作。
First, the skill searches foundational papers, recent studies, and close analogues using topic terms, synonyms, related methods, and competing explanations.

第二步，技能核对重要论文的题名、作者、年份、来源、DOI 和与研究问题相关的内容。
Second, it checks important papers’ titles, authors, years, publication sources, DOIs, and content relevant to the research question.

第三步，技能把已有结论与待研究的问题对应起来，生成若干候选研究思路。
Third, it maps established findings against open questions and generates candidate research ideas.

第四步，技能为每个候选思路查找相近研究，比较真正的差异、实施条件和潜在贡献。
Fourth, it searches close prior work for each candidate and compares the real differences, implementation requirements, and potential contributions.

第五步，技能推荐优先方案，写出研究问题、假设、数据或材料、方法、对照、预期观察和首个行动。
Fifth, it recommends priority proposals and describes the question, hypothesis, data or materials, method, controls, expected observations, and first action.

第六步，技能整理必读论文，并为领先方案绘制研究流程图。
Sixth, it compiles essential reading and creates a research workflow diagram for the leading proposal.

## 交付内容 / Deliverables

| 交付内容 / Output | 中文说明 | English explanation |
| --- | --- | --- |
| 文献与缺口 / Literature and gaps | 汇总相关研究及待解决问题。 | Summarizes relevant work and open questions. |
| 候选思路 / Candidate ideas | 比较各思路与相近工作的差异及实施条件。 | Compares each idea with close prior work and implementation needs. |
| 重点方案 / Priority proposal | 写出问题、假设、方法、对照和首个行动。 | Describes the question, hypothesis, method, controls, and first action. |
| 必读论文与流程图 / Reading and diagram | 提供重点论文和领先方案的研究流程图。 | Provides key papers and a workflow diagram for the leading proposal. |

如果需要独立报告，可以在请求中指定保存位置和想要的文件格式。
If you want a standalone report, specify its save location and preferred file format in the request.

## 本地命令 / Local commands

复制完整技能文件夹后，在 Windows PowerShell 中运行内置程序查看指南、资源和命令参数。
After copying the complete skill folder, use the bundled executable in Windows PowerShell to read the guide, resources, and command arguments.

```powershell
& "<skill-root>/norman-research-idea.exe" guide
& "<skill-root>/norman-research-idea.exe" list
& "<skill-root>/norman-research-idea.exe" read references/literature-search.md
```

| 命令 / Command | 中文用途 | English use |
| --- | --- | --- |
| `verify` | 读取文献 JSON 并核对 DOI 元数据；加入 `--online` 时查询 Crossref。 | Reads reference JSON and checks DOI metadata; `--online` queries Crossref. |
| `render` | 读取研究流程 JSON 并输出可编辑的 SVG 流程图。 | Reads workflow JSON and outputs an editable SVG diagram. |

```powershell
& "<skill-root>/norman-research-idea.exe" verify "<references.json>" --online --output "<verified.json>"
& "<skill-root>/norman-research-idea.exe" render "<workflow.json>" "<workflow.svg>"
```

把 `<skill-root>` 换成技能文件夹路径，并通过 `verify --help` 和 `render --help` 查看完整用法。
Replace `<skill-root>` with the skill folder path, and use `verify --help` and `render --help` for full usage.

macOS 和 Linux 用户选择与系统及处理器匹配的同名可执行文件。
On macOS and Linux, choose the executable that matches the operating system and processor.

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。
