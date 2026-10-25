# norman-humanize

**English** · [中文说明](#中文说明)

Created and maintained by **N同学**. Xiaohongshu: **N同学**. Douyin / Bilibili: **耐心的N同学**.

Edit Chinese and English writing to remove empty framing, mechanical phrasing, repetition, and formatting residue while preserving meaning, facts, evidence, and the writer's voice. Suitable for academic papers and reports, formal correspondence, social media, and everyday drafts. Pasted text uses visible insertions and deletions by default; complete Word documents receive real tracked changes that can be accepted or rejected.

Version **1.3.2** includes executable packages for Windows x64, Mac Apple Silicon, Mac Intel, Linux x64, and Linux ARM64. Editing instructions, reference material, attribution, and the local Word helper are embedded in the executables. No separate Python installation or first-run dependency download is required. An AI client performs the language editing; this package does not include an AI model.

## Installation and invocation

Place the entire `norman-humanize` folder in a host skill directory supporting `SKILL.md`, or explicitly supply its folder path in a conversation. The host must be able to execute local commands. This package does not automatically install itself globally.

```text
Use $norman-humanize to edit this abstract, preserving terminology, numbers, and citations: [text].
Use $norman-humanize for a light edit of this academic paragraph, showing all insertions and deletions: [text].
Use $norman-humanize for a standard edit of this email: [text].
Use $norman-humanize to review this complete Word manuscript and deliver a real tracked-change DOCX: [local DOCX].
```

The entry instructions are English; questions and editing follow the user's language. The client selects the executable for the actual host OS and CPU, reads its embedded `guide`, and loads the relevant embedded references. Do not run the Windows `.exe` on macOS or Linux. A client that cannot execute local programs cannot load the full embedded workflow.

## Configuration before editing

Confirm the missing settings before rewriting. When the host supports selectable questions, collect them together in one popup request. Choices already supplied are reused for the current text or document; a new batch requires new configuration unless the user explicitly requests carryover.

| Setting | Choices |
|---|---|
| Text type | Automatic identification; academic paper or report; formal business or administrative writing; social media or everyday writing |
| Editing level | Light; standard; deep |
| Scope for pasted or plain text | All supplied text; specified paragraphs |
| Scope for a complete Word document | All editable body content, including headings, abstracts, and narrative table text; body paragraphs only; specified sections |

Light editing is recommended for academic, legal, and technical prose; standard editing otherwise. Recommendations and preselected options are not submitted choices. A personal writing sample is optional. If selectable questions are unavailable, the client explains the limitation and asks in chat. Once configuration is complete, editing proceeds without an additional permission-to-start question.

## Editing levels and visible outputs

| Level | Changes allowed |
|---|---|
| Light | Correct specific language problems while preserving paragraph order, headings, lists, and sections |
| Standard | Revise problem sentences and necessary neighboring wording; sentence order may change within a paragraph |
| Deep | When explicitly selected, reorganize sentences and paragraphs while preserving distinct information and evidence relationships |

People, organizations, numbers, units, terminology, citations, qualifications, and the strength of claims remain protected. Clear, natural passages may remain unchanged; there is no required edit quota.

| Input | Default deliverable | Verification |
|---|---|---|
| Pasted text or plain text | Visible `~~deletions~~` and `**insertions**`; unchanged text remains plain | Rejecting edits restores the supplied text; accepting them yields the reviewed draft |
| Complete `.docx` | A new file with real Word insertion/deletion revisions | Accept/reject checks and preservation checks; layout review when rendering is available |

Replacements appear as `~~original wording~~**revised wording**`. If inline markers would damage code, formulas, or formatting, use an original/revised comparison. A clean copy or separate report is added only on request.

The original Word file is preserved. Chinese requests use `<original-stem>-norman-修订版.docx`; other languages use a localized revision suffix. Colored text, strikethrough, comments, or merely enabling Word's tracking switch do not substitute for real revision records. Existing revisions and unsupported complex structures require explicit handling rather than silent reconstruction.

## Windows, Mac, and Linux executables

| System | Executable |
|---|---|
| Windows 10 or later, x64 | `norman-humanize.exe` |
| macOS 13 or later, Apple Silicon | `norman-humanize-macos-arm64` |
| macOS 13 or later, Intel | `norman-humanize-macos-x64` |
| Linux with glibc 2.17 or later, x64 | `norman-humanize-linux-x64` |
| Linux with glibc 2.17 or later, ARM64 | `norman-humanize-linux-arm64` |

These are native executables for their respective systems. macOS and Linux files do not use the `.exe` extension. The Linux builds target glibc distributions; musl/Alpine and other CPU architectures are outside this release. On macOS/Linux, use the actual OS and `uname -m` to select the file. On Apple Silicon under Rosetta, `sysctl -n hw.optional.arm64` reporting `1` identifies the native Apple Silicon architecture.

Windows PowerShell:

```powershell
& "<skill-root>/norman-humanize.exe" version
& "<skill-root>/norman-humanize.exe" selftest
& "<skill-root>/norman-humanize.exe" guide
& "<skill-root>/norman-humanize.exe" inspect "<input.docx>" --out "<output>/inventory.json"
& "<skill-root>/norman-humanize.exe" apply "<input.docx>" --plan "<output>/edits.json" --out "<output>/revised.docx" --report "<output>/revision-check.json"
& "<skill-root>/norman-humanize.exe" verify "<input.docx>" --plan "<output>/edits.json" --revised "<output>/revised.docx"
```

Mac Terminal, Apple Silicon example; substitute `norman-humanize-macos-x64` on Intel:

```sh
chmod u+x "<skill-root>/norman-humanize-macos-arm64"
"<skill-root>/norman-humanize-macos-arm64" version
"<skill-root>/norman-humanize-macos-arm64" selftest
"<skill-root>/norman-humanize-macos-arm64" guide
"<skill-root>/norman-humanize-macos-arm64" inspect "<input.docx>" --out "<output>/inventory.json"
```

Linux Terminal, x64 example; substitute `norman-humanize-linux-arm64` on ARM64:

```sh
chmod u+x "<skill-root>/norman-humanize-linux-x64"
"<skill-root>/norman-humanize-linux-x64" version
"<skill-root>/norman-humanize-linux-x64" selftest
"<skill-root>/norman-humanize-linux-x64" guide
"<skill-root>/norman-humanize-linux-x64" inspect "<input.docx>" --out "<output>/inventory.json"
```

Replace placeholders with actual paths and quote them. `apply` and `verify` take the same arguments on all platforms. Each Word subcommand supports `--help`. The AI client prepares the edit plan from the reviewed text; users do not need to write XML or manually construct a plan. The helper refuses to overwrite the source or an existing output.

---

# 中文说明

`norman-humanize` 由 **N同学**制作和维护。小红书：**N同学**；抖音 / B站：**耐心的N同学**。

用于中英文写作修改，处理空泛表述、机械句式、重复和格式残留，同时保留原意、事实、证据与作者文风。适用于学术论文与报告、正式事务、自媒体和日常文字。粘贴文字默认展示可见增删；完整 Word 文档交付可以接受或拒绝的真实修订稿。

**1.3.2 版**包含 Windows x64、Mac Apple Silicon、Mac Intel、Linux x64 与 Linux ARM64 五种可执行程序。编辑指令、参考规范、署名和本地 Word 辅助工具均已内嵌，无需另装 Python，首次运行不下载依赖。实际语言修改由 AI 客户端完成，包内不包含 AI 模型。

## 放置与调用

把完整 `norman-humanize` 文件夹放入支持 `SKILL.md` 的宿主技能目录，或在对话中明确指定文件夹路径。宿主需要具备执行本地命令的能力。本包不会自动安装到全局目录。

```text
请用 $norman-humanize 修改这段摘要，保留术语、数据和引用：[文字]。
请用 $norman-humanize，轻度修改这段论文，显示全部增删：[文字]。
请用 $norman-humanize，标准修改这封邮件：[文字]。
请用 $norman-humanize 处理这篇完整 Word，交付真实修订稿：[本地 DOCX]。
```

入口指令为英文，实际提问与修改跟随用户语言。客户端根据真实操作系统和 CPU 选择程序，先读取内嵌 `guide`，再按需加载内部参考规范。Mac 和 Linux 使用各自的原生程序，不运行 Windows `.exe`。不能执行本地程序的客户端无法加载完整内嵌流程。

## 修改前的配置

改写前确认缺失设置。宿主支持可选问题时，在一次弹窗请求中集中收集。本次已明确的选项不重复询问；新文字、新文档重新确认，除非用户明确要求沿用。

| 设置 | 选项 |
|---|---|
| 文本类型 | 智能识别；学术论文或报告；正式事务；自媒体或日常 |
| 修改程度 | 轻度；标准；深度 |
| 粘贴文字或纯文本范围 | 全部所提供文字；指定段落 |
| 完整 Word 范围 | 全部可编辑正文，含标题、摘要和表格叙述文字；仅正文段落；指定章节 |

学术、法律和技术文本推荐轻度，其他文字推荐标准。推荐与界面预选不算用户确认。个人文风样本可选，不是必答项。没有可选问题工具时，客户端说明限制后在聊天中提问。设置齐全后直接开始，不额外询问是否启动。

## 修改程度与交付内容

| 档位 | 修改范围 |
|---|---|
| 轻度 | 修改明确存在问题的语言片段，保留段落顺序、标题、列表与章节 |
| 标准 | 修改问题句及必要邻句，可调整同一段内的句子顺序 |
| 深度 | 明确选择后可重组句子与段落，保留独立信息和证据关系 |

人物、机构、数字、单位、术语、引用、限定条件与论断强度均需保留。清楚自然的内容可以原样保留，不设修改比例。

| 输入 | 默认交付 | 核验方式 |
|---|---|---|
| 粘贴文字或纯文本 | 用 `~~删除~~`、`**新增**` 标记实际变化，未改部分正常显示 | 拒绝修改可还原原文，接受修改得到审核后的文本 |
| 完整 `.docx` | 新建带真实 Word 增删修订的文件 | 核验接受与拒绝结果、包部件保留情况；具备渲染条件时检查版面 |

替换显示为 `~~原表述~~**新表述**`。代码、公式或原有格式不适合嵌入标记时，使用完整原文／修改后对照。净稿或单独报告仅在明确要求时增加。

完整 Word 保留原件。中文请求的输出名称为 `<原文件名>-norman-修订版.docx`，其他语言使用对应的本地化修订后缀。红字、删除线、批注或仅打开修订开关，均不能代替真实修订记录。已有修订与复杂结构需要明确处理，不能静默清理或重建全文。

## Windows、Mac 与 Linux 调用

| 系统 | 可执行文件 |
|---|---|
| Windows 10 或更高，x64 | `norman-humanize.exe` |
| macOS 13 或更高，Apple Silicon | `norman-humanize-macos-arm64` |
| macOS 13 或更高，Intel | `norman-humanize-macos-x64` |
| Linux，glibc 2.17 或更高，x64 | `norman-humanize-linux-x64` |
| Linux，glibc 2.17 或更高，ARM64 | `norman-humanize-linux-arm64` |

各文件均为对应系统的原生可执行程序；Mac 和 Linux 程序没有 `.exe` 后缀。本版 Linux 面向 glibc 发行版，不包含 musl/Alpine 和其他 CPU 架构。Mac/Linux 根据真实系统和 `uname -m` 选择文件；Apple Silicon 在 Rosetta 环境下可用 `sysctl -n hw.optional.arm64` 判断原生架构，返回 `1` 表示 Apple Silicon。

Windows PowerShell：

```powershell
& "<skill-root>/norman-humanize.exe" version
& "<skill-root>/norman-humanize.exe" selftest
& "<skill-root>/norman-humanize.exe" guide
& "<skill-root>/norman-humanize.exe" inspect "<input.docx>" --out "<output>/inventory.json"
& "<skill-root>/norman-humanize.exe" apply "<input.docx>" --plan "<output>/edits.json" --out "<output>/revised.docx" --report "<output>/revision-check.json"
& "<skill-root>/norman-humanize.exe" verify "<input.docx>" --plan "<output>/edits.json" --revised "<output>/revised.docx"
```

Mac 终端，以下以 Apple Silicon 为例；Intel 将文件名替换为 `norman-humanize-macos-x64`：

```sh
chmod u+x "<skill-root>/norman-humanize-macos-arm64"
"<skill-root>/norman-humanize-macos-arm64" version
"<skill-root>/norman-humanize-macos-arm64" selftest
"<skill-root>/norman-humanize-macos-arm64" guide
"<skill-root>/norman-humanize-macos-arm64" inspect "<input.docx>" --out "<output>/inventory.json"
```

Linux 终端，以下以 x64 为例；ARM64 将文件名替换为 `norman-humanize-linux-arm64`：

```sh
chmod u+x "<skill-root>/norman-humanize-linux-x64"
"<skill-root>/norman-humanize-linux-x64" version
"<skill-root>/norman-humanize-linux-x64" selftest
"<skill-root>/norman-humanize-linux-x64" guide
"<skill-root>/norman-humanize-linux-x64" inspect "<input.docx>" --out "<output>/inventory.json"
```

将占位符替换为真实路径并加引号。各平台 `apply`、`verify` 使用相同参数，Word 子命令支持 `--help`。修改计划由 AI 客户端根据审核后的文本准备，用户无需自行编写 XML 或构造计划。辅助工具拒绝覆盖源文件和已有输出。
