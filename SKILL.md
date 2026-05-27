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
- Include CJK-aware fonts in the body font stack of any page that can render Chinese, for example `"PingFang SC", "Microsoft YaHei"` after the Latin stack. Do this in both the Chinese and English HTML so a switched language never loses CJK fallback.
- When two parallel manual pages exist (one per language), write each one as a first-class artifact with the same layout primitives, the same metric cards, the same tables, and the same SVG diagrams. Do not let one language be a thinner summary of the other.

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

### Hub Index And Back Navigation
When an HTML artifact has more than one page (a gallery, a multi-doc report set, a small docs site, a multi-tab editor), give it a hub page and make navigation between hub and sub-pages reversible.

Rules:
- The hub page is the canonical entry point. It must list every sub-artifact with a short description, a preview (image, SVG, or live thumbnail), and a direct link.
- Each sub-artifact card should expose two ways to open it:
  - `Open inline` loads the sub-page in an `<iframe>` embedded in the hub so the reviewer never loses the hub context.
  - `Open standalone` opens the sub-page in a new tab so the reviewer can copy a link or compare two pages side-by-side.
- Every sub-page must include a back-to-hub link in its topbar (for example `← Back to gallery` or `← Back to home`). The link target is the hub page, not the repository README.
- Sub-pages must detect iframe embedding (`window.top !== window.self`) and hide the back-to-hub link when embedded, so the parent hub UI is not duplicated. Other UI such as language switches inside the sub-page can stay; just suppress the navigation row that points back at the hub.
- When the hub embeds a sub-page in an iframe, propagate cross-frame state with `postMessage`. At minimum, the hub should forward the current language so the embedded sub-artifact does not show the wrong locale.
- The hub and every sub-page share the same language switch, fonts, max content width, and export-button style. Treat the hub as the source of truth for shared chrome; sub-pages must not invent their own competing topbar.
- For bilingual artifacts, the hub must localize the card titles, descriptions, and the back-to-hub link text. Both languages must be present in every page, not only on the hub.
- For durable docs sites, the hub may also be the docs server `index.html`. Sub-pages keep a `← Back to home` link in the topbar that resolves correctly under every language route (for example `/index.html` for the default language and `/en/index.html` for English).
- Do not rely on browser history alone for back navigation. A reviewer arriving at a deep-linked sub-page must still see a visible back-to-hub link without pressing the browser back button.

### Manual HTML Ownership Marker
Declare manual ownership with an explicit marker comment near the top of the document, for example `<!-- paperbench-html-source: manual -->`. The build system must:
- Detect the marker by reading the file head, not by filename or directory.
- Skip overwriting marked files when regenerating from Markdown or templates.
- Apply the same protection rule across **all** language routes, not just the default language. A manually maintained English page under `en/` must be preserved with the same logic that protects the default-language manual page.
- Continue to inject shared site furniture (language switch nav, math support, etc.) into manual pages, since that is augmentation, not body replacement.
- Treat the absence of the marker as permission to regenerate; do not silently keep stale auto-generated content alive.

When the source-of-truth document moves (e.g. when a manual HTML supersedes a previously auto-generated page), explicitly migrate the marker and rebuild once to verify both languages remain intact.

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
  - purple for the module or focal stage under review in a module-focused report
  - gray for neutral metadata
- Keep enough whitespace.
- Avoid decorative complexity unless the task is design-focused.
- Make the page readable on mobile.

### Headline Metric Cards
For experiment reports, evaluation summaries, and module status pages, place a small grid of 3-5 "metric cards" near the top so the headline numbers are readable in under 10 seconds. A useful pattern:
- Large number in a strong color (`color: var(--blue)` etc.), font-size around `2rem`, font-weight 800.
- One-line label below in muted color, including the denominator or comparison baseline (`257 / 305`, `vs V7 baseline 25.6%`).
- Use semantic color per card: green for the achieved target, blue for the headline result, orange for the delta vs baseline, purple for volume or population size.
- Place these next to the executive summary so a reviewer can match each takeaway to a number.

### Table Conventions For Numeric Reports
- Right-align numeric columns with `text-align: right` and `font-variant-numeric: tabular-nums` so digits line up across rows.
- Include the denominator inside the cell when the number is a ratio (`52 / 62 = 83.9%`), not in a separate column.
- Bold the headline cell in each row (the metric the table exists to compare) so the eye lands on it.
- For tables that have both per-item rows and an aggregate row, give the aggregate row a distinct background and bold weight (for example `tr.total td { background: #f1f5f9; font-weight: 700; }`).
- Use `rowspan` to group per-item variants under the item label rather than repeating the label.
- Keep at most one totals row per table; do not interleave totals between groups unless the data demands it.

