# HTML Artifact Skill

HTML Artifact 工作流让 agent 输出从“文本计划”升级为“可读、可交互、可审阅的工作界面”。

核心思想不是用 HTML 替代 Markdown，而是：

> 当输出的目的不只是记录，而是帮助人理解、比较、决策、审阅、调整时，优先让 agent 生成 HTML Artifact。

Markdown 适合短文本、轻量笔记、README、简单说明。HTML 适合复杂信息、可视化、交互、评审、分享和决策。

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
6. Export area with copy buttons for Markdown, JSON, prompt text, diffs, or selected rows.
7. Appendix with assumptions, raw data, unresolved questions, and next actions.

## Workflow

1. Explore the problem space with an HTML exploration artifact.
2. Let the human compare, adjust, and choose.
3. Turn the chosen direction into an HTML implementation plan.
4. Implement using the artifact as shared context.
5. Verify with an HTML review artifact against the plan and current diff.

## Files

- `SKILL.md`: Cursor skill definition.
- `examples.md`: Prompt templates for common HTML artifact tasks.

