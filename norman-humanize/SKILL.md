---
name: norman-humanize
description: Edit Chinese and English prose to remove AI writing tells while preserving facts and voice. Supports visible text edits and real Word tracked changes. Includes Windows, macOS and Linux executables.
metadata:
  version: "1.3.2"
---

# Norman Humanize

Select the executable matching the actual host OS and CPU. Derive `<skill-root>` from this SKILL.md location. Before editing or diagnosing text, run that executable with `guide` and follow the complete embedded instructions. Load every reference it requires using `read <resource>`; `list` shows resource names. Configuration questions, editing rules, attribution, licenses, and Word helpers are embedded. Do not look for loose rules/scripts or install Python.

| Host | Executable |
|---|---|
| Windows 10+ x64 | norman-humanize.exe |
| macOS 13+ Apple Silicon | norman-humanize-macos-arm64 |
| macOS 13+ Intel | norman-humanize-macos-x64 |
| Linux glibc 2.17+ x64 | norman-humanize-linux-x64 |
| Linux glibc 2.17+ ARM64 | norman-humanize-linux-arm64 |

Windows PowerShell:

```powershell
& "<skill-root>/norman-humanize.exe" guide
```

macOS/Linux: use the host OS and `uname -m` to select the corresponding file. On an Apple Silicon machine running a translated shell, `sysctl -n hw.optional.arm64` reporting 1 identifies Apple Silicon. The example is for Apple Silicon; substitute the matching filename for other hosts:

```sh
chmod u+x "<skill-root>/norman-humanize-macos-arm64"
"<skill-root>/norman-humanize-macos-arm64" guide
```
