# Norman Humanize 使用说明 / User Guide

## 技能用途 / Purpose

Norman Humanize 润色中文和英文稿件，调整重复、空泛或机械的表达，同时保留事实、语气和作者原意。
Norman Humanize edits Chinese and English drafts to improve repetitive, empty, or mechanical phrasing while preserving facts, tone, and the author’s meaning.

它适用于学术写作、正式报告、商务文字、社交媒体文案、日常文字和完整 Word 文档。
It works with academic writing, formal reports, business text, social posts, everyday writing, and complete Word documents.

## 在 Codex 中使用 / Use in Codex

粘贴文字或上传文档，并输入“使用 `$norman-humanize` 润色这份内容”。
Paste text or upload a document and ask “Use `$norman-humanize` to edit this content.”

开始改写前，选择文本类型、修改程度和处理范围。
Before editing starts, choose the text type, editing level, and scope.

| 设置 / Setting | 中文说明 | English explanation |
| --- | --- | --- |
| 文本类型 / Text type | 可选自动识别、学术论文或报告、正式商务或行政写作，以及社交媒体或日常写作。 | Choose automatic identification, academic paper or report, formal business or administrative writing, or social or everyday writing. |
| 处理范围 / Scope | 可选全部内容或指定段落、章节。 | Choose all content or selected paragraphs or sections. |

| 修改程度 / Editing level | 中文说明 | English explanation |
| --- | --- | --- |
| 轻度 / Light | 聚焦明确的问题表达。 | Targets clear wording problems. |
| 标准 / Standard | 可调整段内句子。 | May adjust sentences within a paragraph. |
| 深度 / Deep | 可在所选范围内重组段落结构。 | May reorganize paragraphs within the selected scope. |

你也可以提供自己的写作样本，让修改后的措辞更贴近原有风格。
You can also provide a writing sample so the revised wording better matches your existing style.

## 文字与 Word 的交付方式 / Text and Word outputs

| 输入 / Input | 中文交付说明 | English output description |
| --- | --- | --- |
| 粘贴文字 / Pasted text | 用 `~~删除~~` 和 `**新增**` 逐处标示修改，便于接受或保留原文。 | Marks each change with `~~deleted~~` and `**inserted**` so you can accept it or keep the original. |
| 完整 Word 文档 / Complete Word document | 生成带有 Word 原生修订记录的新 `.docx`，可在“审阅”界面逐项接受或拒绝。 | Creates a new `.docx` with native tracked changes that you can accept or reject in Word’s Review interface. |

## 工作流程 / Workflow

第一步，提供原稿并选定类型、修改程度和范围。
First, provide the draft and select the type, editing level, and scope.

第二步，技能阅读所选内容，识别表达问题，并按所选程度进行修改。
Second, the skill reads the selected content, identifies wording issues, and edits within the chosen level.

第三步，技能对照原稿检查姓名、数字、引文、结论和限定条件，再交付可逐项查看的修改结果。
Third, the skill compares names, numbers, citations, conclusions, and qualifying conditions with the source before delivering reviewable changes.

## 本地命令 / Local commands

复制完整技能文件夹后，可以通过 Windows PowerShell 阅读内置指南和编辑规则。
After copying the complete skill folder, you can read the bundled guide and editing rules from Windows PowerShell.

```powershell
& "<skill-root>/norman-humanize.exe" guide
& "<skill-root>/norman-humanize.exe" list
& "<skill-root>/norman-humanize.exe" read references/rules-common.md
& "<skill-root>/norman-humanize.exe" read references/rules-zh.md
```

| 命令 / Command | 中文用途 | English use |
| --- | --- | --- |
| `inspect` | 读取 Word 文档结构。 | Inspects the Word document structure. |
| `apply` | 根据编辑计划写入修订。 | Applies revisions from an edit plan. |
| `verify` | 检查修订结果。 | Checks the revision result. |

```powershell
& "<skill-root>/norman-humanize.exe" inspect "<input.docx>" --out "<inventory.json>"
& "<skill-root>/norman-humanize.exe" apply "<input.docx>" --plan "<edits.json>" --out "<revised.docx>" --report "<revision-check.json>"
& "<skill-root>/norman-humanize.exe" verify "<input.docx>" --plan "<edits.json>" --revised "<revised.docx>"
```

把 `<skill-root>` 换成技能文件夹路径，并通过各命令的 `--help` 查看参数格式。
Replace `<skill-root>` with the skill folder path, and use each command’s `--help` option for its argument format.

macOS 和 Linux 用户选择与系统及处理器匹配的同名可执行文件。
On macOS and Linux, choose the executable that matches the operating system and processor.

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。
