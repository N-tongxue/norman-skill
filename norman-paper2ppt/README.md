# norman-paper2ppt

**English** · [中文说明](#中文说明)

Created and maintained by **N同学**. Xiaohongshu: **N同学**. Douyin / Bilibili: **耐心的N同学**.

Turn academic paper PDFs into evidence-grounded Chinese research presentations. Read the full paper, organize its research story, preserve original scientific figures, prepare all slide prompts together, and assemble a 16:9 PPTX. The image version is always included; slide-by-slide speaker notes and editable text/image output are optional. The required `norman-fig2ppt` engine and its three-platform runtimes are bundled.

## Installation and invocation

Place the entire `norman-paper2ppt` folder in a host skill directory supporting `SKILL.md`, preserving its structure, or explicitly supply its folder path in a conversation. This package does not automatically install itself globally.

```text
Use $norman-paper2ppt to turn this paper into a research presentation: [local PDF].
Use $norman-paper2ppt for a 5-minute overview, with speaker notes and an editable PPTX: [PDF].
Use $norman-paper2ppt for a 10-minute journal-club presentation, with speaker notes: [PDF].
Use $norman-paper2ppt for a 15-minute deep reading, preserving the paper's original figures: [PDF].
```

`SKILL.md` instructions are English; presentations and speaker notes default to Simplified Chinese. Supporting references retain their Chinese guidance. The skill confirms mode, speaker notes, and editable output **one question at a time**, reusing choices already supplied. Once these choices are complete, it proceeds without additional style or outline approval.

## Modes and visible outputs

| Mode | Duration | Total slides | Approximate narration, when selected |
|---|---|---|---|
| A · Brief overview (`brief`) | 5 minutes | 5–7 | 1,000 Chinese characters |
| B · Standard reading (`standard`) | 10 minutes | 8–12 | 2,000 Chinese characters |
| C · Deep reading (`deep`) | 15 minutes | 12–16 | 3,000 Chinese characters |

The deck uses four parts: **one cover; one combined background / technical approach / data and methods slide; core-results slides; one combined innovation / conclusions / research implications slide**. Total counts include all four parts. Each combined slide contains all three topics. Speaker-note length allows about ±10%; character counts do not guarantee speaking duration.

| Deliverable | Availability | Contents |
|---|---|---|
| `paper-image.pptx` | Always | One embedded complete image per slide, in 16:9 format |
| Final slide images / ZIP | Always | Reviewed slide images in presentation order |
| `speaker-notes.txt` | When selected | Slide-by-slide narration, also written into presenter notes where supported |
| `paper-editable.pptx` | When selected | Native editable external text; ordinary images for scientific visuals |

**Original figures remain the main evidence:** inventory main-text Figures and panels before planning results. Shorter decks prefer two related Figures per slide when readable; longer decks prefer one enlarged Figure per slide. Record omissions instead of claiming unsupported complete coverage. Insert originals directly from PDF extraction or high-resolution crops; do not ask AI to redraw curves, labels, or statistics. No new AI scientific illustrations, photographs, 3D scenes, or decorative icons are added. Simple paper-grounded flowcharts may support the narrative.

The cover places the paper title and bibliographic details on the left and the **real first PDF page** on the right. Designed text boxes, consistent hierarchy, readable original figures, and clear conclusion bands form full compositions. Editable output preserves text-box fills and padding; scientific figures and other complex visuals remain images.

## Batch production and verification

Read the paper once, settle the full deck's content and common style, compile all prompts, generate independent slide drafts continuously, then review the complete set and correct affected slides. AI drafts leave original-figure slots empty; the original files are inserted locally before final rendering. This is orchestration of real image-tool calls, not a separate image-generation batch API. The prompt compiler generates no images itself.

Target native 1920×1080 or higher images, inspect actual dimensions, and disclose resolution limits. Do not present interpolation as native HD. Machine checks cover manifests and PPTX structure; scientific correctness, watermark visibility, figure fidelity, and layout still require visual review. Actual runtime depends on paper complexity, image-tool availability, and the local presentation backend; no fixed production time is guaranteed.

## Windows and Mac helpers

| System | Helper invocation | Runtime selection |
|---|---|---|
| Windows x64 | `bin/windows-x64/norman-paper2ppt.exe` | Standalone Windows executable |
| Mac Apple Silicon | `/bin/sh bin/norman-paper2ppt` | Automatically selects arm64 |
| Mac Intel | `/bin/sh bin/norman-paper2ppt` | Automatically selects x86_64 |

The Mac launcher detects native Apple Silicon even under Rosetta. No separate Python installation or first-run dependency download is required. Mac requires macOS 14 or later for the bundled dependency set. Keep `vendor/norman-fig2ppt` together with the package: Mac helpers share its native interpreter and Pillow.

Windows PowerShell:

```powershell
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" version
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" inspect-pdf "<paper.pdf>" "<output>/source-pages"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" prepare-image-batch "<output>/deck.json" --style "<output>/style.md"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" validate "<output>/deck.json"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode images -Manifest "<output>/deck.json" -Output "<output>/paper-image.pptx" -PreviewDir "<output>/previews-image"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" audit "<output>/paper-image.pptx" "<output>/deck.json" --kind image
```

Mac Terminal:

```bash
/bin/sh "<skill-root>/bin/norman-paper2ppt" version
/bin/sh "<skill-root>/bin/norman-paper2ppt" inspect-pdf "<paper.pdf>" "<output>/source-pages"
/bin/sh "<skill-root>/bin/norman-paper2ppt" prepare-image-batch "<output>/deck.json" --style "<output>/style.md"
/bin/sh "<skill-root>/bin/norman-paper2ppt" validate "<output>/deck.json"
/bin/sh "<skill-root>/bin/norman-paper2ppt" notes "<output>/deck.json" "<output>/speaker-notes.txt"
/bin/sh "<skill-root>/bin/norman-paper2ppt" audit "<output>/paper-image.pptx" "<output>/deck.json" --kind image
```

Replace placeholders with actual paths and quote them. Use `--help` for helper subcommands. `prepare-image-batch` runs before image production; `validate` runs after final images and prompts exist. `notes` requires narration to be selected. PDF inspection does not modify the source PDF; it requires a new output directory. No OCR engine is bundled.

## Runtime requirements and package records

AI reading and image generation use the host's actual tools. Windows assembly and rendering require locally installed Microsoft PowerPoint and PowerShell. Mac assembly requires an available verified native PPTX backend and an actual renderer, as described in [local execution](references/local-execution.md); the `powerpoint` COM subcommand is Windows-only. No image model, Office installation, or universal Mac renderer is bundled.

Author Python is distributed as a Windows executable and compiled bytecode. PowerShell logic is compressed and embedded, then temporarily extracted for execution; this is packaging rather than native PowerShell compilation or irreversible encryption. Third-party source and notices remain where needed.

`PACKAGE-INFO.json` records dependency versions and source fingerprints. `VALIDATION.json` distinguishes the completed Windows checks from Mac static checks; native macOS execution has not been performed on the Windows build host. `SHA256SUMS.json` covers distributed files except itself. The bundled fig2ppt package retains its own licenses and validation history.

---

# 中文说明

`norman-paper2ppt` 由 **N同学**制作和维护。小红书：**N同学**；抖音 / B站：**耐心的N同学**。

将学术论文 PDF 精读为中文科研汇报：阅读全文、梳理证据主线，以论文原图为主要视觉，集中准备整套提示词，再制作与组装 16:9 PPTX。始终交付图片版，可选逐页讲稿和文字、图片可编辑版。所需 `norman-fig2ppt` 引擎及三平台运行时已内置。

## 放置与调用

把整个 `norman-paper2ppt` 文件夹放入支持 `SKILL.md` 的宿主技能目录，保留内部结构；也可以在对话中明确指定文件夹路径。本包不会自动安装到全局目录。

```text
请用 $norman-paper2ppt 将这篇论文制作成科研汇报：[本地 PDF]。
请用 $norman-paper2ppt 做 5 分钟精要速览，需要讲稿和可编辑 PPT：[PDF]。
请用 $norman-paper2ppt 做 10 分钟组会标准解读，附逐页讲稿：[PDF]。
请用 $norman-paper2ppt 做 15 分钟深度研读，保留论文正文原图：[PDF]。
```

`SKILL.md` 指令为英文，PPT 和讲稿默认简体中文，配套参考规范保留中文。技能依次确认汇报模式、是否讲稿、是否可编辑版，**每次只问一个问题**；已经说明的选择不会重复询问。三个选择完成即继续制作，不额外要求风格或提纲批准。

## 模式与交付内容

| 模式 | 时长 | 总页数 | 选择讲稿时的目标字数 |
|---|---|---|---|
| A · 精要速览（`brief`） | 5 分钟 | 5–7 页 | 约 1,000 个汉字 |
| B · 标准解读（`standard`） | 10 分钟 | 8–12 页 | 约 2,000 个汉字 |
| C · 深度研读（`deep`） | 15 分钟 | 12–16 页 | 约 3,000 个汉字 |

PPT 固定采用四部分结构：**封面 1 页；研究背景、技术路线与数据方法合并 1 页；核心结果多页；研究创新、研究结论与研究启示合并为最后 1 页**。总页数包含上述所有部分，两张合并页均完整覆盖三个主题。讲稿字数允许约 ±10%，实际演讲时长仍受语速影响。

| 交付文件 | 提供条件 | 内容 |
|---|---|---|
| `paper-image.pptx` | 始终提供 | 每页一张嵌入式完整图片，16:9 |
| 最终逐页图片／ZIP | 始终提供 | 按演示顺序保存、已审核的页面图片 |
| `speaker-notes.txt` | 选择讲稿时 | 逐页讲述正文，并尽量写入对应演讲者备注 |
| `paper-editable.pptx` | 选择可编辑版时 | 外部文字为原生文本框，科研图等视觉保留普通图片 |

**以论文正文原图承载证据**：先清点正文 Figure 和面板，再规划结果页。页少时优先两张相关 Figure 一页，页多时优先一张 Figure 一页并放大；可读性优先，未展示内容记录原因。原图来自 PDF 提取或高清渲染裁切，直接保真置入，不让 AI 重画曲线、猜标签或更改统计。禁止新增 AI 科学插画、照片、3D 场景和装饰图标，可用基于论文的简洁流程图辅助解释。

封面左侧为题名与题录，右侧为论文 **真实 PDF 第 1 页**。通过充分放大的原图、统一文字层级、浅色实底解释框和结论带形成丰满页面。可编辑版保留文本框底色和内边距；科研图及复杂视觉仍为普通图片。


## 批量制作与检查

精读一次并确定整套内容与统一风格，集中编译全部提示词，连续生成各页独立初稿，再统一检查和定向修正问题页。AI 底稿为原图留空，之后直接置入原始文件并渲染最终页图。批量指真实图像调用的编排；提示词编译程序本身不生成图片。

目标为原生 1920×1080 或更高，检查实际像素并披露尺寸限制，不以插值冒充原生高清。机器检查覆盖清单和 PPTX 结构，科学准确、原图保真、水印可见与页面排版仍须目视审核。实际耗时取决于论文复杂度、图像工具与本地后端，不承诺固定制作时间。

## Windows 与 Mac 调用

| 系统 | 辅助程序入口 | 运行时选择 |
|---|---|---|
| Windows x64 | `bin/windows-x64/norman-paper2ppt.exe` | 独立 Windows 程序 |
| Mac Apple Silicon | `/bin/sh bin/norman-paper2ppt` | 自动选择 arm64 |
| Mac Intel | `/bin/sh bin/norman-paper2ppt` | 自动选择 x86_64 |

同一文件夹包含三平台支持。Mac 在 Rosetta 下也会识别原生 Apple Silicon。无需另装 Python，首次运行不下载依赖；内置依赖要求 macOS 14 或更高版本。请完整保留 `vendor/norman-fig2ppt`，Mac 辅助程序复用其中的解释器和 Pillow。

Windows PowerShell：

```powershell
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" version
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" inspect-pdf "<paper.pdf>" "<output>/source-pages"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" prepare-image-batch "<output>/deck.json" --style "<output>/style.md"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" validate "<output>/deck.json"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode images -Manifest "<output>/deck.json" -Output "<output>/paper-image.pptx" -PreviewDir "<output>/previews-image"
& "<skill-root>/bin/windows-x64/norman-paper2ppt.exe" audit "<output>/paper-image.pptx" "<output>/deck.json" --kind image
```

Mac 终端：

```bash
/bin/sh "<skill-root>/bin/norman-paper2ppt" version
/bin/sh "<skill-root>/bin/norman-paper2ppt" inspect-pdf "<paper.pdf>" "<output>/source-pages"
/bin/sh "<skill-root>/bin/norman-paper2ppt" prepare-image-batch "<output>/deck.json" --style "<output>/style.md"
/bin/sh "<skill-root>/bin/norman-paper2ppt" validate "<output>/deck.json"
/bin/sh "<skill-root>/bin/norman-paper2ppt" notes "<output>/deck.json" "<output>/speaker-notes.txt"
/bin/sh "<skill-root>/bin/norman-paper2ppt" audit "<output>/paper-image.pptx" "<output>/deck.json" --kind image
```

将占位符替换为实际路径并加引号，子命令参数可用 `--help` 查看。制图前运行 `prepare-image-batch`，最终图片和提示词齐全后再运行 `validate`；`notes` 仅在选择讲稿后执行。PDF 检查不会修改源论文，输出目录必须为新目录；包内不含 OCR 引擎。

## 运行条件与打包记录

AI 阅读和制图仍需宿主提供真实工具。Windows 组装与渲染需要本机 Microsoft PowerPoint 和 PowerShell；Mac 需要已核实的原生 PPTX 后端及实际渲染器，详见 [本地执行说明](references/local-execution.md)。`powerpoint` COM 子命令仅适用于 Windows。包内不含图像模型、Office 安装包或通用 Mac 渲染器。

作者 Python 以 Windows EXE 和编译字节码交付；PowerShell 逻辑压缩封装，运行时临时执行。这属于打包封装，不等于 PowerShell 原生编译或不可逆加密。第三方依赖源码和许可证按需保留。

`PACKAGE-INFO.json` 记录依赖版本及源码指纹；`VALIDATION.json` 区分已完成的 Windows 检查和 Mac 静态检查，本 Windows 构建机未进行 Mac 实机运行；`SHA256SUMS.json` 覆盖除自身以外的分发文件。内置 fig2ppt 保留其许可证与验证历史。
