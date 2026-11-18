---
title: Responses API 公开测试 2 小时和 8 小时后台完成窗口
captured: 2026-11-18
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: OpenAI Background mode
    url: https://developers.openai.com/api/docs/guides/background
    tier: 一手
---

## 是什么

API changelog 在 2026-11-17 另有一节：Responses API 公开测试可以选择两小时或八小时的后台完成窗口。相对标准价，两小时窗口的模型 token 单价低 30%，八小时低 40%。changelog 点名的模型是 `gpt-6.2-astra`、`gpt-6.2-sol`、`gpt-6.1-terra`、`gpt-6-luna`。接口是 `v1/responses`。

指南里的窗口表：`soonest` 是默认，没有折扣；`2h` 比标准价低 30%；`8h` 低 40%。完成目标从 API 接受请求时起算，并且只约束这一次响应。折扣打在每次符合条件的请求的模型 token 单价上，后续请求也包括在内。指南写，后续请求要沿用窗口、continuation ID、模型和项目，才能拿到更高的队列优先级。

打折窗口要求标准处理。`service_tier` 设为 `default` 即标准；设为 `auto` 时，只有 API 实际选中标准处理才符合折扣。`background` 设为 true，`background_options.completion_window` 设为 `2h` 或 `8h`，`stream` 不传或设为 false。`2h` 和 `8h` 与 Batch 共用 Batch/Background 速率限制，提交时按输入 token 计数。默认的 `soonest` 仍走普通请求和 token 限额。标准请求不能复用 `2h` 或 `8h` 后台请求写出来的提示缓存，即使提示相同。

指南还写，即使用 `store: false` 或 Zero Data Retention，后台模式也会临时保存响应数据，以便跑完并取回；`soonest`、`2h`、`8h` 的临时内容在静态存储时加密。

猜测挂靠：按完成时限打折的 token 单价在 E。这是价格档，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。GPT-6.2 的模型发布另记，这一条只记完成窗口。

## 处置记录

- 2026-11-18：新建，status=open。
