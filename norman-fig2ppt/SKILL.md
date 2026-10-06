---
name: norman-fig2ppt
description: "Rebuild scientific figures, mechanism diagrams, flowcharts, and screenshots as editable PowerPoint objects. Choose Quick or Advanced mode before starting unless already specified. Bundled local engines for Windows x64 and macOS Apple Silicon/Intel."
---

# norman-fig2ppt

Before reconstruction, ask whether to use **Quick** or **Advanced** mode and wait for the answer. If the user has already requested quick, advanced, high-fidelity, or element-by-element reconstruction, use the corresponding mode without asking again. Default to English for prompts, explanations, reports, and generated code comments, and to PowerPoint as the output host. Preserve the source image's text unless the user requests translation; honor the user's explicit language, layout, and save-location choices. If Excel or Word is explicitly requested, generate VBA for that host; the bundled runner supports PowerPoint only.

## Select the engine for the current system

Derive the skill root from the absolute path of this SKILL.md; do not hardcode a username or installation location. Determine the operating system first: on Windows, use `bin/windows-x64/norman-engine.exe` with PowerShell's `&` and a quoted absolute path; on macOS, use `/bin/sh "<skill-root>/bin/norman-engine"`. The Mac launcher automatically selects the bundled Apple Silicon or Intel runtime. Users do not need to install Python, a compiler, or MCP, and the engine does not download dependencies on first launch. Do not run the EXE on Mac, call system Python, or use Windows DLLs as Mac runtime libraries.

Windows examples:

```powershell
& "<skill-root>/bin/windows-x64/norman-engine.exe" probe
& "<skill-root>/bin/windows-x64/norman-engine.exe" map <image-width-px> <image-height-px> <canvas-width-pt> <canvas-height-pt> --pretty
& "<skill-root>/bin/windows-x64/norman-engine.exe" crop "<source-image>" "<assets-directory>" --region "R01:x:y:w:h" --manifest "<crop-manifest.json>" --pretty
& "<skill-root>/bin/windows-x64/norman-engine.exe" check "<module.bas>" --mode advanced --pretty
& "<skill-root>/bin/windows-x64/norman-engine.exe" diff "<source-image>" "<rendered-image>" --mode advanced --pretty
& "<skill-root>/bin/windows-x64/norman-engine.exe" run "<module.bas>" --macro BuildFinal --output "<new-output.pptx>" --pretty
```

Invoke the equivalent Mac commands through the launcher:

```bash
/bin/sh "<skill-root>/bin/norman-engine" probe
/bin/sh "<skill-root>/bin/norman-engine" map <image-width-px> <image-height-px> <canvas-width-pt> <canvas-height-pt> --pretty
/bin/sh "<skill-root>/bin/norman-engine" crop "<source-image>" "<assets-directory>" --region "R01:x:y:w:h" --manifest "<crop-manifest.json>" --pretty
/bin/sh "<skill-root>/bin/norman-engine" check "<module.bas>" --mode advanced --pretty
/bin/sh "<skill-root>/bin/norman-engine" diff "<source-image>" "<rendered-image>" --mode advanced --pretty
```

`check` and `diff` accept `quick` or `advanced` modes. Each subcommand supports `--help`; `probe` takes no arguments. `crop --regions-json` accepts an array with name, x, y, width, height, and optional reason fields. A nonzero exit code means failure. Passing a static check does not establish successful macro execution.

## Reconstruct and verify

Inspect the source image and distinguish editable text, borders, arrows, and simple shapes from photographs or textures that need local crops. Record source coordinates for complex crops and preserve their aspect ratios. Do not substitute a full-image background for reconstruction. Flag low-confidence text. Run `probe`, then use `map` for consistent scaling and margins when positioning objects.

**Quick mode:** Create a brief element map (B: background, E: editable elements, R: retained crops, L: connections). Rebuild the main structure, text, and arrows; crop complex regions. Generate a complete `.bas` module with `BuildFinal` as the main procedure and, where feasible, `BuildSkeleton`. Run the quick static check and generate the finished output.

**Advanced mode:** First create a manifest recording each element's ID, type, treatment, source rectangle, text/style, and stacking order. For arrows, record endpoints, associated objects, and connection sides. Verify the skeleton before adding details. Name objects with the `NORMAN_` prefix; rerun cleanup must affect only that prefix. Bind connectors to shapes where possible. Preserve the source stacking order, generate the finished output, actually render it, and run advanced `diff`. Check text, proportions, positions, connections, colors, and omissions individually. Use SSIM only as a diagnostic. Normally use at most six refinement rounds; stop after two consecutive rounds without improvement. If improvement continues and specific corrections remain, allow at most nine rounds.

On Windows, prefer PowerPoint VBA and the local macro runner. The runner creates and displays a new presentation without changing security settings; report execution and saving separately. If only WPS is available, use the basic Shapes API and do not claim verified WPS compatibility.

On Mac, prefer direct native PPTX generation: read [scene-format.md](references/scene-format.md), interpret the image with Codex, create measured scene JSON, and run:

```bash
/bin/sh "<skill-root>/bin/norman-engine" build "<scene.json>" --source-image "<source-image>" --output-dir "<new-output-directory-that-does-not-exist>" --pretty
```

This path does not require Office or VBA execution. Text, shapes, connectors, and Bézier curves are editable native objects; photographs and textures are retained only as local crops. The companion `.bas` depends on the PPTX generated in the same build. The engine neither interprets nor uploads images: Codex supplies image understanding and scene data. The engine does not generate preview PNGs; export them separately through local PowerPoint or a verified renderer. Choose locally available fonts rather than assuming Windows fonts exist on Mac.

## Optional Mac VBA workflow

When VBA is explicitly requested, use Mac-compatible PowerPoint Shapes APIs and POSIX paths. Avoid Windows COM, ActiveX, kernel32, Sleep, and drive-letter paths. Mac does not support Windows COM module import. Call the runner only when the user provides a `.pptm` with the task macro already imported:

```bash
/bin/sh "<skill-root>/bin/norman-engine" run "<module.bas>" --presentation "<template-with-imported-task-macro.pptm>" --macro BuildFinal --output "<new-output.pptx>" --pretty
```

The runner executes the specified macro already in the template; it does not import the supplied `.bas`. Check the installed PowerPoint scripting terminology, use a working copy, and attempt execution once without changing permissions or macro security settings. Do not automatically retry after a timeout or an unknown execution state. Report `macro_executed` and `saved` separately. A missing template returns `manual_import_required` and must not be described as success. Mac Office automation has not been tested on a real Mac by the current Windows build host; if blocked, continue delivering a native PPTX.

## Deliverables

List paths to the editable output, companion `.bas`, actual crops, manifest, and diagnostic previews. Explain the editable scope, retained images, and actual macro execution/save status. For Advanced mode, include a visual verification record. Explicitly state when rendering was not performed; do not present probing, static checks, or a preview as a finished editable output. Do not include the tool's working process in generated files.
