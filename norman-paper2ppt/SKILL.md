---
name: norman-paper2ppt
description: Turn academic paper PDFs into Chinese research presentations with original figures, optional speaker notes and editable text/image PPTX. Includes embedded helpers and Fig2PPT for Windows, macOS and Linux.
metadata:
  version: "1.1.0"
---

# Norman Paper2PPT

Derive `<skill-root>` from this SKILL.md location. Select the executable matching the actual host OS and CPU. Before reading a paper or producing slides, run its `guide` command and follow the complete embedded workflow. Load the required references using `read <resource>`; `list` shows logical resource names. The guide confirms missing presentation mode, speaker notes and editable output one question at a time, reusing choices already supplied. All full instructions, references, attribution, helpers, Fig2PPT and runtimes are embedded. Do not search for loose scripts or install Python.

| Host | Executable |
|---|---|
| Windows 10+ x64 | norman-paper2ppt.exe |
| macOS 14+ Apple Silicon | norman-paper2ppt-macos-arm64 |
| macOS 14+ Intel | norman-paper2ppt-macos-x64 |
| Linux glibc 2.17+ x64 | norman-paper2ppt-linux-x64 |
| Linux glibc 2.17+ ARM64 | norman-paper2ppt-linux-arm64 |

Windows PowerShell:

```powershell
& "<skill-root>/norman-paper2ppt.exe" guide
```

Mac/Linux: select using the real OS and `uname -m`. On Apple Silicon under Rosetta, `sysctl -n hw.optional.arm64` returning 1 identifies Apple Silicon. Example for Apple Silicon:

```sh
chmod u+x "<skill-root>/norman-paper2ppt-macos-arm64"
"<skill-root>/norman-paper2ppt-macos-arm64" guide
```

The host AI client interprets the paper and generates layouts with its image tool. No AI model is bundled. Optional editable output uses `fig2ppt <command>` in the same executable and Quick text/images only; load `read vendor/norman-fig2ppt/guide.md` when selected. Windows assembly/rendering requires local PowerPoint; Mac/Linux require a verified presentation backend and renderer. No separate Python installation or first-run download is needed. Mac/Linux builds have static checks pending native execution; Mac files are not Developer ID signed or notarized. Linux musl/Alpine is outside this release.
