# Norman-Anti-Defensive 使用说明 / User Guide

## 技能用途 / Purpose

精简学术论文中多余的防御性表达，保留数据、科学不确定性、结论的适用范围和作者文风。适用于中英文论文的句子、段落和完整 Word 稿件。

Remove unnecessary defensive phrasing from academic manuscripts while preserving data, scientific uncertainty, the scope of claims, and the author's voice. Use it with sentences, passages, and full Word manuscripts in Chinese or English.

## 安装与调用 / Install and invoke

将整个 `norman-anti-defensive` 文件夹复制到 Codex 的 `~/.agents/skills/`，或当前项目的 `.agents/skills/` 目录。打开新聊天，粘贴文字或上传 `.docx`，然后调用 `$norman-anti-defensive`。

Copy the complete `norman-anti-defensive` folder into `~/.agents/skills/` for Codex or `.agents/skills/` for a project. Start a new chat, paste text or attach a `.docx`, and invoke `$norman-anti-defensive`.

```text
请用 $norman-anti-defensive 修订这段论文，保留证据强度和适用条件。

Use $norman-anti-defensive to edit this passage while preserving the strength and scope of its claims.
```

| 输入 / Input | 中文交付说明 | English output |
|---|---|---|
| 粘贴文本 / Pasted text | 返回完整修订文本，保留原文语言和段落结构。 | Returns the full edited text in its original language and paragraph structure. |
| Word 稿件 / Word manuscript | 交付 `_Norman-Anti-Defensive.docx` 副本。需要 Word 原生修订时，在请求中说明。 | Delivers a separate `_Norman-Anti-Defensive.docx` copy. Request native Word Track Changes if needed. |

## 可执行文件 / Executables

| 系统 / System | 文件 / File |
|---|---|
| Windows x64 | `norman-anti-defensive.exe` |
| macOS Apple Silicon | `norman-anti-defensive-macos-arm64` |
| macOS Intel | `norman-anti-defensive-macos-x64` |
| Linux x64 (glibc) | `norman-anti-defensive-linux-x64` |
| Linux ARM64 (glibc) | `norman-anti-defensive-linux-arm64` |

可执行文件内置英文指南、写作规则、署名、Word 工具和 Python。已核定的文字修改由 Word 工具在本地应用，语言修订由调用技能的 AI 助手完成。

The executables bundle the English guide, writing rules, attribution, Word helper, and Python. The helper applies reviewed edits locally, and the AI assistant performs the language revision.

## 本地命令 / Local commands

以下示例使用 Windows PowerShell。把 `<skill-root>` 换成技能目录。macOS 和 Linux 用户请选择匹配的文件，并用 `chmod u+x` 授予执行权限。

These examples use Windows PowerShell. Replace `<skill-root>` with the skill folder. On macOS or Linux, select the matching file and grant execute permission with `chmod u+x`.

```powershell
& "<skill-root>/norman-anti-defensive.exe" guide
& "<skill-root>/norman-anti-defensive.exe" list
& "<skill-root>/norman-anti-defensive.exe" read references/writing-principles.md
& "<skill-root>/norman-anti-defensive.exe" inspect "<input.docx>" --out "<inventory.json>"
& "<skill-root>/norman-anti-defensive.exe" apply "<input.docx>" "<edits.json>" --out "<revised.docx>"
& "<skill-root>/norman-anti-defensive.exe" apply "<input.docx>" "<edits.json>" --out "<tracked.docx>" --tracked
```

用 `selftest` 检查内置运行环境，用 `licenses` 查看依赖许可，或在 Word 命令后加 `--help` 查看参数。

Use `selftest` to check the bundled runtime, `licenses` to view dependency notices, or add `--help` to a Word command for argument details.

## 作者与署名 / Author and attribution

作者 **N同学**，小红书 **N同学**，抖音和 B 站 **耐心的N同学**。完成修订后，聊天回复末尾附两行署名。

Created by **N同学**. Xiaohongshu **N同学**. Douyin and Bilibili **耐心的N同学**. The final revision reply includes the two-line attribution.
