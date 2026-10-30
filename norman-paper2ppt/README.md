# norman-paper2ppt

**English** · [中文说明](#中文说明)

Created and maintained by **N同学**. Xiaohongshu: **N同学**. Douyin / Bilibili: **耐心的N同学**.

Turn academic paper PDFs into evidence-grounded Chinese research presentations. Read the full paper, organize its research story, preserve original scientific figures, prepare all slide prompts together, and assemble a 16:9 PPTX. The image version is always included; slide-by-slide speaker notes and editable text/image output are optional. Version **1.1.0** packages the full workflow, references, helpers, Fig2PPT and Python runtime inside five native executables, matching the single-file distribution style of `norman-humanize`. No separate Python installation or first-run dependency download is required.

## Installation and invocation

Place the entire `norman-paper2ppt` folder in a host skill directory supporting `SKILL.md`, or explicitly supply its folder path in a conversation. This package does not automatically install itself globally.

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

---

# 中文说明

`norman-paper2ppt` 由 **N同学**制作和维护。小红书：**N同学**；抖音 / B站：**耐心的N同学**。

将学术论文 PDF 精读为中文科研汇报：阅读全文、梳理证据主线，以论文原图为主要视觉，集中准备整套提示词，再制作与组装 16:9 PPTX。始终交付图片版，可选逐页讲稿和文字、图片可编辑版。完整流程与 Fig2PPT 引擎均已封装到五平台可执行程序中。

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