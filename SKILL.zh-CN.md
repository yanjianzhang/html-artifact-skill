# HTML Artifact Skill 中文参考

> Cursor 实际加载的 skill 定义是英文 [`SKILL.md`](SKILL.md)。本文件是中文参考，用于维护双语说明和人工阅读。

## 目的

当用户需要比 Markdown 更容易阅读、比较、审阅、分享或交互的输出时，使用 HTML Artifact。

适合场景：

- 复杂计划和规格说明
- 代码审阅和 PR 解释
- 架构说明
- 研究报告和事故报告
- 交互式编辑器
- 任务排序、分桶、打标、prompt tuning
- 数据集审阅和可视化比较

如果短 Markdown 回答已经足够，不要强行使用 HTML。

## 核心原则

Artifact 应帮助人类保持在 loop 中。它不只是“更好看的文档”，而是让底层决策、系统、代码、计划或数据更容易被检查和行动。

Markdown 适合轻量记录；HTML artifact 适合决策、审阅、比较和协作界面。

## Source Independence

不要要求 Markdown 一定是 HTML artifact 的 canonical source。

当已有 `.html` artifact 被编辑、审阅、增强、服务或发布时：

- 直接读取和保留 HTML。
- 除非用户明确要求 Markdown-driven generation，否则不要从同名 `.md` 重新生成。
- 把 Markdown 当作可选来源、历史、附录或导出格式。
- 如果构建系统同时支持 Markdown 和 HTML，应使用明确 marker 或 metadata 声明 manual HTML ownership。
- 不要用 Markdown-derived output 覆盖用户维护的 HTML artifact。

## HTML-First Source Conversion

当源材料来自 Markdown、文本、Mermaid、Graphviz、日志、JSON 或混合笔记时，把有用内容转换成浏览器原生 HTML 正文。

规则：

- 不要留下 raw Markdown appendix，除非用户明确要求保留 raw source。
- 标题、列表、表格、引用、代码块、图、metadata 和链接都应渲染为 HTML。
- 如果源文本对审计有价值，可以放入 evidence 或 raw-data section，但不要让它成为主要阅读路径。
- Markdown-derived 页面应使用 “Full Document Content” 或 “Rendered Content” 这类语言，而不是 “Original Markdown Source Appendix”。
- 导出控件优先提供 HTML、JSON、Prompt、Diff 或结构化数据；只有用户需要兼容时才提供 Markdown export。

## 双语 Artifacts

创建或维护 durable HTML artifact / docs site 时，应维护中英文版本。

规则：

- 单文件 artifact：在同一个 HTML 中提供 `中文` / `English` 切换或双语视图。
- 多页面站点：维护平行路由。公开 README / 外部入口默认英文，并提供清晰中文跳转。
- 设置语言 metadata：中文 `<html lang="zh-CN">`，英文 `<html lang="en">`。
- 两种语言保持相同的信息架构、标题、锚点、导出控件和导航。
- 如果翻译尚未完成，也要创建对应语言入口并明确标注未完成部分，不要假装已经完整本地化。
- 索引或 manifest 应包含双语路径，例如 `html_en` 和 `html_zh`。
- 如果 HTML artifact 对应 Markdown/source document，应继承 source 的创建历史；standalone HTML artifact 可使用文件时间。
- 支持中文的页面应在 font stack 中包含 CJK fallback，例如 `"PingFang SC", "Microsoft YaHei"`。

## 数学公式渲染

包含方程、指标、评分规则或符号定义时，把它们渲染成数学内容，而不是普通代码文本。

规则：

- 作者手写公式优先使用 LaTeX delimiter：inline `\(...\)`，display `\[...\]` 或 `$$...$$`。
- 多行指标定义使用 aligned display，让等号和条目纵向对齐。
- 如果源 artifact 已有 `<div class="formula">A = ...</div>` 这类纯文本公式块，保留 source text，同时用 MathJax 或等价方式升级浏览器视图。
- 窄屏下公式块应可横向滚动，不要撑坏布局。
- 离线 artifact 不应依赖外部 CDN；如果 served docs site 可以接受 CDN MathJax，应显式说明并保留可读 fallback。

## Durable Documentation Sites

多页面 HTML 文档站的服务、翻译和缓存也属于 artifact 系统。

规则：

