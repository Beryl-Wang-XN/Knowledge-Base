---
title: Gemini 平台预览语义治理策略，在工具调用前检查
captured: 2026-11-21
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: Google Developers Blog
    url: https://developers.googleblog.com/check-what-your-ai-agents-do-before-they-do-it-with-semantic-governance-policies/
    tier: 一手
---

## 是什么

Google Developers Blog 的日期是 2026-11-20。Semantic governance policies 在 Gemini 平台进入预览。它在智能体提议的工具调用执行之前做两次检查：对照用自然语言写的规则，以及对照用户原来的请求。用户意图检查默认打开。两次都通过，调用才执行；不通过时，响应里的工具调用被换成可配置的拒绝消息。裁决、理由和裁判所用的 token 写入客户项目的 Cloud Logging。只有文本、没有动作的响应不检查。流式模型响应不检查。

目前的策略执行点是 Agent Gateway，智能体的出站流量要经过它。博客写智能体的模型可以走 Gemini API、Anthropic Messages API、Gemini 平台上的 Claude，或 OpenAI 兼容的 Chat Completions，包括自托管的 vLLM。裁判是一个 LLM，结果是概率性的，博客建议先用 dry run，只记录会拒绝什么、先不拦截。Gemini API changelog 这次没有 2026-11-20 节，最新仍是已记的 2026-11-19。这篇没有写策略或裁判的单价，待核实。

猜测挂靠：请求出站前的策略执行在 D。这是供应商的智能体治理能力，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改 `registry/`。

## 处置记录

- 2026-11-21：新建，status=open。
