# HTML Artifact Skill

[中文 README](README.zh-CN.md)

The HTML Artifact workflow turns agent output from a text-only plan into a readable, interactive, reviewable work surface.

The core idea is not to replace Markdown with HTML. It is:

> When the output is meant to help a human understand, compare, decide, review, or adjust something, prefer an HTML Artifact.

Markdown is still right for short text, lightweight notes, README drafts, and simple explanations. HTML is better for complex information, visualization, interaction, review, sharing, and decision support.

An HTML artifact can be maintained as a first-class source file. Do not assume every HTML page must be generated from Markdown. When editing, publishing, or reviewing an existing HTML artifact, preserve the HTML itself and treat Markdown as optional history, appendix material, or an export format.

Presentation style inspired by [trq212's X post](https://x.com/trq212/status/2052809885763747935). The previews below are checked into this repo so the README remains useful even when remote embeds fail.

## What It Looks Like

### Gallery hub

[![Gallery hub preview](assets/readme/gallery-hub.svg)](examples/gallery/index.html)

A hub page indexes every sub-artifact, supports inline preview in an embedded iframe panel, and propagates the active language to embedded children. Every sub-artifact links back to the hub from its topbar and auto-hides that link when it is being rendered inside the hub's iframe.

[Open hub HTML](examples/gallery/index.html) · [Prompt examples](examples.md#hub-page-with-sub-artifacts)

### Decision report

[![Decision report preview](assets/readme/decision-report.svg)](examples/gallery/decision-report.html)

Cards, evidence matrices, bilingual controls, and export actions turn a long answer into a decision surface.

[Open demo HTML](examples/gallery/decision-report.html) · [Prompt examples](examples.md#general)

### Interactive review

[![Interactive review preview](assets/readme/filter-interaction.svg)](examples/gallery/interactive-review.html)

Search, filters, and export controls let users inspect only the findings that matter.

[Open demo HTML](examples/gallery/interactive-review.html) · [Prompt examples](examples.md#pr-review)

### Formula-heavy report

[![Formula report preview](assets/readme/formula-report.svg)](examples/gallery/formula-report.html)

Metric definitions and equations are rendered as readable math blocks with narrow-screen fallbacks.

[Open demo HTML](examples/gallery/formula-report.html) · [Prompt examples](examples.md#formula-heavy-report)

## Methodology

### HTML-first content

When input comes from Markdown, logs, JSON, tables, or mixed notes, convert the useful content into browser-native HTML as the main reading surface:

- Render headings, lists, tables, quotes, code blocks, diagrams, and links as HTML.
- Do not hide the full content inside an `Original Markdown Source Appendix`.
- If source auditability matters, add evidence or raw-data sections, but do not make them the primary reading path.
- Prefer export controls for HTML, JSON, Prompt, Diff, or structured data. Offer Markdown export only as a compatibility option.

### Bilingual output

Durable artifacts and documentation sites should maintain both English and Chinese reading paths:

- Single-file artifact: include a `中文` / `English` switch or two top-level language views in the same HTML file.
- Multi-page site: maintain parallel routes, for example English at the public entry and Chinese in a linked `zh-CN` route or file.
- Set language attributes correctly: `<html lang="en">` and `<html lang="zh-CN">`.
- Indexes or manifests should record bilingual paths explicitly, such as `html_en` and `html_zh`.
- If a translation is incomplete, still create the other-language entry and mark unfinished sections clearly.

### Math and formulas

When a page includes metrics, scoring rules, probability, sets, or algorithm definitions, render formulas as math, not as plain code blocks:

- Prefer LaTeX delimiters: inline `\(...\)`, display `\[...\]` or `$$...$$`.
- Use aligned display blocks for multi-line metric definitions so equal signs scan vertically.
- Existing plain formula blocks such as `<div class="formula">...</div>` may preserve source text while upgrading the browser view with MathJax or equivalent rendering.
- Formula regions need horizontal-scroll fallbacks so narrow screens do not break the page.

### Hub + sub-pages

When an HTML artifact has more than one page, give it a hub and make navigation reversible:

- The hub is the canonical entry point. It lists every sub-artifact as a card with a short description, a preview, and direct links.
- Each card offers both `Open inline` (loads the sub-artifact in an embedded iframe so the reviewer never loses hub context) and `Open standalone` (opens in a new tab for link-sharing or side-by-side review).
- Each sub-page has a `← Back to hub` link in its topbar. Sub-pages detect iframe embedding (`window.top !== window.self`) and hide that link when embedded so the parent UI is not duplicated.
- The hub forwards language changes to embedded sub-artifacts via `postMessage` so the locale stays consistent across frames.
- For docs sites, the hub may be the docs server `index.html`. The back-to-hub link must resolve correctly under every language route, for example `/index.html` and `/en/index.html`.

### Durable docs sites

When HTML artifacts become a multi-page documentation site, serving, translation, and cache hygiene are part of artifact quality:

- Use one server entry point to index all HTML artifacts and keep stable English and Chinese routes.
- Shared UI such as language switches, math support, and translation status bars may be injected into manual or standalone HTML, but must not replace the original body.
- Trust only complete HTML document caches. A valid cache should at least include `html/head/body`; corrupt fragments must never overwrite a complete artifact.
- Request-time translation should be async: return the current static page first, translate in the background, then refresh when ready.
- Historical translation backfill should run through slow polling so language switches do not block page load.
- For remote previews, use a supervisor or hook to keep both the docs server and tunnel (for example ngrok) alive and record the current public URL.

## Cursor Usage

To use this as a project skill, place this repository at:

```text
.cursor/skills/html-artifact/
```

Cursor will discover `SKILL.md` as the skill definition.

## When To Use

Use HTML artifacts when the work involves:

- complex plans or specs
- architecture decisions
- code review or PR explanation
- long research reports
- incident reports
- interactive editors
- task ranking, bucketing, labeling, or prompt tuning
- visual comparisons

Keep Markdown for short notes, CLI output, simple checklists, README drafts, and prompt drafts.

## Standard Artifact Shape

A strong HTML artifact usually contains:

1. Header with title, purpose, context, source, and date.
2. Executive summary with 3-5 takeaways.
3. Navigation through tabs, sidebar, or anchors.
4. Main body with cards, tables, diagrams, snippets, annotations, timelines, and risks.
5. Useful interactions such as filters, search, toggles, sliders, collapsible sections, or drag-and-drop.
6. Export area with copy buttons for HTML, JSON, prompt text, diffs, or selected rows.
7. Appendix with assumptions, raw data, unresolved questions, and next actions.

## Workflow

1. Explore the problem space with an HTML exploration artifact.
2. Let the human compare, adjust, and choose.
3. Turn the chosen direction into an HTML implementation plan.
4. Implement using the artifact as shared context.
5. Verify with an HTML review artifact against the plan and current diff.

## Files

- `SKILL.md`: Cursor skill definition.
- `SKILL.zh-CN.md`: Chinese skill reference.
- `examples.md`: English prompt templates for common HTML artifact tasks.
- `examples.zh-CN.md`: Chinese prompt templates for common HTML artifact tasks.
- `examples/gallery/index.html`: bilingual hub page that previews every demo inline or opens it standalone.
- `examples/gallery/`: self-contained demo HTML files linked from this README. Each one carries a back-to-hub link that auto-hides when embedded in the hub iframe.
- `assets/readme/`: rendered preview assets used by the README gallery.
- `scripts/render-readme-assets.py`: dependency-free generator for the README preview assets.

