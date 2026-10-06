# norman-fig2ppt

**Turn scientific figures into editable PowerPoint objects.**  
**把科研图片重建为可编辑的 PowerPoint 对象。**

A Codex skill for scientific figures, mechanism diagrams, flowcharts, and screenshots, with bundled local engines for Windows and Mac.  
面向科研图、机制图、流程图与截图的 Codex 技能，内置 Windows 与 Mac 本地运行引擎。

**Windows x64 · macOS Apple Silicon · macOS Intel**  
**Quick / Advanced · English by default · No separate Python installation**

[English](#english) · [简体中文](#简体中文)

## English

### What you can do

Rebuild the structure of an existing figure so you can edit its labels, boxes, arrows, and simple graphics in PowerPoint. Photographs, textures, and complex regions can remain as local image crops. The aim is a usable editable figure that preserves the source layout.

- Editable text, shapes, and connections; the Mac native PPTX workflow also supports editable Bézier paths.
- **Quick mode** for the main structure, text, and arrows, with local crops for complex regions.
- **Advanced mode** for measured element reconstruction, a manifest, skeleton checks, and visual refinement when a renderer is available.
- Supporting VBA, crop assets, manifests, and diagnostic records as applicable to the selected workflow.

The skill's instructions and prompts are in English. Source-image text is preserved unless you ask for translation; you can still request a different response or output language.

### Install

1. Extract the package and keep the complete `norman-fig2ppt` folder, including `bin`, `agents`, and `references`.
2. Copy that folder to the user skills directory recognized by your Codex version:

   | Platform | Current documented user location | Existing installations using `.codex/skills` |
   |---|---|---|
   | Windows | `%USERPROFILE%\.agents\skills\norman-fig2ppt` | `%USERPROFILE%\.codex\skills\norman-fig2ppt` |
   | macOS | `~/.agents/skills/norman-fig2ppt` | `~/.codex/skills/norman-fig2ppt` |

3. Keep one active copy. When replacing an older version, move the old folder outside the skills directory first, then copy the new folder rather than merging them.
4. If the skill does not appear, restart Codex.

The current documented user location is `~/.agents/skills`; this local setup has also used `.codex/skills`. See the [official Codex skills guide](https://learn.chatgpt.com/docs/build-skills). Copying this distribution does not automatically install or update an active skill.

### Start with an image

Attach an image in Codex and enter:

> Use $norman-fig2ppt in Advanced mode to rebuild this image as an editable PowerPoint. Preserve the original text and layout, and save the result to my desktop.

For a faster first version:

> Use $norman-fig2ppt in Quick mode to rebuild this image as an editable PowerPoint.

If you leave the mode unspecified, the skill asks you to choose before starting. It does not ask again when your request already specifies a mode.

### Choose a mode

| | Quick | Advanced |
|---|---|---|
| Best for | A faster editable first version | A closer reconstruction of a detailed figure |
| Reconstruction | Main structure, text, arrows, and local crops | Measured objects, styles, stacking order, and connections |
| Verification | Quick static checks | Manifest and skeleton checks, plus rendered comparison when available |
| Refinement | Focus on essential elements | Usually up to 6 rounds; at most 9 if improvement continues |

Both modes use editable objects where practical. Complex image regions may remain raster crops, and unclear source text is flagged for review.

### Platform requirements

| Platform | Default workflow | Requirements |
|---|---|---|
| Windows x64 | Generate VBA and run it in local PowerPoint | PowerPoint installed; macro execution permitted by its existing security settings |
| macOS Apple Silicon / Intel | Generate native editable PPTX from a measured scene | macOS 14 or later for the bundled dependencies; Office is not required for generation |

The Mac launcher selects the matching architecture automatically. The package includes its runtime dependencies; you do not need to install Python, a compiler, or MCP. No dependencies are downloaded on first engine launch.

On Mac, PowerPoint or another verified local renderer is needed to view/export previews for visual comparison. The engine itself does not create preview PNGs. If you specifically need VBA execution on Mac, first import the task macro into a `.pptm` template and provide that template. The Mac runner executes an existing macro rather than importing `.bas` files, and it does not change permissions or macro security settings.

### What you receive

Depending on the platform and mode, delivery includes the editable `.pptx`, companion `.bas`, retained crops, an element manifest, and available diagnostic previews or visual verification records.

The Mac native `build` command outputs:

```text
output/
├── NormanFigure.pptx
├── NormanFigure.bas
├── manifest.json
├── draw-order.json
├── report.json
└── assets/              # When local crops are needed
```

Keep the Mac-generated `.bas` with its companion PPTX: it depends on that presentation rather than independently rebuilding the geometry. Macro execution, saving, and rendering are reported separately. A static check alone does not prove that a macro ran or that the finished slide was visually verified.

### How it works and validation status

Codex interprets your image and prepares the geometry, text, and reconstruction data. The local engine maps coordinates, crops assets, checks VBA, compares images, and runs the supported output workflow. It is not a standalone automatic image-recognition application.

The package itself does not upload your images or connect to an author-operated backend. Codex still operates under its normal network requirements and data settings.

Windows behavioral checks have passed. Both Mac architectures have undergone archive, hash, architecture, and library checks; the Mac author bytecode and native PPTX generation were tested on Windows. **Execution on a real Mac, Mac PowerPoint automation, and Gatekeeper first launch have not been verified; the package is not Apple-notarized.** See [PACKAGE-INFO.json](PACKAGE-INFO.json) and [VALIDATION.json](VALIDATION.json) for the recorded scope.

If macOS blocks first launch, follow its system controls to allow the application; do not disable global Gatekeeper. Keep the distribution intact when extracting or copying. The skill invokes the launcher through `/bin/sh`; if executable permissions were lost during transfer, the launcher repairs only its bundled interpreter's permission.

### Author and licenses

Created by **N Tongxue** on Xiaohongshu (**N同学**), and **Naixin de N Tongxue** on Douyin / Bilibili (**耐心的N同学**).

Third-party notices are included in `THIRD_PARTY_LICENSES` and the bundled runtime license directories. Windows uses the existing Nuitka-compiled engine; Mac author code is distributed as CPython bytecode without the original author `.py` files or private build scripts. Bytecode and binaries can be reverse-engineered; the package makes no strong source-secrecy or DRM guarantee.

## 简体中文

### 能做什么

将现有图片中的文字、框线、箭头和简单图形重建为 PowerPoint 对象，方便后续修改内容、调整布局和重新配色。照片、纹理与复杂区域可保留为局部裁片，在尽量还原原图的同时提供实用的可编辑结果。

- 支持可编辑文字、图形与连线；Mac 原生 PPTX 路径还支持可编辑 Bézier 曲线。
- **Quick（快速）模式**：重建主要结构、文字与箭头，复杂区域保留局部裁片。
- **Advanced（高级）模式**：按测量数据逐元素重建，记录清单、检查骨架，并在有可用渲染器时进行视觉对比与细化。
- 按所选流程交付配套 VBA、裁片素材、元素清单和诊断记录。

技能指令与提示统一使用英文，默认以英文沟通；图片中的原始文字保持原文，除非你明确要求翻译。你仍可指定其他回复语言或输出语言。

### 安装方法

1. 解压安装包，保留完整的 `norman-fig2ppt` 文件夹，包括 `bin`、`agents` 和 `references`。
2. 将整个文件夹复制到当前 Codex 版本识别的用户级技能目录：

   | 平台 | 当前官方文档的用户级位置 | 使用 `.codex/skills` 的现有安装 |
   |---|---|---|
   | Windows | `%USERPROFILE%\.agents\skills\norman-fig2ppt` | `%USERPROFILE%\.codex\skills\norman-fig2ppt` |
   | macOS | `~/.agents/skills/norman-fig2ppt` | `~/.codex/skills/norman-fig2ppt` |

3. 只保留一个活动副本。更新旧版本时，先把旧目录移到技能目录之外备份，再放入新目录，避免直接合并留下旧文件。
4. 如果技能没有显示，重启 Codex。

当前官方文档使用 `~/.agents/skills`，本机现有环境也曾使用 `.codex/skills`。详情见 [Codex 官方技能说明](https://learn.chatgpt.com/docs/build-skills)。修改或复制发布包不会自动安装或更新活动技能。

### 从一张图片开始

在 Codex 中附上图片，然后输入：

> 使用 $norman-fig2ppt 的 Advanced 高级模式，把这张图重建为可编辑 PowerPoint，保留原始文字和布局，保存到桌面。

如果希望先快速得到可编辑初稿：

> 使用 $norman-fig2ppt 的 Quick 快速模式，把这张图重建为可编辑 PowerPoint。

没有指定模式时，技能会先询问并等待你的选择；已经指定模式时直接开始，不会重复询问。

### 两种模式怎么选

| | Quick 快速模式 | Advanced 高级模式 |
|---|---|---|
| 适合场景 | 尽快获得可编辑初稿 | 更接近原图的细致重建 |
| 重建内容 | 主要结构、文字、箭头与局部裁片 | 测量后的对象、样式、层级与连接关系 |
| 检查方式 | 快速静态检查 | 元素清单与骨架检查；有可用渲染器时进行渲染对比 |
| 细化轮次 | 优先完成核心元素 | 通常最多 6 轮；持续改善时最多 9 轮 |

两种模式都会尽量使用可编辑对象。复杂图像区域可能仍以位图裁片保留；无法可靠识别的文字会标明，便于你核对。

### 平台与运行要求

| 平台 | 默认流程 | 要求 |
|---|---|---|
| Windows x64 | 生成 VBA 并在本机 PowerPoint 中执行 | 已安装 PowerPoint，现有安全设置允许宏执行 |
| macOS Apple Silicon / Intel | 根据测量后的场景数据直接生成原生可编辑 PPTX | 内置依赖要求 macOS 14 或更新；生成文件无需 Office |

Mac 启动器自动选择对应架构。包内已包含运行组件，无需另装 Python、编译器或 MCP；引擎首次启动不会下载依赖。

Mac 上的预览导出与视觉对比需要 PowerPoint 或其他已验证的本地渲染器，引擎本身不生成预览 PNG。如明确需要在 Mac 执行 VBA，请先把任务宏导入 `.pptm` 模板并提供该文件。Mac 运行器执行模板已有的宏，不自动导入 `.bas`，也不会更改权限或宏安全设置。

### 交付内容

根据平台与模式，交付可编辑 `.pptx`、配套 `.bas`、保留的局部裁片、元素清单，以及实际生成的诊断预览或视觉核对记录。

Mac 原生 `build` 命令输出：

```text
output/
├── NormanFigure.pptx
├── NormanFigure.bas
├── manifest.json
├── draw-order.json
├── report.json
└── assets/              # 需要局部裁片时生成
```

Mac 生成的 `.bas` 依赖同次生成的 PPTX，请一起保留；它不是独立重建全部几何的脚本。宏执行、文件保存和实际渲染会分别报告，静态检查通过不能代替宏运行成功或视觉验收。

### 工作方式与验证状态

Codex 负责理解图片，并准备几何、文字与重建数据；本地引擎负责坐标映射、素材裁切、VBA 检查、图像对比和对应的输出流程。它并不是脱离 Codex 的自动识图软件。

本包本身不上传你的图片，也不连接作者后台；Codex 仍按其正常联网要求与数据设置工作。

Windows 行为检查已通过。Mac 两种架构已完成归档、哈希、架构与运行库检查；Mac 作者字节码和原生 PPTX 生成已在 Windows 上验证。**真实 Mac 执行、Mac PowerPoint 自动化和 Gatekeeper 首次启动尚未验证，本包也未经过 Apple 公证。** 具体范围见 [PACKAGE-INFO.json](PACKAGE-INFO.json) 与 [VALIDATION.json](VALIDATION.json)。

如果 macOS 首次启动时阻止程序，请通过系统提供的控制项允许打开，不要关闭全局 Gatekeeper。解压和复制时保持目录完整。技能通过 `/bin/sh` 调用启动器；如传输导致可执行权限丢失，启动器只修复包内解释器的权限。

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。

第三方组件许可保存在 `THIRD_PARTY_LICENSES` 和各内置运行环境的许可目录。Windows 保持现有 Nuitka 编译引擎；Mac 作者代码以 CPython 字节码分发，不包含作者原始 `.py` 或私有构建脚本。字节码与二进制均可能被逆向，本包不提供强源码保密或 DRM 保证。
