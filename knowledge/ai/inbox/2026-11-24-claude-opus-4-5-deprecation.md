---
title: Claude Opus 4.5 弃用，Anthropic 自营平台预定 2027-01-22 停用
captured: 2026-11-24
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Claude 模型弃用页
    url: https://platform.claude.com/docs/en/about-claude/model-deprecations
    tier: 一手
---

## 是什么

Claude Platform 发布说明的 2026-11-23 节宣布弃用 Claude Opus 4.5，模型 ID 是 `claude-opus-4-5-20251101` 和 `claude-opus-4-5`。Claude API 上的停用日写的是 2027-01-22，建议迁到 Claude Opus 5.5。

弃用页的状态表把 `claude-opus-4-5-20251101` 标成 Deprecated，弃用日 November 23, 2026，暂定停用日 January 22, 2027。历史节写，停用包含不带日期的 `claude-opus-4-5`，推荐替换是 `claude-opus-5-5`。同一页写，这些日期适用于 Anthropic 自营平台：Claude API、Claude Platform on AWS、Claude Models on Google Cloud（Anthropic 托管）和 Microsoft Foundry。Claude Code 走 Claude API 时也用这些日期；若 Claude Code 接到别的平台或网关，日期跟实际提供请求的平台走。

同一页写，Google 托管的 Claude Models 和 Amazon Bedrock（`bedrock-mantle` 与 `bedrock-runtime`）各自排停用时间，生命周期和日期可以不同。那两张表这次没有打开。停用之后，对已停用模型的请求会失败。页上的一般政策写，公开发布的模型至少提前 60 天通知；这一条没有另写 Opus 4.5 的通知邮件。没有新的 token 标价。

猜测挂靠：模型生命周期在 G。这是友商模型的停用安排，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改 `registry/`。

## 处置记录

- 2026-11-24：新建，status=open。