### Callout Boxes
Provide a small set of semantic callout styles (`.callout`, `.callout.green`, `.callout.orange`, `.callout.red`, `.callout.purple`) with a left border in the same hue. Use them to lift one-line conclusions out of the body text:
- green for confirmed positive findings
- blue for neutral observations
- orange for caveats and trade-offs
- red for blockers or invalidating issues
- purple for the focal module or focal change

Callouts must be short. If a callout grows past three lines, demote it into a regular paragraph or split it into a bulleted list.

## Diagram Conversion Guidelines
When source material contains Mermaid, Graphviz, ASCII flows, or diagram-like code blocks:
- Do not leave them as raw code if they are important to understanding.
- Prefer converting them to inline SVG, HTML/CSS flow diagrams, or another browser-native representation.
- Do not rely on Mermaid CDN, external renderers, remote fonts, or network access.
- Preserve the original diagram source in a collapsible appendix or details block.
- If conversion is unsafe or unsupported, show a clear fallback: a readable code block plus a note explaining that the diagram could not be converted.
- For flowcharts, preserve direction, node labels, edges, branching, feedback loops, and semantic grouping.

### Inline SVG Pipeline Diagrams
For pipeline, architecture, or data-flow diagrams that frame a report:
- Use inline `<svg viewBox="...">` with `width: 100%; height: auto` so the diagram scales with the panel.
- Define a single arrow `<marker>` in `<defs>` and reuse it on every edge, so all edges have identical arrowheads.
- Color-code nodes by role and document the roles in a legend below the SVG (input, focal module, planner/orchestrator, downstream stage, final output).
- Highlight the focal module with a thicker stroke and a stronger fill (a light gradient is fine) so the eye lands on the page's subject.
- Label every node with both its name (large, bold) and its identifier or path (small, muted): for example a module name plus its source file, model, or key configuration.
- Place an SVG `<title>` and an outer `role="img" aria-label="..."` so screen readers and search indexes understand the diagram.
- Annotate the dominant output of the focal node next to its outgoing edge (data type, schema, id space), not in a paragraph that the reader has to find later.
- Keep the diagram below ~600 px tall on desktop so it remains readable next to body text, and ensure it remains legible on narrow screens (no horizontal scroll required).
- Repeat the same SVG content in both language versions of a bilingual artifact; translate the in-diagram text but keep the geometry identical so reviewers comparing the two versions can map nodes one-to-one.

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

## Use Case: Module / Pipeline Documentation
When the artifact explains one module inside a larger pipeline (for example an extractor, planner, reviewer, scorer, gate, or orchestrator), structure the page so the reader can answer four questions without scrolling back:

1. Where does this module sit in the pipeline? Show a pipeline SVG that highlights the focal module and dims the rest. Place this near the top of the page.
2. What does it consume and emit? Add an inputs / outputs / model card with a `<dl class="kv">` block that lists each input field (name, type, source, size or cap), each output field (name, type, structure), and the model or external service the module calls (model name, version, concurrency parameters, timeout). Name the source file and key constants verbatim, for example `paperbench/rubric/v8_modules.py · MAX_CHUNK_CHARS = 18000`.
3. How does it work internally? If the module has multiple recall layers, retry stages, sub-prompts, or fallbacks, give each one its own labelled card with a one-line description and the constants or prompt names that govern it.
4. Does it actually work? Place per-item validation tables (one row per paper, document, ticket, or sample) above the aggregate row, and include both extractor-level and end-to-end measurements when both exist. Add a callout that states the headline conclusion in one sentence.

Additional rules:
- Distinguish "what this module can reach" from "what survives downstream" with separate tables and clearly different metric labels. Do not conflate planner-only or smoke-only numbers with final pipeline numbers.
- For every measured number, link or cite the run artifact path (`tmp/...` or similar) in a muted footer so a reader can audit.
- For every cited code path, prefer a code-style inline reference rather than a free-form sentence: `paperbench/rubric/v8_modules.py · EvidenceExtractor.extract` is more useful than "the extract function in v8_modules".
- When comparing variants of the same module (with vs without a layer, monolithic vs parallel, etc.), present them as adjacent rows in one table so the delta is obvious, then summarize the delta in a callout below the table.

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

