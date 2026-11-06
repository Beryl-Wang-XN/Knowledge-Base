---
title: Mistral 公开预览 Managed Agents，同日还有一批 Studio 能力
captured: 2026-11-06
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: Mistral release notes
    url: https://docs.mistral.ai/resources/release-notes
    tier: 一手
---

## 是什么

Mistral 发布说明把 2026-11-05 标成一批新发布，头条是 Managed Agents，公开预览，Mistral 托管。

Managed Agents 用 Agents SDK（`mistralai-agents`）写一次代理：模型、指令、工具和环境定义一次，然后可以在本进程运行、用 `agents serve` 自托管，或用 `agents deploy` 交给 Mistral。部署后在后台执行，任务可以跑数小时或数天，崩溃后从最后完成的步骤恢复，也可以等人审批后再继续。发布说明写 Mistral 保存会话，使用方不必自备数据库。同条还列出：可选审批的工具调用、运行中可以转向或打断、按会话的沙箱、连接器与 MCP、skills、密钥、guardrails、自定义 hooks，以及默认送到 Studio 的追踪。

同一页、同一日期还有这些条目，本次不拆成多条：Workflow builder（公开预览，用自然语言生成并部署工作流）；HTTP API connectors（私有预览，用 HTTP 而不是只接 MCP）；`mistral apps` CLI（公开预览）；离线评测 SDK、托管数据集、从生产追踪建数据集、在线评测（均为公开预览）；托管搜索索引（公开预览，按名称、嵌入模型和可选 schema 提供向量索引）；webhooks 与 triggers（公开预览）；Studio apps 出现在 Vibe Code Web（一般可用）。

这页没有标价，价格待核实。

猜测挂靠：长时运行的托管代理和自托管工人，D。对标友商的代理运行时，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成调度或服务条目。

## 处置记录

- 2026-11-06：新建，status=open。
