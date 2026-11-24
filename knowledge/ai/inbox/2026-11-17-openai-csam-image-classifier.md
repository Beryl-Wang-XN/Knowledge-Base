---
title: OpenAI 向获批组织提供免费的 CSAM 图像分类模型
captured: 2026-11-17
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
---

## 是什么

OpenAI API changelog 的 2026 年 11 月一节新增 Nov 16。条目类型是 Feature，模型是 `omni-moderation-csam-latest`，端点是 `v1/moderations`。页上写：获批组织可以免费使用 OpenAI CSAM Image Classifier，用来帮人工复核排列图像优先级。模型分别给出可能是儿童性虐待材料（CSAM）的信号，以及可能是 AI 生成 CSAM 的信号。

更新日志指向的说明页这次打开是 404，所以没有更多的准入条件、速率或信号字段。页的 `last-modified` 是 2026-11-16 23:25:19 GMT。同页更早的一节仍是 11 月 5 日的 `gpt-6-cyber`。

猜测挂靠：新的审核模型 ID 和零价格在 G。这是供应商的模型和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-17：新建，status=open。
