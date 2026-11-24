---
title: Gemini Decision 1 与 Decisions API 上线，输入 $0.10、输出不计 token
captured: 2026-11-12
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Gemini Decisions API
    url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
    tier: 一手
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
  - name: Gemini Decision 1 模型卡
    url: https://ai.google.dev/gemini-api/docs/models/gemini-decision-1
    tier: 一手
  - name: Decisions API 指南
    url: https://ai.google.dev/gemini-api/docs/decisions-api
    tier: 一手
  - name: Gemini API 定价页 Gemini Decision
    url: https://ai.google.dev/gemini-api/docs/pricing#gemini-decision
    tier: 一手
  - name: Gemini API 速率限制 Gemini Decision
    url: https://ai.google.dev/gemini-api/docs/rate-limits#gemini-decision
    tier: 一手
---

## 是什么

2026-11-11，Google 博客和 Gemini API changelog 都写下了 Gemini Decision 1（`gemini-decision-1`）和 Decisions API。它不是逐 token 生成文本，而是对同一份输入做有界判断：yes/no、单选、有序量表。模型卡写输入上限 262,144 token，单次最多 1,000 个互不影响的问题，输出 token 上限为 0。输入可以是文本、图片、视频、音频和 PDF。指南里 yes/no 的类型名写成 `noul`，返回 0.01 到 0.99 的概率和置信度；choice 与 score 各支持 2 到 255 个选项或等级。文档写需要 `google-genai` 或 `@google/genai` 3.2 及以上，端点是 `v1beta` 的 `decisions`。

定价页已打开。付费层输入（文本、图片、视频、音频、PDF）每百万 token $0.10，输出标成不适用，因为是 0 个输出 token。共享输入按一次计费，每道题再加自己的说明和标准。免费层输入不收费。上下文缓存写的是不可用，Batch API 不支持。速率限制页：Free 为 200 RPM、50,000 TPM、10,000 RPD；Tier 1 为 1,500 / 1,000,000 / 50,000；Tier 2 为 5,000 / 4,000,000 / 不限 RPD；Tier 3 为 15,000 / 10,000,000 / 不限 RPD。

博客还写，在最多 16K token 的上下文上，模型计算中位延迟约 50–100 ms，端到端约 150–250 ms，问题数从 1 到 100 时几乎持平。同一篇说，在他们共用的基准上，相对 Gemini 3.5 Flash-Lite 走 Interactions API，大约便宜近 5 倍。博客写 Gemini in Google Cloud 还没接上，是即将支持。模型卡的最新更新只写 November 2026，没有更细的日。

这和 2026-10-23 已合并的 OpenAI Decisions API 是同一类计费形状：按输入计、不收输出 token。两边的缓存和速率不是同一页，这里不并成一条。

猜测挂靠：新模型在 G。新模型 ID 和标价是对标友商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-12：新建，status=open。
