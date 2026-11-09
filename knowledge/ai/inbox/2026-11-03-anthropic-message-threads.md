---
title: Anthropic Messages API 公开测试 message threads
captured: 2026-11-03
from: intel
module: B-inference
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明（2026-11-02）
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Message threads 文档
    url: https://platform.claude.com/docs/en/build-with-claude/message-threads
    tier: 一手
  - name: Make long-running agents faster with message threads
    url: https://claude.com/resources/articles/message-threads
    tier: 一手
---

## 是什么

2026-11-02，Anthropic 在 Messages API 放出 **message threads** 公开测试。长对话和 agent 循环不必每轮重传整段历史：第一次请求带上完整对话、`system` 和 `tools`，并设置 `"thread": {"type": "create"}`；之后只发送新消息和上一则回复的 `id`（`"type": "continue"`）。每轮请求要带 beta header `message-threads-2026-08-12`。服务端在调用模型前把对话重新拼好。它和 Claude Managed Agents 里的 session threads 不是同一件事。

发布说明和文档写明：线程在最后一次请求后 5 分钟过期，并在最后一次使用后不超过 1 小时删除；续不上时继续请求返回 404，需要重新发送完整对话。文档写明价格和速率限制不变，且不符合零数据保留（ZDR），也不适用于已开启 HIPAA 准备的组织。产品文写明模型仍然每轮读完整段对话，因此 token 用量不变；并对大多数 Claude Code 用户默认打开后，50 万到 100 万 token 的请求，中位首 token 时间大约下降 35%。可用范围是 Claude API、Claude Platform on AWS、Claude Models on Google Cloud（Anthropic 托管）和 Claude in Microsoft Foundry，文档写明对每个模型都处于 beta。

猜测挂靠：B（首 token 时间，以及少做一遍上传和分词）。若回顾后确认重点是供应商的长会话服务方式，再决定是否同时看 D。Anthropic 是模型供应商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成推理或计费条目。

## 处置记录

- 2026-11-03：新建，status=open。
