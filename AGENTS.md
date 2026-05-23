# AGENTS.md

## Project Overview

This is a collection of standalone **Manim Community v0.20.1** animation scripts for mathematical education videos. Each `.py` file is a self-contained scene, run independently via the Manim CLI. There is no package structure, no dependency files (`pyproject.toml`, `setup.cfg`, etc.), and no automated testing or CI.

Python version: **3.11** (3.8–3.12 supported). Dependency: `manim==0.20.1` (and its transitive deps: numpy, etc.).

## Directory Structure

```
动点最值/        Geometry: moving point optimization problems
动点最值2/       More advanced geometry
公式/            Famous math/physics formulas
函数图像/        Function graphs, 2D/3D parametrics, sorting visualizations
人物画像/        Portraits of mathematicians and scientists
证明和演示/      Proofs and demonstrations (Taylor series, volume proofs)
base/            Empty
Logo.py          (does not exist at root; see 公式/Logo.py for LogoScene)
```

File names use **Chinese characters**; class, method, and variable names are **English**.

## Running a Script

Single script (preview quality, auto-play):
```
manim -p <dir>/<script>.py <ClassName>
```

High-quality render (no preview):
```
manim -qh <dir>/<script>.py <ClassName>
```

The exact CLI command is typically written as a comment at the bottom of each file, e.g.:
```python
# manim -pqh 公式模版.py ImportantFormulas
```

**Note:** Scripts must be run from the **project root** or from within the directory containing the file. Cross-directory imports (e.g. `from Logo import LogoScene`) only work when the script is run from the directory containing the imported module.

## Build / Lint / Test

There is **no** build system, linter, formatter, or test framework configured. Scripts are verified by running them manually with Manim.

To check that a script at least imports correctly (does not crash before rendering):
```
manim -ql <script>.py <ClassName> --disable_caching
```
(Use `-ql` for lowest quality, fastest check.)

## Code Conventions

### Imports

```python
from manim import *       # Always first; wildcard import is the Manim convention
# Optional additional imports (sparingly):
import numpy as np
import math
```

Cross-file intra-project imports use bare module names (no package prefix, no dots):
```python
from Logo import LogoScene   # Only if Logo.py exists in the same directory
```

Do **not** use relative imports (`from .Logo import ...`).

### File Structure

```python
from manim import *
# Module-level config settings (before class definition)
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080

class MyScene(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"  # or "#0F0B1A"
        # ... animation code ...

# manim -pqh <filename>.py MyScene
```

### Naming

| Element | Convention | Example |
|---------|-----------|---------|
| File names | Chinese, no spaces | `动点3.py`, `公式模版.py` |
| Class names | PascalCase, English | `ParabolaPlot`, `ImportantFormulas` |
| Methods | snake_case | `construct()`, `add_logo()` |
| Variables | snake_case | `axis_labels`, `formula_groups_left` |

### Background Colors

Standard dark backgrounds used throughout:
- `#0F0F1A` – deep navy (most common)
- `#0F0B1A` – darker purple-tinged
- `#1F2430` – slate (alternative from readme.txt)

Lighter backgrounds (e.g. `#FFF8E7`) appear in a few scenes.

### LaTeX / Chinese Text

Always set the xelatex compiler for Chinese support:
```python
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
```

For Chinese text labels, use `Text()` with `font="Microsoft YaHei"`:
```python
Text("中文标签", font="Microsoft YaHei", font_size=16, color=YELLOW)
```

For math expressions, use `MathTex()` or `Tex()`.

### Animations

Group multiple animations with `self.play(*anims, run_time=...)`. Common patterns:

```python
# Coordinate conversion from math space to scene space
point = Dot(axes.c2p(x, y), color=RED)

# Label that follows a moving object
label = always_redraw(lambda: Tex("P").next_to(P, UP, buff=0.15))

# Line that updates with moving endpoints
line = always_redraw(lambda: DashedLine(A.get_center(), P.get_center(), color=RED_C))

# Trace a moving point
trace = TracedPath(P.get_center, dissipating_time=1, stroke_color=YELLOW)
self.add(trace)
```

### Error Handling

No exception handling patterns exist. Scripts are short and visual; if something goes wrong, Manim's built-in error messages are the primary debugging tool.

### Type Annotations

**None.** The codebase does not use type hints. Do not add them — the project intentionally forgoes them. Similarly, no docstrings are used (the one exception is `Logo.py`'s `add_logo` method).

### Code Style

- Indentation: 4 spaces
- Lines under ~100 characters (informal)
- Comment style: Chinese comments for section labels within `construct()`, e.g. `# 1. 创建标题`
- No trailing whitespace
- Spaces around operators and after commas (conventional PEP 8-ish)
- List/dict literals use trailing commas on final items in multi-line blocks

### Base Class Usage

Some scenes inherit from `LogoScene` (defined in `公式/Logo.py`) instead of `Scene` to get a watermarked logo in the corner:

```python
from manim import *
from Logo import LogoScene

class MyScene(LogoScene):
    def construct(self):
        self.add_logo()                    # Add logo before main content
        self.camera.background_color = "..."
        # ... animation code ...
```

## Adding a New Script

1. Create a `.py` file in the appropriate subdirectory (use an existing file as template).
2. Define a single `Scene` subclass with a `construct()` method.
3. Add the `manim` CLI command as a comment at the bottom.
4. Run it to verify before committing.

## Git

Add `**/media/` and `**/_pycache_/` to `.gitignore` (already done). Manim renders output to `media/` directories; these should never be committed.