## Anti-Patterns
Avoid these failure modes; each one has shown up in real reports and degrades trust.

- **Boilerplate hero from a category template.** Do not inherit a generic category description (for example "explains repository structure, doc strategy, and review records") into the hero of a topic-specific artifact. The hero must describe *this* artifact's content, scope, and measurement target. Replace any inherited "purpose" string from an auto-generated category before publishing.
- **Stale category metadata after rewrites.** When an artifact is rewritten with new scope (single paper → core3, smoke → planner-only), update the badges, tags, related-docs list, and JSON export at the same time. A mismatch between the body and the metadata is treated as evidence the page is out of date.
- **Auto-generated and manual fighting over the same file.** Never let a Markdown-driven build overwrite a manually maintained HTML page. Use the ownership marker, apply it to all language routes, and verify by rebuilding twice in a row that the manual page is byte-stable between rebuilds.
- **Mixing planner-only, smoke, and end-to-end numbers in one row.** Each metric must declare its scope (extractor-level, planner-only, full-pipeline, smoke vs full). Putting a planner-only `84.3%` and a final-rubric percent in the same column without labels misleads reviewers.
- **Decorative source-code dumps.** Do not embed long raw Markdown or unprocessed source as the main reading surface. Render the useful parts as cards, tables, callouts, and diagrams; keep the raw source as an optional appendix only if audit is required.
- **One-language improvements.** If a structural fix or new diagram is added to one language route, port it to the other route in the same change. A bilingual artifact where the languages have diverged in layout silently signals the project is unmaintained.
- **Aggregate-only conclusions.** Do not present aggregate metrics without per-item rows when the aggregate could be dominated by one item. For three-paper benchmarks, always show the three per-paper rows above the total.
- **Forgotten artifact paths.** When a number comes from a run, link or list the artifact path inline. Numbers without an artifact path are unauditable.
- **Diagram drift.** When the pipeline changes (a module is added, renamed, or repositioned), update every diagram in the artifact tree, not just the one in the most recently edited page. A bilingual artifact must have identical diagram geometry across languages.
- **Sticky-nav fight with the build system.** If the build system injects a sticky language switch at the top of `<body>`, do not also inject a competing fixed-position nav in the page body; let the build-system nav own that slot and provide an inline language switch in the topbar at most.

## Prompt Pattern
When invoking this skill, follow this pattern:

> Create a single-file bilingual HTML artifact for [task]. It should help me [decision/review/understand/edit/share]. Include [visualizations/interactions]. Render any source material as browser-native HTML, not as a raw Markdown appendix. Add export buttons for [HTML/JSON/Prompt/Diff]. Make it self-contained, readable in a browser, and available in both Chinese and English.

## Quality Checklist
Before finishing, verify:
- Is this more useful than Markdown?
- Can the user understand the main point in 30 seconds (hero + metric cards + executive summary)?
- Can the user inspect details if needed (per-item tables, code paths, artifact paths)?
- Does the hero describe *this* artifact, not a generic category boilerplate?
- Are source diagrams rendered as browser-native visuals rather than raw Mermaid when possible?
- For module/pipeline pages, is there a labelled pipeline SVG with the focal module highlighted and a legend?
- For module/pipeline pages, are inputs, outputs, and the model/service named with their source file and key constants?
- Are per-item rows shown above any aggregate row, and is the aggregate visually distinct?
- Are numeric columns right-aligned with tabular figures, and do ratios include their denominator inline?
- Is every measurement number traceable to an artifact path or run id in the page itself?
- Are risks and assumptions visible?
- Are comparisons easy to scan?
- Are interactions useful rather than decorative?
- Is there a way to export the result back to the agent workflow (JSON, Prompt, Markdown summary)?
- Is the file self-contained, working without internet, and openable directly in a browser?
- Is there both a Chinese and English reading path for durable artifacts, with the same layout, the same metric cards, the same tables, and the same SVG geometry?
- Is the body font stack CJK-safe in both language pages?
- Is source material rendered as useful HTML rather than left as raw Markdown?
- Are formulas rendered as math and still readable on narrow screens?
- If this is a docs site, are complete HTML documents protected from malformed translation caches or partial injection?
- If the artifact has more than one page, is there a hub index that previews every sub-page, and does every sub-page expose a back-to-hub link that hides itself when embedded?
- If the page is manually owned, does it carry the manual ownership marker in **every** language route it claims to own, and does a fresh rebuild leave both files byte-stable?
- If remote preview was requested, is the server/tunnel supervised rather than manually started once?

