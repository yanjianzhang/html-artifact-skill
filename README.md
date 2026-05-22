# HTML Artifact Skill

HTML Artifact 工作流让 agent 输出从“文本计划”升级为“可读、可交互、可审阅的工作界面”。

核心思想不是用 HTML 替代 Markdown，而是：

> 当输出的目的不只是记录，而是帮助人理解、比较、决策、审阅、调整时，优先让 agent 生成 HTML Artifact。

Markdown 适合短文本、轻量笔记、README、简单说明。HTML 适合复杂信息、可视化、交互、评审、分享和决策。

HTML artifact 可以直接作为一等源文件维护。不要默认要求每个 HTML 都由 Markdown 生成；当用户编辑、发布或审阅已有 HTML artifact 时，应优先保留 HTML 本身，只把 Markdown 当作可选历史、附录或导出格式。

## Methodology

### HTML-first content

当输入来自 Markdown、日志、JSON、表格或混合笔记时，默认把有用内容转换成浏览器原生 HTML 正文：

- 标题、列表、表格、引用、代码块、图和链接都应渲染为 HTML。
- 不要把完整内容藏在 `Original Markdown Source Appendix` 一类的 raw Markdown 附录里。
- 如果需要审计原始材料，可以加入 evidence/raw-data 区块，但它不应成为主要阅读路径。
- 导出优先提供 HTML、JSON、Prompt、Diff 或结构化数据；Markdown 导出只作为兼容选项。

### Bilingual output

持久化 artifact 和文档站点默认维护中英文两个阅读路径：

- 单文件 artifact：在同一个 HTML 中提供 `中文` / `English` 切换或双语视图。
- 多页面站点：维护平行路由，例如中文在 canonical path，英文在 `en/` 下。
- 页面应设置正确语言属性：`<html lang="zh-CN">` 和 `<html lang="en">`。
- 索引或 manifest 应显式记录双语路径，例如 `html_zh` 与 `html_en`。
- 如果英文正文尚未完成，也要创建英文入口并明确标注未翻译部分，不能假装已经完整本地化。

### Math and formulas

涉及指标、评分规则、概率、集合或算法定义时，公式应该作为数学内容呈现，而不是普通代码块：

- 优先使用 LaTeX delimiter：inline `\(...\)`，display `\[...\]` 或 `$$...$$`。
- 多行指标定义使用 aligned display，便于对齐等号和逐行阅读。
- 已存在的 `<div class="formula">...</div>` 纯文本公式块可以保留 source text，同时在浏览器中升级为 MathJax 或等价渲染。
- 公式区域需要横向滚动 fallback，避免移动端或窄屏把页面撑坏。

### Durable docs sites

当 HTML artifact 发展成多页面文档站时，服务、翻译和缓存也属于 artifact 质量的一部分：

- 用统一入口索引所有 HTML artifact，并维护 `zh` / `en` 平行路由。
- 语言切换、公式支持、翻译状态条等共享 UI 可以注入 manual/standalone HTML，但不能替换原始正文。
- 只信任完整 HTML 文档缓存：至少应包含 `html/head/body`。坏缓存或片段不能覆盖完整 artifact。
- 请求时翻译应异步：先返回已有静态页面，再后台翻译并在完成后刷新。
- 历史翻译 backfill 应由慢轮询处理，不阻塞用户点击语言切换。
- 需要远程预览时，用 supervisor/hook 同时守护 docs server 和 tunnel（例如 ngrok），并记录当前 public URL。

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
- `examples.md`: Prompt templates for common HTML artifact tasks.

