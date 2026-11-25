---
title: OpenAI 更新 chat-latest 指向的快照
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
  - name: Chat Latest
    url: https://developers.openai.com/api/docs/models/chat-latest
    tier: 一手
  - name: OpenAI API Pricing
    url: https://developers.openai.com/api/docs/pricing
    tier: 一手
---

## 是什么

OpenAI API changelog 的另一节，日期也是 2026-11-24，写更新了 `chat-latest` 快照。它指向 ChatGPT 里 Plus、Pro、Business 和 Enterprise 当前可用的最新模型。changelog 建议生产环境用 GPT-6.2 系列，并写底层快照会定期更换。这一节没有写出换到了哪一个快照。

模型页把 `chat-latest` 写成 ChatGPT 当前使用的最新 Instant 模型，并建议生产环境用 GPT-6.2 Astra。页上的规格是：文本和图像输入，文本输出；上下文 400,000；最大输入 272,000；最大输出 128,000；知识截止 2026-04-20。支持 Chat Completions 和 Responses，不支持 Batch。模型页和定价页的文本 token 价都是每百万 token 输入 $5、缓存输入 $0.50、输出 $30。页上没有写这次快照更新是否改了标价。

猜测挂靠：模型身份和目录价在 G。这是供应商在售的移动别名，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-25：新建，status=open。
