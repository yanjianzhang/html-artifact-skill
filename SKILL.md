---
name: html-artifact
description: Generate self-contained HTML artifacts for complex plans, specs, code reviews, architecture explanations, research reports, design prototypes, interactive editors, visual comparisons, and decision support. Use when Markdown would be too long, hard to review, or insufficiently interactive.
---

# HTML Artifact Skill

## Purpose
Use this skill when the user needs an output that is easier to read, compare, review, share, or interact with than Markdown.

Prefer HTML artifacts for:
- complex plans
- specs
- code reviews
- architecture explanations
- PR explanations
- design prototypes
- research reports
- incident reports
- interactive editors
- task prioritization
- configuration editing
- prompt tuning
- dataset review
- visual comparisons

Do not use HTML when a short Markdown answer is enough.

## Core Principle
The artifact should help the human stay in the loop.

It should not merely be a prettier document. It should make the underlying decision, system, code, plan, or data easier to inspect and act on.

Markdown is for lightweight records. HTML artifacts are for human decisions, reviews, comparisons, and collaboration interfaces.

## Source Independence
Do not require Markdown as the canonical source for an HTML artifact.

HTML may be the primary artifact and the source of truth. When an existing `.html` artifact is being edited, reviewed, enriched, served, or published:
- Read and preserve the HTML directly.
- Do not regenerate it from a same-named `.md` file unless the user explicitly asks for Markdown-driven generation.
- Treat Markdown as optional source material, history, appendix content, or export format.
- If a build system supports both Markdown and HTML, prefer an explicit marker or metadata field that declares manual HTML ownership rather than relying on filename conventions.
- Do not overwrite a user-maintained HTML artifact with Markdown-derived output.
- Keep export-to-Markdown useful, but do not make Markdown a dependency for editing or serving the artifact.

## HTML-First Source Conversion
When source material is Markdown, plain text, Mermaid, Graphviz, logs, JSON, or mixed notes, convert the useful content into browser-native HTML as the main reading surface.

Rules:
- Do not leave the source as a raw Markdown appendix unless the user explicitly asks for raw source preservation.
- Render headings, lists, tables, quotes, code blocks, diagrams, metadata, and links as HTML sections that are readable directly in the browser.
- If source text matters for auditability, place it in a clearly labeled evidence or raw-data section only when that helps review; do not make it the primary reading path.
- For Markdown-derived pages, use language such as "Full Document Content" or "Rendered Content" rather than "Original Markdown Source Appendix".
- Export controls should prefer HTML, JSON, Prompt, Diff, or selected structured data. Offer Markdown export only when the user asks for Markdown compatibility.

## Bilingual Artifacts
Maintain both Chinese and English versions when creating or maintaining a durable HTML artifact or documentation site.

Rules:
- For a standalone artifact, include a clear language switch or two top-level language views (`中文` and `English`) in the same self-contained file unless separate files are requested.
- For a multi-page site, maintain parallel `zh` and `en` routes. A common pattern is Chinese at the canonical path and English under `en/`, with every page linking to its counterpart.
- Keep language metadata explicit: set `<html lang="zh-CN">` for Chinese pages and `<html lang="en">` for English pages.
- Keep the same information architecture, headings, anchors, export controls, and navigation in both languages.
- If full human-quality translation is not yet available, still create the English page and mark untranslated body sections clearly; do not silently pretend mixed-language content is fully localized.
- For generated indexes or manifests, include both language paths, for example `html_zh` and `html_en`.
- Preserve historical ordering across languages. If an HTML artifact corresponds to a Markdown/source document, inherit that source's creation history; standalone HTML artifacts can use artifact file time.

## When To Choose HTML
Use HTML when any of these are true:
- The content is longer than about 100 lines.
- Multiple options or approaches must be compared.
- A diagram, flow, timeline, matrix, chart, or visual hierarchy would help.
- Code diffs, review annotations, severity levels, or risks must be inspected.
- The result should be shared with a teammate, reviewer, manager, investor, or customer.
- The work synthesizes several context sources.
- The user needs controls such as filtering, search, toggles, sliders, drag-and-drop, or export.
- The user is unlikely to carefully read a long Markdown response.

Keep Markdown for short explanations, README drafts, CLI output, simple checklists, quick notes, and prompt drafts.

## Default Output Format
Generate a single self-contained HTML file.

Requirements:
- Inline CSS
- Inline JavaScript if needed
- No external CDN
- No external fonts
- No external images unless explicitly provided
- Convert Mermaid, Graphviz, or other diagram source blocks into browser-native inline SVG or equivalent HTML/CSS diagrams when possible
- Openable directly in a browser
- Responsive layout
- Clear visual hierarchy
- Export / copy buttons when the user needs to bring results back into the agent workflow

