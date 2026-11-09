---
title: Gemini Embedding 2 预览模型名弃用并转到正式模型
captured: 2026-11-07
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
---

## 是什么

Gemini API changelog 的 2026-11-06 节写明：`gemini-embedding-2-preview` 已弃用。自 2026-11-06 起，发往这个模型名的请求会转到 `gemini-embedding-2`，并按 Gemini Embedding 2 的费率计。changelog 写两者使用同一套 API schema、定价和 embedding 空间，因此不需要改其他代码，也不需要重新做向量索引。应把模型名改成 `gemini-embedding-2`。

本次没有打开定价页，不抄具体单价。

猜测挂靠：G（模型档案里的版本与计费身份）。这是供应商的模型切换，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不改 `registry/`，也不写成模型档案。

## 处置记录

- 2026-11-07：新建，status=open。
