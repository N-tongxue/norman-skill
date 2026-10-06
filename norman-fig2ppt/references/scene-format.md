# Native editable PPTX scene format

Read this reference only when invoking `norman-engine build`. Scene JSON contains task-generated geometry, not engine source code. The single-slide canvas width/height must equal the source image's pixel dimensions, with a maximum of 20000. Coordinates, stroke widths, and font sizes use source-image pixels. The engine scales the longest canvas edge to 960 pt. Elements are drawn in array order; later elements appear above earlier ones. Provide every field and do not add undefined fields.

Top-level fields: `width`, `height`, `background` (`#RRGGBB`), `elements`, and `warnings` (an array of strings). Supply 1–15000 elements with unique IDs.

Each element has these fields:

| Field | Value |
|---|---|
| id | Unique string, converted to a `NORMAN_` object name |
| kind | `text`, `rect`, `ellipse`, `line`, `path`, or `crop` |
| x, y, width, height | Source-image coordinates; bounds must remain inside the canvas. Lines may have zero width or height. |
| rotation | Degrees; for a line, 180 means bottom-left to top-right, otherwise top-left to bottom-right |
| fill, stroke | `#RRGGBB` or null; text color uses fill |
| stroke_width | Nonnegative number |
| text | Text, with `\n` for line breaks; use an empty string for non-text elements |
| font, font_size, bold | Font name, positive font size, and Boolean; choose a font available locally on Mac rather than assuming Windows fonts are installed |
| align | `left`, `center`, or `right` |
| arrow_start, arrow_end | Booleans |
| segments | Used for path elements; otherwise `[]` |
| crop_box | `[x1,y1,x2,y2]` for crop elements; otherwise `[]` |
| note | Reason for retaining a crop or another explanation; may be empty |

A path's `segments` is an array of objects with `command` and `coordinates`. Commands `M`, `L`, `C`, and `Z` require 2, 2, 6, and 0 coordinates respectively. A path must start with `M`. Coordinates are relative to the element's top-left corner; `C` contains two control points and an endpoint. Use multiple `M` subpaths for holes or separate contours.

`crop_box` uses absolute source-image coordinates. A crop must not cover 98% or more of the source image area, preventing whole-image substitution for editable reconstruction. Crops preserve aspect ratio and are centered within their element rectangles. The engine outputs the assets and a crop manifest.

Minimal example:

```json
{
  "width": 800, "height": 600, "background": "#FFFFFF", "warnings": [],
  "elements": [
    {
      "id": "title", "kind": "text", "x": 50, "y": 30, "width": 500, "height": 60,
      "rotation": 0, "fill": "#222222", "stroke": null, "stroke_width": 0,
      "text": "Editable text", "font": "Arial", "font_size": 32, "bold": false,
      "align": "left", "arrow_start": false, "arrow_end": false,
      "segments": [], "crop_box": [], "note": ""
    }
  ]
}
```

The `build` output directory must not already exist. Outputs are `NormanFigure.pptx`, `NormanFigure.bas`, `manifest.json`, `draw-order.json`, `report.json`, and any required `assets`. The companion VBA depends on the PPTX from the same build; it is not a standalone geometry generator. `build` does not execute VBA or render PNGs. Export previews separately through PowerPoint or a verified renderer.
