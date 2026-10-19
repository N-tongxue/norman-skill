# 本地执行与文件约定

## 运行时与能力检查

所有示例中的 S、OUT、FIG 是任务实际发现的绝对路径变量；不是工具中的字面参数，不硬编码用户名。本包已内置 norman-fig2ppt 引擎及其专用运行时（vendor/norman-fig2ppt），同时内置 paper2ppt 辅助程序运行时，不包含图像模型或 PowerPoint，不声称离线一键完成 AI 工作。内置图像工具不要求自行配置 API 密钥。本包脚本无网络调用。

当前 Windows 路线：编译入口内置 Pillow、pypdf、pypdfium2，系统需注册 Microsoft PowerPoint COM，norman-fig2ppt 从本包 vendor/norman-fig2ppt 调用。以执行时能力为准。

```powershell
& "$S/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode probe
& "$S/bin/windows-x64/norman-paper2ppt.exe" inspect-pdf "$PDF" "$OUT/source-pages"
```

PowerShell 使用 UTF-8 读 JSON。建议 PowerShell 7；旧 Windows PowerShell 读脚本时注意 UTF-8 编码。本包 PowerShell 脚本主体为 ASCII，中文内容均从 UTF-8 JSON 读取。不得全局改执行策略。若平台要求，可在当前获准进程中执行脚本；不要关闭 Office 宏保护。

macOS：使用本地已核实的原生 PPTX 后端（如环境提供的 `@oai/artifact-tool`，先读实际文档）来嵌入整页图片、写备注并保存；本包内封装的 PowerShell COM 逻辑只支持 Windows。可编辑版发现并读取 Fig2PPT 的 Mac `scene-format.md`，先查看 `build --help`，场景仅含 `text` 和局部 `crop` 两类元素及纯色背景，逐页构建再用已核实后端合并。引擎本身不渲染，需另找真实渲染器。不要把 Windows 命令伪称跨平台；没有后端时如实报告并交付已有图片和讲稿。

Mac 的辅助程序使用 `/bin/sh "$S/bin/norman-paper2ppt" <子命令>`；以下 PowerShell 示例只适用于 Windows。Mac 可用同名 PDF、提示词、校验、讲稿和审计子命令；组装与渲染遵循上面的本地后端约定。

## 工作目录

```text
paper2ppt-<short-name>-<timestamp>/
  deck.json
  # 九类分析保存在 deck.json.analysis；详细分析文件仅按需导出
  evidence.json
  # 分镜直接保存在 deck.json.slides，不重复写一份
  style.md
  image-batch.json    # 由提示词编译脚本产生的独立页面调用队列
  generation-log.json # 真实调用与文件保存进度，执行时填写
  source-pages/       # PDF 文本、整页渲染
  figures/            # 原图和选用面板，保留来源坐标
  prompts/01.txt ...
  generated/          # 原始工具输出及修订，不混作最终图片
  slides/01.png ...   # 审核后的完整高清图片，仅封面烘焙两行水印
  editable/           # 仅选择可编辑版时，局部图片、对象清单、BAS、逐页 PPTX
  previews-image/    # 实际 PowerPoint 渲染
  previews-editable/
  qa.json
  paper-image.pptx
  paper-editable.pptx # 可选
  speaker-notes.txt   # 可选
```

## deck.json 约定

UTF-8 JSON，路径相对 deck.json 所在目录，也接受绝对路径。模式固定为 `brief`／`standard`／`deep`。下面仅展示第一页的数据形状；真实任务需按选定模式填满全部页面。不得将示例当已生成的成果。

页数范围恢复为 brief 5–7、standard 8–12、deep 12–16。section 序列严格为「封面」→「研究背景、技术路线与数据方法」→若干「核心结果」→「研究创新、研究结论与研究启示」。封面、研究概览、综合总结各恰好 1 页，其余 N−3 页全部是结果页。概览页 topics 必须为 ["研究背景", "技术路线", "数据方法"]；末页 topics 必须为 ["研究创新", "研究结论", "研究启示"]。title 写具体统领观点。校验器检查字段，实际图中三个主题的完整性须目视核实。

```json
{
  "mode": "standard",
  "narration": true,
  "editable": false,
  "slides": [
    {
      "number": 1,
      "section": "封面",
      "title": "经过精读确定的页面标题",
      "cover_paper_image": {"path": "source-pages/page-001.png", "pdf_page": 1, "side": "right"},
      "image_brief": "逐字文案：……。输入图像1是论文真实首页。布局：左侧题名与题录，右侧完整首页图；具体构图、层级和科学限定在此一次写定。",
      "reference_images": [],
      "seconds": 30,
      "evidence_ids": ["E001"],
      "image": "slides/01.png",
      "prompt": "prompts/01.txt",
      "notes": "本页完整讲述内容"
    }
  ]
}
```