## Standard Structure
Every HTML artifact should generally include:
1. Header
   - title
   - purpose
   - context
   - date or version if relevant
2. Executive Summary
   - 3-5 most important takeaways
3. Navigation
   - tabs, sidebar, or anchor links for long documents
4. Main Body
   - cards
   - tables
   - diagrams
   - code snippets
   - annotations
   - comparisons
   - timelines
   - risk blocks
5. Interactions
   - search
   - filters
   - toggles
   - sliders
   - drag and drop
   - collapsible sections
   - comparison controls
6. Export Section
   - Copy as HTML
   - Copy as JSON
   - Copy as Prompt
   - Copy diff
   - Export selected items
7. Appendix
   - assumptions
   - raw data
   - unresolved questions
   - next actions

## Report Layout Rules
When generating analytical reports, experiment reports, evaluation summaries, benchmark comparisons, or documentation index cards:

- State the exact evidence scope used for every aggregate conclusion. For experiment reports, list the paper IDs, titles, sample counts, valid/invalid rows, and any checkpointed or excluded runs before presenting rankings.
- Include a per-item comparison view whenever aggregates are shown. For PaperBench-style reports, this means per-paper rows with the compared variants or versions, P/R/F1 or equivalent metrics, and a short interpretation for each paper.
- Use interactive filters for comparison tables that are longer than a few rows or likely to be inspected by paper, variant, module, model, run, severity, or tag.
- Keep aggregate and per-item conclusions separate. Do not mix partial, checkpointed, smoke, or failed runs into headline rankings unless the report clearly labels the scope and risk.
- Write summary cards as decision-oriented abstracts, not generic artifact descriptions. A card should say what was measured, which data it used, the main result, and the recommended interpretation.
- Do not display tags that apply to every page in the same collection. Hide generic tags such as `Standalone HTML`, `artifact`, or broad category labels when they add no filtering value; show only differentiating tags such as version, protocol, model, benchmark, status, or risk.
- For bilingual documentation sites, keep the same layout, evidence scope, tables, filters, and card summaries across languages. Do not add a structural improvement to only one language route.

## Math And Formula Rendering
When an artifact includes equations, metrics, scoring rules, or symbolic definitions, render them as math, not as plain code-like text.

Rules:
- Prefer LaTeX delimiters for author-written formulas: inline `\(...\)` and display `\[...\]` or `$$...$$`.
- For multi-line metric definitions, use an aligned display block so equal signs and terms scan vertically.
- If a source artifact already has plain formula blocks such as `<div class="formula">A = ...</div>`, preserve the source text but upgrade the browser view with MathJax or an equivalent local renderer.
- Keep formula blocks horizontally scrollable on small screens; do not let long equations break the page layout.
- Do not rely on external CDNs for required offline artifacts. If CDN MathJax is acceptable for a served documentation site, make that dependency explicit and keep a readable fallback.
- Avoid wrapping formulas in `<code>` or `<pre>` unless the user is reviewing source syntax rather than reading the math.

## Durable Documentation Sites
When maintaining a multi-page HTML documentation site, treat serving, translation, and generated caches as part of the artifact system.

Rules:
- Use a single docs server entry point that indexes all HTML artifacts and keeps stable `zh` and `en` routes.
- Add a language switch to manual and standalone HTML artifacts without replacing their original body.
- When injecting shared UI, math support, or translation controls into existing HTML, only mutate complete HTML documents with `html/head/body`; never let a fragment or corrupt cache overwrite a full artifact.
- Validate translation caches before using them. If a cached HTML translation is malformed, fall back to the complete source page and regenerate the cache later.
- For on-demand translation, return the existing static page immediately and do translation in the background. Show a status banner and refresh only after the updated page is available.
- For backfill translation, run slow polling separately from request-time behavior so language-switch clicks do not block page load.
- For public preview tunnels such as ngrok, use a supervisor or hook that keeps both the docs server and tunnel process alive and records the current public URL.

## Visual Design Guidelines
Use a clean, information-dense but readable style.

Rules:
- Max content width around 1100-1280px.
- Use cards for major concepts.
- Use tables for structured comparisons.
- Use badges for status, priority, severity, and confidence.
- Use semantic colors:
  - red for blocker or high risk
  - orange for warnings
  - blue for informational notes
  - green for success or recommendation
  - gray for neutral metadata
- Keep enough whitespace.
- Avoid decorative complexity unless the task is design-focused.
- Make the page readable on mobile.

