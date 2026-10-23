---
title: OpenAI Decisions API 正式可用，按 input token 计费
captured: 2026-10-23
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI《Build more responsive apps with the Decisions API》
    url: https://openai.com/index/decisions-api/
    tier: 一手
---

## 是什么

2026-10-22，OpenAI 宣布 Decisions API 正式可用。公告写明它基于 GPT-6 Luna，用来回答有界问题：分类、路由，或决定智能体的下一步。输入可以是文本、图片或原生 JSON。返回三种结果：predicate（条件为真的概率）、choice（从给定选项里选一个，并带概率和置信度）、score（按有序等级打出的加权分）。

公告中的产品口径：相对同一模型走 Responses API，最快约 10 倍；单次请求最多 400 个问题；已接入 GPT-Live；推理驻留写的是美国和欧洲。公告写明的价格是每百万 input token 0.10 美元，缓存 input 每百万 0.01 美元，不收取 output token 费用。30 分钟和 12 小时缓存写入的价格，公告指向定价指南，这次没有打开该页，标待核实。

## 为什么没在当天处理

这是 2026-10-23 的定时情报拉取，不是当天的学习主轨。先留在 inbox，等用户回顾后再决定要不要核进计费或路由相关条目。

## 处置记录

- 2026-10-23：新建，status=open。
