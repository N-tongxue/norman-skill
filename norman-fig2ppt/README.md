# Norman Fig2PPT 使用说明 / User Guide

## 技能用途 / Purpose

Norman Fig2PPT 将科研图、机制图、流程图和截图重建为可编辑的 PowerPoint 对象。
Norman Fig2PPT rebuilds scientific figures, mechanism diagrams, flowcharts, and screenshots as editable PowerPoint objects.

它会分别处理文字、边框、箭头、连接线和简单形状，并将照片或复杂纹理作为局部图片保留。
It handles text, borders, arrows, connectors, and simple shapes separately while retaining photographs or complex textures as local image crops.

## 在 Codex 中使用 / Use in Codex

上传原图，说明希望保留的文字语言、页面尺寸和输出位置，并在请求中写出技能名。
Upload the source image, specify the text language, slide size, and output location you want, and name the skill in your request.

例如，输入“使用 `$norman-fig2ppt` 的 Quick 模式，把这张机制图重建为可编辑 PPTX”。
For example, ask “Use `$norman-fig2ppt` in Quick mode to rebuild this mechanism diagram as an editable PPTX.”

| 模式 / Mode | 中文说明 | English explanation |
| --- | --- | --- |
| Quick | 快速重建主体布局、文字、形状和连线。 | Quickly rebuilds the main layout, text, shapes, and connections. |
| Advanced | 逐个元素记录位置和样式，并对实际渲染结果进行细致比对。 | Records each element’s position and style and compares an actual render in detail. |

如果请求中没有指定模式，技能会请你在 Quick 和 Advanced 之间选择。
If the request does not specify a mode, the skill asks you to choose between Quick and Advanced.

## 工作流程 / Workflow

第一步，提供清晰原图，并指出必须保持准确的标签、数字、图例和连接关系。
First, provide a clear source image and identify labels, numbers, legends, and connections that must remain accurate.

第二步，技能识别可编辑元素与需要裁切保留的图片区域，并把原图坐标映射到幻灯片画布。
Second, the skill identifies editable elements and image regions to retain as crops, then maps source coordinates onto the slide canvas.

第三步，技能生成可编辑 PPTX，并在适用的流程中附带 PowerPoint VBA 模块和元素记录。
Third, the skill generates an editable PPTX and, where applicable, a PowerPoint VBA module and an element record.

第四步，查看输出中的文字、位置、颜色、连线和局部图片，并反馈需要调整的元素。
Fourth, review the output’s text, positions, colors, connections, and image crops, then point out any elements to adjust.

## 本地命令 / Local commands

复制完整技能文件夹后，在 Windows PowerShell 中用以下命令查看内置指南和资源。
After copying the complete skill folder, use the following commands in Windows PowerShell to read its bundled guide and resources.

```powershell
& "<skill-root>/norman-fig2ppt.exe" guide
& "<skill-root>/norman-fig2ppt.exe" list
& "<skill-root>/norman-fig2ppt.exe" read references/scene-format.md
```

| 命令 / Command | 中文用途 | English use |
| --- | --- | --- |
| `probe` | 查看本机可用的重建路径。 | Reports the available reconstruction path. |
| `map` | 计算原图与幻灯片之间的缩放和边距。 | Calculates scaling and margins between the image and slide. |
| `crop` | 提取需要保留的局部图片。 | Extracts image regions to retain. |
| `check` | 检查 VBA 模块。 | Checks a VBA module. |
| `diff` | 比较原图与渲染图。 | Compares the source with a rendered slide. |
| `build` | 读取场景 JSON 并生成原生可编辑 PPTX。 | Reads scene JSON and generates a native editable PPTX. |

使用 `build` 之前，先读取 `references/scene-format.md`。
Read `references/scene-format.md` before using `build`.

```powershell
& "<skill-root>/norman-fig2ppt.exe" probe
& "<skill-root>/norman-fig2ppt.exe" map <image-width-px> <image-height-px> <canvas-width-pt> <canvas-height-pt> --pretty
& "<skill-root>/norman-fig2ppt.exe" build "<scene.json>" --source-image "<source-image>" --output-dir "<new-output-directory>" --pretty
```

把 `<skill-root>` 换成技能文件夹路径，并用 `命令 --help` 查看该命令的完整参数。
Replace `<skill-root>` with the skill folder path, and use `command --help` to see all arguments for a command.

macOS 和 Linux 用户选择与系统及处理器匹配的同名可执行文件，再运行相同的子命令。
On macOS and Linux, choose the executable that matches the operating system and processor, then run the same subcommands.

## 输出内容 / Outputs

主要交付物是可编辑 PPTX，复杂图像区域可作为普通图片对象保留。
The main deliverable is an editable PPTX, with complex image regions retained as ordinary image objects where needed.

Advanced 模式还可附带元素清单、裁片、对照图和视觉调整记录。
Advanced mode can also include an element manifest, crops, comparison images, and a visual refinement record.

### 作者与许可

作者：小红书 **N同学**；抖音 / B站 **耐心的N同学**。
