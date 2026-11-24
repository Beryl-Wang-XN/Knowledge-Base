---
title: Gemini Interactions API 预览按需加载工具定义
captured: 2026-11-20
from: intel
module: D-serving
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

Gemini API changelog 在 2026-11-19 的另一节写下工具检索，状态是预览。Interactions API 可以搜索开发者自己的工具库，按需加载函数 schema，这样大工具集不必每次请求都整份送上。changelog 写，给工具标 `defer_loading: true`，并加上一个 `{"type": "tool_search"}` 工具，由 Gemini 取回 schema；或者把 `execution` 设为 `"client"`，改由调用方自己检索。远程 MCP 服务器也支持 `defer_loading`。

适用模型写的是 Gemini 3.6 及更新模型，包括全部 Gemini 4，并且只在 Interactions API。指南页这次没有打开。changelog 这一节没有标价，待核实。

同日的 Genie 4 一般可用另记。

猜测挂靠：请求里工具定义的加载方式在 D。这是供应商的接口能力，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-20：新建，status=open。
