---
name: norman-anti-defensive
description: Edit academic manuscripts to remove unnecessary defensive phrasing while preserving scientific accuracy, uncertainty, scope, and authorial voice. Use for sentences, passages, and Word manuscripts, including abstracts, introductions, results, and conclusions. Includes Windows, macOS, and Linux executables.
metadata:
  version: "1.0.0"
---

# Norman-Anti-Defensive

Find `<skill-root>` from this file's location. Select the executable matching the host operating system and processor, then run `guide` to load the complete editing and delivery instructions. Use the same executable with `read <resource>` for each reference named in the guide. The writing rules, attribution, Word helper, and Python runtime are bundled.

| Host | Executable |
|---|---|
| Windows x64 | `norman-anti-defensive.exe` |
| macOS Apple Silicon | `norman-anti-defensive-macos-arm64` |
| macOS Intel | `norman-anti-defensive-macos-x64` |
| Linux x64 (glibc) | `norman-anti-defensive-linux-x64` |
| Linux ARM64 (glibc) | `norman-anti-defensive-linux-arm64` |

Run this command in Windows PowerShell.

```powershell
& "<skill-root>/norman-anti-defensive.exe" guide
```

On macOS or Linux, substitute the matching executable name. The example uses Apple Silicon. Check the host architecture with `uname -m`. If macOS is running a translated shell, `sysctl -n hw.optional.arm64` returning `1` identifies Apple Silicon.

```sh
chmod u+x "<skill-root>/norman-anti-defensive-macos-arm64"
"<skill-root>/norman-anti-defensive-macos-arm64" guide
```

The AI client performs the editorial work in the manuscript's language. The local commands load guidance and apply reviewed Word edits.
