# Norman Manuscript Audit 使用说明 / User Guide

## 技能用途 / Purpose

Norman Manuscript Audit 用于科研论文投稿前检查，覆盖文字校对、页面排版、图表可读性、编号、交叉引用和参考文献格式。
Norman Manuscript Audit reviews research manuscripts before submission, covering proofreading, layout, figure and table readability, numbering, cross-references, and reference formatting.

## 在 Codex 中使用 / Use in Codex

将完整技能文件夹复制到项目的 `.agents/skills` 或用户的 `~/.codex/skills`，然后在新聊天中调用 `$norman-manuscript-audit`。
Copy the complete skill folder into the project's `.agents/skills` or the user's `~/.codex/skills`, then invoke `$norman-manuscript-audit` in a new chat.

例如，输入“使用 `$norman-manuscript-audit` 对附件做简易检查，直接开始。”
For example, ask “Use `$norman-manuscript-audit` to run a Simple review of the attached manuscript. Start directly.”

## 检查流程 / Review workflow

提供稿件后，如果范围尚未明确，技能会请你选择检查模式。已指定模式或具体范围时直接开始。
Once a manuscript is supplied, the skill asks for a mode if the scope is unclear. It starts directly when you specify a mode or a focused scope.

| 模式 / Mode | 中文说明 | English explanation |
| --- | --- | --- |
| 简易检查 / Simple | 检查排印错误、排版、图表、编号、交叉引用及参考文献格式。 | Checks typographic errors, layout, figures and tables, numbering, cross-references, and reference formatting. |
| 深度检查 / Deep | 在格式检查基础上审查创新性、方法、数据、统计、结果、结论、证据及可复现性。经授权可逐条核验参考文献真实性。 | Adds review of novelty, methods, data, statistics, results, conclusions, evidence, and reproducibility. References can be verified individually with authorization. |

## 交付内容 / Deliverables

报告汇总核实后需要修改的问题、对应位置、修改建议和关键问题的复检办法。深度检查按实际发现补充结构化问题清单。
The report lists verified issues, locations, proposed fixes, and retest steps for significant findings. Deep review adds structured issue lists when warranted.

## 本地命令 / Local commands

在 Windows x64 的 PowerShell 中使用内置程序查看指南、资源和命令参数。PDF 文本提取和报告校验依赖已打包。
Use the bundled executable in PowerShell on Windows x64 to read the guide, resources, and command arguments. The dependencies for PDF text extraction and report validation are bundled.

```powershell
& "<skill-root>/norman-manuscript-audit.exe" guide
& "<skill-root>/norman-manuscript-audit.exe" list
& "<skill-root>/norman-manuscript-audit.exe" read references/local-tools.md
```

| 命令 / Command | 中文用途 | English use |
| --- | --- | --- |
| `extract` | 从稿件及补充材料中提取内容和位置。 | Extracts content and source locations from manuscripts and supplements. |
| `consistency` | 筛查数字、图表引用、缩写和占位符。 | Screens for numeric, figure/table reference, abbreviation, and placeholder issues. |
| `bibliography` | 筛查引文和 DOI，获得授权后可查询 Crossref。 | Screens citations and DOIs, with Crossref lookup when authorized. |
| `validate` | 校验结构化问题清单和可选的 Markdown、CSV 报告。 | Validates structured issues and optional Markdown and CSV reports. |

```powershell
& "<skill-root>/norman-manuscript-audit.exe" extract manuscript.md -o extracted.json
& "<skill-root>/norman-manuscript-audit.exe" consistency extracted.json -o candidates.json
& "<skill-root>/norman-manuscript-audit.exe" bibliography extracted.json -o references.json
& "<skill-root>/norman-manuscript-audit.exe" validate issues.json --markdown audit_report.md --csv issues.csv
```

把 `<skill-root>` 换成技能文件夹路径，使用各命令的 `--help` 查看全部参数。将输出写入独立的审计目录。
Replace `<skill-root>` with the skill folder path and use `--help` after each command for its arguments. Write outputs to a separate audit directory.

Windows x64 用户使用 `norman-manuscript-audit.exe`。macOS 和 Linux 用户按系统和处理器选择下表中的同名文件。
Use `norman-manuscript-audit.exe` on Windows x64. On macOS and Linux, choose the file matching your system and processor.

| 平台 / Platform | 可执行文件 / Executable |
| --- | --- |
| Windows x64 | `norman-manuscript-audit.exe` |
| macOS Apple Silicon | `norman-manuscript-audit-macos-arm64` |
| macOS Intel | `norman-manuscript-audit-macos-x64` |
| Linux ARM64 | `norman-manuscript-audit-linux-arm64` |
| Linux x64 | `norman-manuscript-audit-linux-x64` |

macOS 和 Linux 版本使用系统的 `tar`，Linux 版本面向 glibc 发行版。
The macOS and Linux builds use the system `tar`. The Linux builds target glibc-based distributions.

macOS 和 Linux 可在终端运行。例如，在 Apple Silicon Mac 上，从技能目录执行以下命令。如果通过 ZIP 下载后执行权限丢失，先运行 `chmod +x`。
On macOS and Linux, run the helper from a terminal. For example, use the following commands from the skill folder on an Apple Silicon Mac. If a ZIP download drops executable permissions, run `chmod +x` first.

```sh
chmod +x ./norman-manuscript-audit-macos-arm64
./norman-manuscript-audit-macos-arm64 guide
./norman-manuscript-audit-macos-arm64 read references/local-tools.md
```

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。
