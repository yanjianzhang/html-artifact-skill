# HTML Artifact Prompt Examples

[中文示例](examples.zh-CN.md)

## General

```text
Do not write Markdown. Create a single-file HTML artifact that helps me understand, compare, and decide on this problem:
{problem}
Requirements:
- Include an Executive Summary.
- Include visual structure.
- Include a comparison table.
- Include risks and recommendations.
- Include next actions.
- Render all source material as HTML body content; do not keep a raw Markdown appendix.
- Provide English and Chinese reading paths.
- Keep it as a single HTML file that opens directly in a browser.
```

## Exploration

```text
Create an HTML exploration artifact.
Topic: {topic}
Give me 6 clearly different options and show them side by side in a card grid.
For each option include:
- Core idea
- Best-fit user
- Pros
- Cons
- Implementation cost
- Risks
- Recommendation score
End with your recommended option or combination.
```

## Implementation Plan

```text
Create an HTML implementation plan.
Goal: {goal}
Include:
- Overall architecture
- Data-flow diagram
- File change list
- API/schema design
- Key code snippets
- Risks
- Test plan
- Phased task breakdown
Make it visually clear enough that I can hand it to another agent session for implementation.
Maintain English and Chinese versions; for site-style output, provide `html_en` / `html_zh` paths or manifest fields.
```

## PR Review

```text
Generate an HTML code review artifact from the current git diff.
Focus on:
- Explaining what this PR changes
- Rendering the key diffs
- Adding side notes to important code
- Labeling findings as Blocker / Major / Minor / Nit
- Drawing the relevant data flow or call chain
- Listing required fixes and suggested improvements
Do not only write prose; make it an HTML page that is easy to review.
```

## Temporary Editor

```text
Create a single-file temporary HTML editor for this data:
{data}
The operation I need is: {sort / bucket / label / edit config / tune prompt}
Requirements:
- Provide an initial recommendation.
- Support manual editing.
- Support search or filtering.
- Warn about conflicts or anomalies.
- Provide Copy as HTML / JSON / Prompt buttons.
- Exported content should be directly usable when pasted back into an agent.
- If this is a durable tool, provide English / Chinese interface entries.
```

## Documentation Site

```text
Organize this set of Markdown / HTML / JSON materials into an HTML artifact documentation site.
Requirements:
- Convert all Markdown content into browser-native HTML body content; do not keep an Original Markdown Source Appendix.
- Maintain English and Chinese versions of every page.
- Use English as the public README / external entry, with a clear link to the Chinese version.
- Add an English / Chinese switch at the top of every page.
- Indexes and manifests must record bilingual entries, for example `html_en` / `html_zh`.
- If a same-named HTML artifact corresponds to a Markdown source, inherit the source creation history; standalone HTML artifacts can use file time.
- If a page includes formulas or metric definitions, render them with MathJax / LaTeX display math rather than plain code blocks.
- When injecting language switches, math support, or translation controls, preserve the complete HTML body; corrupt caches or HTML fragments must not overwrite a full page.
- Translation should be async: show the current static page first, backfill translation in the background, then refresh dynamically.
- Export buttons should prefer HTML / JSON / Prompt.
```

## Durable HTML Docs Server

```text
Maintain the current HTML artifact documentation site as a durable remotely previewable docs site.
Requirements:
- Use a unified server entry point to index all HTML pages.
- Keep English and Chinese routes, with an English public README and a clear link to Chinese docs.
- Inject language switching and formula support into manual / standalone HTML without replacing the original body.
- Validate translation caches and accept only complete HTML with html/head/body.
- Do not block page load when the user switches language: return the current static page first, translate in the background, then refresh.
- Configure a watchdog / supervisor so the docs server and ngrok tunnel restart automatically if they stop, and write the public URL to a log.
```

## Hub Page With Sub-Artifacts

```text
Create a bilingual HTML hub page that indexes the following sub-artifacts:
- {sub-artifact 1 (path or title)}
- {sub-artifact 2 (path or title)}
- {sub-artifact 3 (path or title)}
Requirements:
- The hub lists every sub-artifact as a card with a short description and a preview (image or inline SVG).
- Each card exposes two actions: "Open inline" (loads the sub-artifact in an iframe panel embedded in the hub) and "Open standalone" (opens in a new tab).
- Every sub-artifact must have a "Back to hub" link in its topbar, with text that matches the active language.
- Each sub-artifact must detect iframe embedding (`window.top !== window.self`) and hide its back-to-hub link when embedded, so the parent UI is not duplicated.
- The hub forwards language changes to embedded sub-artifacts via `postMessage` so the locale stays consistent.
- Hub and sub-artifacts share the same language switch, fonts, and export styles; do not invent a competing topbar in any sub-page.
- Provide English and Chinese reading paths on the hub and every sub-artifact.
- A deep-linked sub-artifact must still show the back-to-hub link without depending on the browser back button.
```

## Formula-Heavy Report

```text
Create a bilingual HTML artifact that includes metric formulas.
Requirements:
- Use cards to explain the purpose, inputs, outputs, and optimization direction for each metric.
- Render formulas with LaTeX display math or aligned blocks; do not leave them only in pre/code.
- Long formulas must be horizontally scrollable on narrow screens.
- If original formula text is preserved, also provide browser-readable math rendering.
- Provide English / Chinese reading paths.
```

