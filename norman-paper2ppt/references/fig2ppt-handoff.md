# Fig2PPT：简易文字与图片分离

仅用户选择可编辑版时读取本文件。**必须先完成并审核全部完整 AI 页图**；图片版也仍需交付。

## 发现和核实接口

使用本包内置依赖：FIG = S/vendor/norman-fig2ppt，读取 FIG/SKILL.md；无需技能列表中存在单独的 norman-fig2ppt。必须保留完整 vendor 目录，不能只复制 EXE，Windows DLL、Mac 运行时和第三方许可证都属于依赖。Windows 引擎通常为 `FIG/bin/windows-x64/norman-engine.exe`，Mac 为 `FIG/bin/norman-engine`，以实际文件为准。运行 probe 和 help，不依赖记忆中的新参数。

本次重建时已核实当前 Windows 引擎支持 `probe, map, crop, check, diff, run`；**不支持 build，也不支持 check --mode quick**，即使其 SKILL.md 示例写了这些参数。当前 check 只接受 BAS 路径和 `--pretty`；run 接受 BAS、`--macro`、`--output`、`--pretty`。安装更新后以真实 --help 为准，禁止把文档与二进制不一致说成执行成功。

```powershell
$ENGINE = Join-Path $FIG 'bin/windows-x64/norman-engine.exe'
& $ENGINE probe
& $ENGINE map --help
& $ENGINE crop --help
& $ENGINE check --help
& $ENGINE run --help
& $ENGINE map 1920 1080 960 540 --pretty
```

## 分离边界

生成简要元素清单：背景 B（纯色幻灯片背景）、文字 E、局部图片 R；连接和箭头如存在，包含在图片 R 内，不单独重画。全部对象只有：

1. 原生文本框：标题、正文、关键结论、外部图注、页眉页码及封面的水印；正文无技能水印。
2. 普通图片：科研图表、照片、插画、路线图及其他视觉块。图片**内部**文字、坐标轴、图例和箭头保持位图，不进一步分离或矢量化。

必须目视识别文字而不是把未知 OCR 直接交给用户。标注 `text not separable` 不能代替完成外部文字分离；先修改页图或重新布局，使其可以忠实处理。

不要保留含外部正文的完整背景再叠文本；这会重影，也不算分离。选择图块时排除待重建的外部文字。若文字叠在复杂背景，先用实际图像编辑工具生成去除该段文字的局部底图，再将文本框放回；检查图形和科学信息没有改变。保留复杂视觉块不等于对其内部进一步矢量化。

## 局部裁图与测量清单

对每页基于已审定完整页图测量源像素坐标。用真实 `map` 记录像素与点数变换，再使用 `crop` 提取视觉块：

```powershell
& $ENGINE crop "$OUT/slides/01.png" "$OUT/editable/01/assets" --region 'R01:120:260:900:600' --manifest "$OUT/editable/01/crops.json" --pretty
```

上面的坐标仅说明接口，必须用实际测量值替换；裁图路径从真实返回中取得。保留来源矩形、理由、层叠顺序。避免裁掉图例、误差条、图注限定。裁图成功并不代表文字已重建。

每页在 deck.json 中加入下面字段；文字 `font_size`、位置 `box` 均为源图像素，输出按 960/source_width 缩放：

```json
{
  "source_size": [1920, 1080],
  "background": "#F7F8FA",
  "editable_pptx": "editable/01/slide.pptx",
  "objects": [
    {
      "id": "TITLE", "kind": "text", "box": [80,60,1740,100],
      "text": "与最终页图一致且经原文核实的标题",
      "font": "Microsoft YaHei", "font_size": 64,
      "color": "#162D46", "bold": true, "align": "left"
    },
    {
      "id": "FIGURE", "kind": "image", "box": [120,260,900,600],
      "path": "editable/01/assets/R01.png"
    }
  ]
}
```