## Diagram Conversion Guidelines
When source material contains Mermaid, Graphviz, ASCII flows, or diagram-like code blocks:
- Do not leave them as raw code if they are important to understanding.
- Prefer converting them to inline SVG, HTML/CSS flow diagrams, or another browser-native representation.
- Do not rely on Mermaid CDN, external renderers, remote fonts, or network access.
- Preserve the original diagram source in a collapsible appendix or details block.
- If conversion is unsafe or unsupported, show a clear fallback: a readable code block plus a note explaining that the diagram could not be converted.
- For flowcharts, preserve direction, node labels, edges, branching, feedback loops, and semantic grouping.

## Interaction Guidelines
Only add interaction when it helps the task.

Useful interactions:
- filters for large tables
- tabs for multiple views
- toggles for before/after
- sliders for tuning visual parameters
- drag-and-drop for ranking or bucketing
- copy buttons for exporting results
- collapsible sections for long explanations
- live preview for prompt, template, or config editing

When creating an editor, always include an export button. The export should be directly usable by the user, usually as HTML, JSON, prompt text, patch instructions, or a config diff. Add Markdown export only when the user needs Markdown compatibility.

## Workflow
Use this five-step loop for complex work:

1. Explore: create an HTML exploration artifact that opens the problem space and compares 4-6 routes.
2. Select: let the user read, compare, adjust, and choose.
3. Plan: convert the chosen route into an implementation plan artifact with modules, files, data flow, risks, and tests.
4. Implement: use the artifact as the shared contract while making changes.
5. Verify: review the plan and diff with an HTML review artifact showing implemented, missing, diverged, risky, and untested parts.

## Use Case: Planning and Exploration
When the user asks for planning, brainstorming, architecture, or product exploration, create an HTML artifact that includes:
- multiple options
- side-by-side comparison
- trade-offs
- risks
- cost estimate
- recommended path
- visual diagrams if helpful
- next-step implementation plan

Avoid giving only one plan too early unless the user explicitly asks.

## Use Case: Code Review
When reviewing code or a PR, create an HTML artifact that includes:
- summary of what changed
- key files
- rendered diff snippets
- inline annotations
- severity labels
- architecture or data-flow diagram
- correctness risks
- performance risks
- security risks
- missing tests
- required fixes
- optional improvements

Severity levels:
- Blocker
- Major
- Minor
- Nit

## Use Case: Code Understanding
When explaining a codebase or subsystem, create an HTML artifact that includes:
- mental model
- key modules
- file map
- call graph
- data flow
- important code snippets
- common pitfalls
- glossary
- recommended reading order

Optimize for "understand in one reading".

## Use Case: Design Prototype
When prototyping UI, interaction, animation, or visual style, create an HTML artifact that includes:
- realistic UI mockup
- multiple states
- controls for key parameters
- live preview
- copy/export button for chosen parameters
- explanation of design trade-offs

If the final implementation target is React, Flutter, Swift, or another stack, still use HTML for exploration unless the user asks otherwise.

## Use Case: Research Report
When creating a report, create an HTML artifact that includes:
- executive summary
- main findings
- evidence
- charts or tables
- diagrams
- risks and uncertainties
- recommendations
- action list
- appendix with sources or assumptions

Optimize for the target reader: self, engineer, manager, executive, investor, or customer.

## Use Case: Custom Editor
When the user needs to rank, bucket, label, edit, review, or tune something, create an HTML tool, not a static document.

Examples:
- ticket prioritizer
- feature flag editor
- prompt editor
- dataset labeling interface
- config diff editor
- design parameter tuner
- copy review interface

Always:
- preload a reasonable initial state
- show warnings for conflicts
- allow editing
- provide export / copy functionality

## Prompt Pattern
When invoking this skill, follow this pattern:

> Create a single-file bilingual HTML artifact for [task]. It should help me [decision/review/understand/edit/share]. Include [visualizations/interactions]. Render any source material as browser-native HTML, not as a raw Markdown appendix. Add export buttons for [HTML/JSON/Prompt/Diff]. Make it self-contained, readable in a browser, and available in both Chinese and English.

## Quality Checklist
Before finishing, verify:
- Is this more useful than Markdown?
- Can the user understand the main point in 30 seconds?
- Can the user inspect details if needed?
- Are source diagrams rendered as browser-native visuals rather than raw Mermaid when possible?
- Are risks and assumptions visible?
- Are comparisons easy to scan?
- Are interactions useful rather than decorative?
- Is there a way to export the result back to the agent workflow?
- Is the file self-contained?
- Does it work without internet?
- Is there both a Chinese and English reading path for durable artifacts?
- Is source material rendered as useful HTML rather than left as raw Markdown?
- Are formulas rendered as math and still readable on narrow screens?
- If this is a docs site, are complete HTML documents protected from malformed translation caches or partial injection?
- If remote preview was requested, is the server/tunnel supervised rather than manually started once?

