---
title: 百炼下线 qwen4-max-preview，原 ID 改按 Qwen4-Max 标准价
captured: 2026-11-26
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: 阿里云百炼模型上架与更新
    url: https://help.aliyun.com/zh/model-studio/newly-released-models
    tier: 一手
  - name: Model releases and updates
    url: https://help.aliyun.com/en/model-studio/newly-released-models
    tier: 一手
  - name: 阿里云百炼模型价格
    url: https://help.aliyun.com/zh/model-studio/model-pricing
    tier: 一手
---

## 是什么

百炼中文和英文上架页仍把 `qwen4-max-preview` 放在 2026-11-11 那一节，并新写它已于 2026-11-25 下线。原模型 ID 的请求自动路由到 Qwen4-Max，按 `qwen4-max` 标准价格计费，预览期的限时折扣不再适用。页上这次没有重写钟点。11 月 12 日的 inbox 已经记下预览期到北京时间 2026-11-25 24:00，这一条只补下线后的路由和计费。

价格页千问 Max 一节，输入不超过 1M token 时，`qwen4-max` 的标准价是：华北 2（北京）输入 10 元、输出 30 元 / 百万 token，并有 100 万 token 免费额度。美国（弗吉尼亚）有两行，服务部署范围「全球」为 10 元 / 30 元，「弗吉尼亚」为 10.938 元 / 32.813 元。新加坡「国际」为 10.938 元 / 32.813 元。德国（法兰克福）、日本（东京）、中国香港的「全球」行都是 10 元 / 30 元。输出列写的是思维链加回答。

北京这一行标了 Batch 调用半价。节首写，支持 Batch 时输入和输出按实时推理价的 50%，而且不能和上下文缓存折扣同时生效。这些行都标了上下文缓存享有折扣，缓存单价不在这一行，标 **待核实**。

猜测挂靠：下线后的路由和目录价在 G。这是供应商的价格变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改 11 月 12 日那条。

## 处置记录

- 2026-11-26：新建，status=open。
