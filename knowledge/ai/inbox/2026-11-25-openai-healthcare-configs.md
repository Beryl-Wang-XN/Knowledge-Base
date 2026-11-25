---
title: OpenAI 在 Responses API 放出四款医疗配置
captured: 2026-11-25
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API Changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: Healthcare model configurations in the OpenAI API
    url: https://help.openai.com/en/articles/20001656-healthcare-model-configurations-in-the-openai-api
    tier: 一手
  - name: OpenAI Model Release Notes
    url: https://help.openai.com/en/articles/9624314-model-release-notes
    tier: 一手
  - name: OpenAI API Pricing
    url: https://developers.openai.com/api/docs/pricing
    tier: 一手
---

## 是什么

OpenAI API changelog 的 2026-11-24 节放出四款 Healthcare model configurations，走 Responses API：`gpt-6.2-astra-healthcare`、`gpt-6.2-sol-healthcare`、`gpt-6-astra-healthcare`、`gpt-6.1-sol-healthcare`。changelog 写它们给选出的模型配一套面向临床问题的 harness；模型使用网页搜索时，搜索的是一份医学来源索引。帮助中心和模型发布说明同一天也有这一节。帮助中心写，要使用这份医疗索引，请求里必须打开网页搜索。

帮助中心写，API 组织可以直接用，不需要 ChatGPT for Healthcare 或 ChatGPT Enterprise 工作区。能调用不等于可以处理受保护健康信息；处理 PHI 之前，组织要有适用的 Business Associate Agreement，并满足账户和工具配置要求。这些配置不代替专业医疗判断。`gpt-6.2-astra-healthcare` 的模型页这次打开是 404，上下文长度和知识截止日期标 **待核实**。

定价页按每百万 token 列出标准价。短上下文在前、长上下文在后：

- `gpt-6.2-astra-healthcare`：输入 $8.00 / $16.00，输出 $40.00 / $60.00，缓存输入 $0.40 / $0.80，30 分钟缓存写入 $10.00 / $20.00，12 小时缓存写入 $20.00 / $40.00。
- `gpt-6.2-sol-healthcare`：输入 $2.00 / $4.00，输出 $10.00 / $15.00，缓存输入 $0.10 / $0.20，30 分钟缓存写入 $2.50 / $5.00，12 小时缓存写入 $5.00 / $10.00。
- `gpt-6-astra-healthcare`：输入 $10.00 / $20.00，输出 $50.00 / $75.00，缓存输入 $1.00 / $2.00。30 分钟和 12 小时缓存写入这一行是空的。
- `gpt-6.1-sol-healthcare`：输入 $2.00 / $4.00，输出 $10.00 / $15.00，缓存输入 $0.10 / $0.20。缓存写入这一行也是空的。

同一页的 Fast 档只有输入、输出和缓存输入。短上下文在前、长上下文在后：Astra 医疗是 $16.00 / $80.00 / $0.80 对 $32.00 / $120.00 / $1.60；Sol 6.2 医疗是 $4.00 / $20.00 / $0.20 对 $8.00 / $30.00 / $0.40；GPT-6 Astra 医疗是 $20.00 / $100.00 / $2.00 对 $40.00 / $150.00 / $4.00；GPT-6.1 Sol 医疗是 $4.00 / $20.00 / $0.20 对 $8.00 / $30.00 / $0.40。

定价页写，上述四款医疗配置的促销价至少保留到 2026-12-31。医疗这一节没有写短上下文和长上下文的 token 分界，分界标 **待核实**。

猜测挂靠：模型身份和标价在 G。这是供应商的新配置和目录价，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-25：新建，status=open。
