---
title: OpenAI 更新日志补记 Agents 后台压缩、自动审批与定时任务
captured: 2026-11-08
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: OpenAI API changelog 2026-11-06 10:24 UTC 存档
    url: https://docswatch.stevetoth.ai/archive/20261106102425/https://developers.openai.com/api/docs/changelog/
    tier: 二手
  - name: Scheduled automations
    url: https://developers.openai.com/api/docs/guides/agents-api/sessions/automations
    tier: 一手
  - name: Automatic review
    url: https://developers.openai.com/api/docs/guides/agents-api/sessions/approvals
    tier: 一手
---

## 是什么

这次打开的 OpenAI API 更新日志，比 2026-11-06 10:24 UTC 的页面存档多出几条 Agents API 与 Live API 记录。存档里的 2026 年 11 月只有 11 月 5 日的 GPT-6 Cyber 和 11 月 4 日的 Images 2.6，10 月 30 日只有 GPT-6 Rosalind。这些新出现的条目自己的日期是 10 月 2 日、10 月 23 日、10 月 30 日和 11 月 2 日，不是 11 月 7 日的发布公告。上一次定时拉取没有记下它们。

现行更新日志里已读到的内容：

- 10 月 30 日：Agents API 公开测试里，上下文压缩默认改为在后台运行。把 `compaction.async` 设为 `false` 才是阻塞式压缩。页面写明后台压缩可能增加 token 用量。同条还有可选的 `experimental.time_awareness`，默认关闭。已有会话可以整表替换工具列表。
- 10 月 30 日：符合条件的项目可以把会话的 `review` 设为 `auto_review`，由模型批准或拒绝受支持的工具和权限请求。更新日志写明有额外的 token 计费。具体单价本次没有打开定价页，标 **待核实**。
- 10 月 23 日：Agents API 公开测试增加定时任务，可以在新会话或已有会话里安排一次或重复任务；打开 `automations` 工具后，代理可以在当前会话里安排自己的后续任务。
- 10 月 2 日：可以按单次根代理回合取回该回合的消息和工具调用，不必列出整个会话历史。
- 11 月 2 日：Live API 的外呼 SIP 对所有组织开放，经自有 SIP 服务商把 GPT-Live 接到电话号码。这和存档里更早的 Realtime API SIP IP 段不是同一条。

猜测挂靠：D（会话调度与代理运行方式）。后台压缩和自动审批会改变 token 用量，回顾时再决定要不要改挂 E。这是友商代理平台的计费与调度变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成调度或计费条目，也不改学习计划。

## 处置记录

- 2026-11-08：新建，status=open。
