---
title: Claude 组织 webhook 增加客户自管密钥的失败和恢复事件
captured: 2026-11-23
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Claude Platform 发布说明 2026-11-19 存档
    url: https://docswatch.stevetoth.ai/archive/20261119103448/https://platform.claude.com/docs/en/release-notes/overview/
    tier: 二手
  - name: AI Docs Watch
    url: https://docswatch.stevetoth.ai/anthropic/claude-platform-release-notes/2026-11-22/
    tier: 二手
---

## 是什么

Claude Platform 发布说明现在的 2026-11-16 那一节，在已记过的旧模型文本水印之外，多了一句：组织 webhook 增加两种事件，仍是 beta。密钥管理服务持续拒绝客户自管加密密钥时发送 `external_key.failed`，密钥恢复可用时发送 `external_key.recovered`。这一节的日期标题仍是 November 16，没有单独的 2026-11-22 节。

2026-11-19 10:34 UTC 的同一页存档里，11 月 16 日那一节只有水印，没有这两句。文档监测站把首次看见写在 2026-11-22 10:17 UTC，并写变化发生在 11 月 19 日存档和这次抓取之间。发布说明页本身没有写这两句是哪一小时加上的。

现行页只写出事件名和触发条件。载荷、重试，以及「持续拒绝」要多少次才发送，这次没有另开文档。没有单独标价。

猜测挂靠：供应商平台能力在 F。这是友商接口变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改已有的水印条目。

## 处置记录

- 2026-11-23：新建，status=open。
