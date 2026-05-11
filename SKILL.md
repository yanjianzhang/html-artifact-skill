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
   - Copy as Markdown
   - Copy as JSON
   - Copy as Prompt
   - Copy diff
   - Export selected items
7. Appendix
   - assumptions
   - raw data
   - unresolved questions
   - next actions

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

When creating an editor, always include an export button. The export should be directly usable by the user, usually as JSON, Markdown, prompt text, patch instructions, or a config diff.

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

> Create a single-file HTML artifact for [task]. It should help me [decision/review/understand/edit/share]. Include [visualizations/interactions]. Add export buttons for [JSON/Markdown/Prompt/Diff]. Make it self-contained and readable in a browser.

## Quality Checklist
Before finishing, verify:
- Is this more useful than Markdown?
- Can the user understand the main point in 30 seconds?
- Can the user inspect details if needed?
- Are risks and assumptions visible?
- Are comparisons easy to scan?
- Are interactions useful rather than decorative?
- Is there a way to export the result back to the agent workflow?
- Is the file self-contained?
- Does it work without internet?

