---
title: 火山方舟写出 DeepSeek-V4.1-Flash 经济版，同权重、单价更低
captured: 2026-11-15
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: 火山方舟 DeepSeek-V4.1-Flash（升级 1017）
    url: https://ark.volcengine.com/region:cn-beijing/docs/deepseek-v4-1-flash
    tier: 一手
  - name: 火山方舟模型价格
    url: https://ark.volcengine.com/region:cn-beijing/docs/model-pricing
    tier: 一手
  - name: 火山方舟续写模式
    url: https://ark.volcengine.com/region:cn-beijing/docs/continuation-mode
    tier: 一手
  - name: 火山方舟创建 Message
    url: https://ark.volcengine.com/region:cn-beijing/docs/messages-api
    tier: 一手
---

## 是什么

2026-11-14，火山方舟三篇文档的更新时间都是 2026-11-14T10:24:25Z：DeepSeek-V4.1-Flash（升级 1017）、续写模式、创建 Message。模型发布公告目录的更新时间仍是 2026-11-13，202611 一节仍只有 `doubao-seed-evolving`，没有这一条的上线行。没有另见一篇写明当天上线的公告。

模型页把这一系列写成 552B 总参数 MoE，并列出两个版本。推荐版本 `deepseek-v4-1-flash-261017`，相对 `deepseek-v4-1-flash-260910` 提升复杂编程与完整项目开发，并缩短任务运行时间和输出长度。经济版 `deepseek-v4-1-flash-economy-261017` 与标准版使用完全相同的模型权重，能力和效果一致；价格更低，回答生成速度略慢。页上没有给出慢多少。

价格页已打开，它自己的更新时间是 2026-11-13T10:24:08Z，早于上面三页。在线推理（常规）按请求完成时间落入的时段计费。高峰时段是北京时间周一至周五 09:00–12:00、14:00–18:00，其余为空闲时段。单位是元 / 百万 tokens，缓存存储是元 / 百万 tokens / 小时。`deepseek-v4-1-flash`：空闲输入 1.00、输出 4.00、缓存命中 0.02；高峰输入 2.00、输出 8.00、缓存命中 0.04；缓存存储 0.017。`deepseek-v4-1-flash经济版`：空闲输入 0.80、输出 3.20、缓存命中 0.016；高峰输入 1.60、输出 6.40、缓存命中 0.032；缓存存储同样 0.017。两行的音频输入和音频缓存命中都是空的。

续写模式表已打开。经济版和 `deepseek-v4-1-flash-261017`、`deepseek-v4-1-flash-260910` 一样：Chat API 要直接预填并加 `prefix=true`，Responses API 要直接预填并加 `partial=true`，Messages API 不支持。创建 Message 的错误响应里，`type` 和 `request_id` 旁都写着，当前仅 `deepseek-v4-1-flash-261017` 和 `deepseek-v4-1-flash-economy-261017` 支持返回该字段。

猜测挂靠：新的模型 ID 和标价在 G。这是供应商的型号和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-15：新建，status=open。
