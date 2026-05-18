# HTML Artifact Prompt Examples

## General

```text
不要写 Markdown。请做一个单文件 HTML artifact，帮助我理解、比较和决策这个问题：
{问题}
要求：
- 有 Executive Summary
- 有可视化结构
- 有对比表
- 有风险和建议
- 有下一步 action
- 将所有源材料渲染为 HTML 正文，不要保留 raw Markdown appendix
- 提供中文和 English 两个阅读路径
- 单文件 HTML，可直接浏览器打开
```

## Exploration

```text
请生成一个 HTML exploration artifact。
主题：{主题}
请给我 6 个明显不同的方案，用卡片网格并排展示。
每个方案都要写：
- 核心思路
- 适合谁
- 优点
- 缺点
- 实现成本
- 风险
- 推荐指数
最后给出你的推荐组合方案。
```

## Implementation Plan

```text
请生成一个 HTML implementation plan。
目标：{目标}
请包含：
- 总体架构
- 数据流图
- 文件改动列表
- API/schema 设计
- 关键代码片段
- 风险点
- 测试计划
- 分阶段任务拆解
要求视觉清晰，方便我之后直接交给另一个 agent 会话实现。
要求维护中文和英文两个版本，站点型输出请提供 `html_zh` / `html_en` 路径或 manifest 字段。
```

## PR Review

```text
请基于当前 git diff 生成一个 HTML code review artifact。
重点：
- 解释这个 PR 做了什么
- 渲染关键 diff
- 对关键代码加旁注
- 按 Blocker / Major / Minor / Nit 标注问题
- 画出相关数据流或调用链
- 给出必须修改项和建议修改项
不要只写文字，要做成方便审阅的 HTML。
```

## Temporary Editor

```text
请做一个单文件 HTML 临时编辑器，用来处理下面的数据：
{数据}
我需要完成的操作是：{排序 / 分桶 / 打标签 / 修改配置 / 调 prompt}
要求：
- 自动给出初始建议
- 支持手动编辑
- 支持搜索或筛选
- 对冲突或异常给出警告
- 提供 Copy as HTML / JSON / Prompt 按钮
- 导出的内容要能直接粘回 agent 使用
- 如这是持久化工具，请提供中文 / English 两个界面入口
```

## Documentation Site

```text
请把这组 Markdown / HTML / JSON 材料整理成一个 HTML artifact 文档站点。
要求：
- 所有 Markdown 内容都转成浏览器原生 HTML 正文，不要保留 Original Markdown Source Appendix。
- 每个页面都维护中文版和英文版。
- 中文页面使用 canonical path，英文页面放在 en/ 下。
- 每页顶部提供 中文 / English 切换。
- index 和 manifest 都要记录双语入口，例如 html_zh / html_en。
- 同名 HTML artifact 如对应 Markdown source，应继承 source 的历史日期；无 source 的 standalone HTML artifact 可使用文件时间。
- 导出按钮优先提供 HTML / JSON / Prompt。
```