选择可编辑版时每页增加实际像素尺寸 `source_size: [width,height]`、`background: "#F7F8FA"`、`objects`；不要把示例 1920×1080 当成真实尺寸。仅采用单页引擎输出再合并的路线时需要 `editable_pptx`。字段详见 Fig2PPT handoff。`notes` 只放逐页讲稿正文，不包含元数据、证据表或制作记录；不需要讲稿时用空串或省略。

封面中的真实论文首页图像在最终完整图片中已经位于右侧；可编辑 objects 中也需有对应普通图片对象，优先引用原始 `cover_paper_image.path` 并保持比例，不拆其内部文字。来源记录不是完成证据，必须目视核对最终页图中的实际位置与保真情况。

图片生成前，先一次写完全部页面的 image_brief 和参考文件清单，再运行 `norman-paper2ppt prepare-image-batch`（见 [快速批量制图](batch-production.md)）编译提示词并实际执行图像队列。完成所有页生成和集中审核后，才执行以下依赖最终页图的 validate 和组装。编译脚本不会调用模型，不能替代真实图片生成。

text 对象支持可选 `fill_color`（#RRGGBB）与 `padding`（源图像素、四边一致）；用于保留解读框和结论框的底色及内边距。两字段均省略时保持透明底、零内边距。仅原生文本框加普通图片，不增加形状描摹。

## 图片版组装、讲稿、渲染与检查

```powershell
& "$S/bin/windows-x64/norman-paper2ppt.exe" validate "$OUT/deck.json" --report "$OUT/manifest-check.json"
# validate 返回 0 后继续；失败应先修复，不忽略。
& "$S/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode images -Manifest "$OUT/deck.json" -Output "$OUT/paper-image.pptx" -PreviewDir "$OUT/previews-image"
& "$S/bin/windows-x64/norman-paper2ppt.exe" audit "$OUT/paper-image.pptx" "$OUT/deck.json" --kind image --report "$OUT/audit-image.json"
# 仅选择讲稿时执行：
& "$S/bin/windows-x64/norman-paper2ppt.exe" notes "$OUT/deck.json" "$OUT/speaker-notes.txt"
```

组装脚本对新输出和渲染目录拒绝覆盖；纠错后请指定 `-v2` 等新文件／目录。插入图片使用 LinkToFile=False、SaveWithDocument=True，960×540 pt 整页嵌入；讲稿写入 NotesPage 的 body placeholder。脚本只关闭其自己打开／创建的文稿，绝不退出用户的整个 PowerPoint 或改变其安全设置。

若只要重新渲染现有文件：

```powershell
& "$S/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode render -InputDeck "$OUT/paper-image.pptx" -PreviewDir "$OUT/previews-image-v2"
```

`validate` 的原生分辨率不足默认报告 warning，不能据此声称达到高清；用户明确要求原生 1920×1080 时用 `--strict-hd`，达不到时披露，不反复重生碰运气。科学正确、实际可读、精确 16:9 和不拉伸仍须通过。

`audit --kind image` 根据真实幻灯片关系顺序检查页数、16:9、每页仅一张图、图像整页定位、图像媒体与已审核文件 SHA256 一致、无外链、讲稿备注一致。若 PowerPoint 压缩改变媒体，检查失败需核实是否影响保真，并避免压缩后重做；不可直接忽略媒体不一致。

`audit --kind editable` 检查实际原生文本、标题、封面两行水印及正文无技能水印、对象数量、近全页底图、非允许对象及讲稿备注。该检查不执行 OCR，不知道原图文字是否仍藏在局部图片中，不检查字体实际渲染和文字重影；必须逐页目视核对。

脚本返回非零表示失败。PowerPoint 可能已保存文件而渲染失败，必须区分报告中的 `saved`、文件存在与渲染成功，不盲目重跑覆盖已有文件。COM 失败时保留真实错误；不要把启动软件／静态检查说成已经完成 PPTX。

## 交付范围

为 `slides/` 创建 ZIP 便于一次下载，保留有序文件名。最终响应链接最终图片版、可选可编辑版、图片 ZIP 和可选讲稿即可；不用在响应罗列内部证据表。若完整流程被真实能力阻塞，清楚标记已完成和未完成项目，绝不交付空文件、代码或图片版冒充完成的可编辑版。

论文分析回复与最终交付回复末尾，还须按 SKILL.md 第 5 节输出两行可见文字水印；输出文件中的水印不能替代聊天水印。
