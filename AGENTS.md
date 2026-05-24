# AGENTS.md

## What this repo is

A 30-minute talk: **"Adopting Agentic Coding"** targeting mid-level developers.  
There is **no build system, no package manager, no CI, no test suite**.

## Main artifact

`presentation.html` — a single self-contained HTML file (inline CSS + JS, no external framework).  
Open it directly in a browser. Needs internet access for Google Fonts (`Lora`, `Plus Jakarta Sans`).

## Directory map

| Path                                         | Purpose                                                 |
| -------------------------------------------- | ------------------------------------------------------- |
| `presentation.html`                          | The live deck (single source of truth for slides)       |
| `docs/agentic-coding-presentation-design.md` | Slide-by-slide outline (9 slides, two 15-min parts)     |
| `raw/*.md`                                   | Source notes per topic — feed these into slide edits    |
| `raw/images/`                                | Local image assets referenced by `presentation.html`    |
| `design/working_with_design.md`              | Visual/design guidance                                  |
| `code_architecture/`                         | Architecture reference docs (React, NestJS, file-level) |
| `intent-driven-development/`                 | Supplementary concept material                          |
| `resources.md`                               | External references                                     |
| `scripts/`                                   | Python utility scripts for presentation editing         |
| `scripts idea.md`                            | Ideas for potential demo scripts                        |

## Skills

A `presentation-design` skill is installed at `.agents/skills/presentation-design/SKILL.md`.  
Load it when reviewing or editing the deck — it provides an evaluation framework and anti-pattern checklist.  
`skills-lock.json` tracks installed skills; update it if adding new ones.

## Workflow

1. **Edit content** → update the relevant `raw/*.md` note first, then reflect changes in `presentation.html`.
2. **Edit structure/outline** → `docs/agentic-coding-presentation-design.md` is the reference outline.
3. **Edit slides** → modify `presentation.html` directly; all slide logic and styling is inline.
4. **Check images** → image paths like `raw/images/contextwindow.svg` are relative; keep assets in `raw/images/`.

## Gotchas

- `GEMINI.md` existed as a prior agent instruction file but has been deleted; treat this file as the canonical one.
- `presentation.html` has built-in speaker notes, slide sorter, and keyboard/touch navigation — do not break the inline JS when editing slides.
- No linting or formatting enforcement; consistency is manual.