- 使用单一 docs server 入口索引所有 HTML artifact，并维护稳定中英文路由。
- 为 manual / standalone HTML 注入语言切换，但不能替换原始 body。
- 注入共享 UI、数学支持或翻译控件时，只修改完整 HTML 文档；完整文档至少应包含 `html/head/body`。
- 使用 translation cache 前要验证完整性。坏缓存应回退到完整源页面，并稍后重新生成。
- 请求时翻译应异步：先返回已有静态页面，后台翻译，完成后显示状态并刷新。
- 历史 backfill 翻译用慢轮询，不阻塞用户点击语言切换。
- 如果需要 ngrok 等公网预览，用 supervisor 或 hook 同时守护 docs server 和 tunnel，并记录当前 public URL。

## 首页 + 子页面 导航

当一个 HTML artifact 超过单页（gallery、多文档报告集合、小型 docs site、多 tab 编辑器）时，必须配套提供一个首页（hub），并保证首页 ↔ 子页面之间的双向导航。

规则：

- 首页是 canonical 入口。它应该列出所有子 artifact，并提供简短说明、预览图（图片、SVG 或实时缩略图）和直达链接。
- 每张子 artifact 卡片至少提供两种打开方式：
  - `嵌入预览`（Open inline）通过 `<iframe>` 把子页面嵌入到首页里，保留首页上下文。
  - `独立打开`（Open standalone）在新标签页打开子页面，便于复制链接或同时对比两个页面。
- 每个子页面顶部必须有 `← 返回 gallery` 或 `← 返回首页` 链接，跳回首页本身，而不是仓库 README。
- 子页面应检测自己是否被 iframe 嵌入（`window.top !== window.self`）。被嵌入时隐藏 back-to-hub 链接，避免与父页 UI 重复。语言切换等子页面自有 UI 可以保留，只屏蔽指向首页的导航行。
- 首页 iframe 嵌入子页面时，使用 `postMessage` 同步跨 frame 状态。至少要把当前语言从首页广播到子页面，避免被嵌入的子 artifact 显示错误的 locale。
- 首页和子页面共用相同的语言切换、字体、最大内容宽度和导出按钮样式。首页是共享 chrome 的事实源，子页面不能再写一套竞争的 topbar。
- 双语 artifact 中，首页必须本地化卡片标题、描述和 back-to-hub 链接文案。两种语言要在每个页面中都出现，而不是只在首页。
- 对于 durable docs site，首页可以等同于 docs server 的 `index.html`。子页面顶部 `← 返回首页` 链接在每个语言路由（例如默认语言的 `/index.html` 和英文的 `/en/index.html`）下都要解析正确。
- 不要只依赖浏览器历史完成返回操作。深链接进入子页面的用户也必须能在页面里直接看到 back-to-hub 链接，而不需要按浏览器后退键。

## 常见结构

每个 HTML artifact 通常应包含：

1. Header：标题、目的、上下文、日期或版本。
2. Executive Summary：3-5 条最重要结论。
3. Navigation：tabs、sidebar 或 anchor links。
4. Main Body：卡片、表格、图、代码片段、注释、对比、时间线、风险块。
5. Interactions：搜索、筛选、切换、滑块、拖拽、折叠、比较控件。
6. Export Section：Copy as HTML / JSON / Prompt / Diff / selected rows。
7. Appendix：假设、raw data、未解决问题、next actions。

## 质量检查

完成前检查：

- 这是否比 Markdown 更有用？
- 用户能否在 30 秒内理解主结论？
- 是否能继续检查细节？
- 源图是否尽量渲染为浏览器原生视觉，而不是 raw Mermaid？
- 风险和假设是否可见？
- 对比是否容易扫描？
- 交互是否真的有用，而不是装饰？
- 是否能导出回 agent 工作流？
- 是否自包含？
- durable artifact 是否有中英文阅读路径？
- 源材料是否渲染为有用 HTML，而不是 raw Markdown？
- 公式是否作为数学内容渲染，并在窄屏可读？
- docs site 是否保护完整 HTML，不被坏缓存或 partial injection 覆盖？
- 如果 artifact 超过一页，是否有首页索引并预览所有子页面，且每个子页面都暴露 back-to-hub 链接、在 iframe 嵌入时自动隐藏？
- 如果要求远程预览，server/tunnel 是否有 supervisor？