实际 objects 必须列全该页外部文本，只有封面列两行水印，正文不列技能水印，不能只照抄示例标题。图片与目标框保持比例。`norman-paper2ppt editable-vba` 只接受 text/image，不生成矢量插画；它将人工测量清单编译为 ASCII BAS，中文通过 ChrW 保真，不依赖系统代码页。

## 文本框样式保留

text 对象可增加 `fill_color: "#EEF5F7"` 与 `padding: 16`；padding 使用源图像素，四边一致，输出按 source_size 等比缩放。不设置时沿用透明底与零内边距。填充属于文本框本身，不新增形状；文字、底色、内边距作为同一对象保留。深底框须指定浅色字。分层小标题与正文可用相邻文本框并保持对齐，不能用包含文字的图片冒充可编辑文本。PowerPoint COM 与 VBA 编译器均支持这两个字段。仍不对科学图内部、流程图和插画矢量化。

## 实际调用与完成条件

先完成真实 Fig2PPT map/crop，人工检查分离清单，并生成对应 BAS 交给 Fig2PPT Quick 静态检查：

```powershell
& "$S/bin/windows-x64/norman-paper2ppt.exe" editable-vba "$OUT/deck.json" 1 "$OUT/editable/01/BuildFinal.bas"
& $ENGINE check "$OUT/editable/01/BuildFinal.bas" --pretty
```

逐条看返回值再进行下一条。Quick 是当前任务模式和重建范围，不代表每个二进制都需要 `--mode` 参数。真实 map/crop/check 加上已读取的 Fig2PPT 重建流程才构成调用记录，不能只引用其名字。

**当前 Windows 首选组装路径**：本地 PowerPoint 常规对象接口，不读取或写入 VBA 项目。它使用同一经测量、裁图和检查的 objects 清单，生成真正的文本框和图片，保存并渲染：

```powershell
& "$S/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode editable -Manifest "$OUT/deck.json" -Output "$OUT/paper-editable.pptx" -PreviewDir "$OUT/previews-editable"
& "$S/bin/windows-x64/norman-paper2ppt.exe" audit "$OUT/paper-editable.pptx" "$OUT/deck.json" --kind editable --report "$OUT/audit-editable.json"
```

这条路径仍实际调用了 Fig2PPT 的图像分离辅助接口，但未执行 Fig2PPT 宏运行器；记录真实执行情况，不宣称引擎 run 已成功。用户明确要求仅文字／图片处理，因此它优先于依赖技能的通用 VBA 偏好。

若采用依赖的宏运行器，则实际运行：

```powershell
& $ENGINE run "$OUT/editable/01/BuildFinal.bas" --macro BuildFinal --output "$OUT/editable/01/slide.pptx" --pretty
```

run 返回中区分宏执行和保存状态，并验证 PPTX 存在可读。当前机器实测会返回 `Programmatic access to Visual Basic Project is not trusted`；不要修改宏设置、要求用户降低安全性或反复重试。改用前述常规对象接口即可继续任务。遇到超时或未知执行状态，先核实有无生成文件与新文稿，不重复运行创建多份。新建文稿不需要删除用户文稿对象；静态检查中的 cleanup 提示应按此语义判断，不能为了消除提示删除其他文稿内容。

仅当采用宏路线并已逐页得到单页文件时，合并（`InsertFromFile`），写回讲稿备注，渲染：

```powershell
& "$S/bin/windows-x64/norman-paper2ppt.exe" powerpoint -Mode merge -Manifest "$OUT/deck.json" -Output "$OUT/paper-editable.pptx" -PreviewDir "$OUT/previews-editable"
& "$S/bin/windows-x64/norman-paper2ppt.exe" audit "$OUT/paper-editable.pptx" "$OUT/deck.json" --kind editable --report "$OUT/audit-editable.json"
```

打开各渲染页与原完整图片比较外部文字完整性、位置、无重影、图片保真、边界、封面固定水印及正文无技能水印；必要时重新测量调整。用实际文本对象和图片对象检查可编辑范围。静态通过、成功生成 BAS、probe 或 map 都不是可编辑成品；只有保存的 PPTX、实际对象验证及视觉检查才能支持完成报告。
