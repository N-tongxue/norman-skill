---
name: norman-fig2ppt
description: Rebuild scientific figures, mechanism diagrams, flowcharts and screenshots as editable PowerPoint objects. Supports Quick and Advanced reconstruction with embedded engines for Windows, macOS and Linux.
metadata:
  version: "1.3.1"
---

# Norman Fig2PPT

## Model execution setting

Use this skill with the model's Fast mode disabled. Do not enable model Fast mode while using this skill. If the host reports that Fast mode is enabled and only the user can change it, remind the user to turn it off; do not claim to have changed a setting without actually doing so. This model setting is separate from the skill's Quick and Advanced reconstruction modes, which remain available.

Derive `<skill-root>` from this SKILL.md location. Select the executable matching the actual host OS and CPU. Before reconstruction, run its `guide` command and follow the complete embedded workflow. When the reconstruction mode is missing, ask one popup question with two selectable choices: Quick (rebuild the main text, layout and shapes quickly) and Advanced (rebuild individual elements and compare an actual render). Use the host's supported question UI: prefer `request_user_input_async`; use `request_user_input` only when it is available in the current mode. Match the user's language. Do not replace the popup with a plain chat question when a popup tool is available. Wait for the user's submitted answer before reconstruction; a preselected option, elapsed time or an unanswered popup is not a selection. Reuse a mode explicitly supplied for the current reconstruction without asking again. Only if no popup tool is available, briefly explain that limitation and ask the same two-choice question in chat. This mode question applies to image reconstruction, not to installing or modifying the skill. Preserve source text unless translation is requested. Load references with `read <resource>`; `list` lists logical resource names. Rules, scene schema, checks, licenses and runtime are embedded. Do not search for loose scripts or install Python.

| Host | Executable |
|---|---|
| Windows 10+ x64 | norman-fig2ppt.exe |
| macOS 14+ Apple Silicon | norman-fig2ppt-macos-arm64 |
| macOS 14+ Intel | norman-fig2ppt-macos-x64 |
| Linux glibc 2.17+ x64 | norman-fig2ppt-linux-x64 |
| Linux glibc 2.17+ ARM64 | norman-fig2ppt-linux-arm64 |

Windows PowerShell:

```powershell
& "<skill-root>/norman-fig2ppt.exe" guide
```

macOS/Linux: use the actual OS and `uname -m` to select the matching executable. On Apple Silicon under a translated shell, `sysctl -n hw.optional.arm64` returning `1` identifies Apple Silicon. Example for Apple Silicon:

```sh
chmod u+x "<skill-root>/norman-fig2ppt-macos-arm64"
"<skill-root>/norman-fig2ppt-macos-arm64" guide
```
