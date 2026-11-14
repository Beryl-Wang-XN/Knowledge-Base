---
title: DeepSeek 开放全家桶应用 API，文件解析与语音另有标价
captured: 2026-11-14
from: intel
module: E
business: true
status: open
review_after:
entry:
sources:
  - name: DeepSeek API 更新日志
    url: https://api-docs.deepseek.com/updates/
    tier: 一手
  - name: DeepSeek 更新日志（中文）
    url: https://api-docs.deepseek.com/zh-cn/updates
    tier: 一手
  - name: DeepSeek 全家桶应用 API 新闻
    url: https://api-docs.deepseek.com/news/news261113/
    tier: 一手
  - name: DeepSeek 发布全家桶应用 API（中文）
    url: https://api-docs.deepseek.com/zh-cn/news/news261113/
    tier: 一手
  - name: DeepSeek Models & Pricing
    url: https://api-docs.deepseek.com/quick_start/pricing
    tier: 一手
  - name: DeepSeek 模型与价格（中文）
    url: https://api-docs.deepseek.com/zh-cn/quick_start/pricing
    tier: 一手
  - name: Build a Chatbot
    url: https://api-docs.deepseek.com/guides/build_a_chatbot
    tier: 一手
---

## 是什么

2026-11-13，DeepSeek 更新日志写下了全家桶应用 API。`deepseek-flash`（版本 DeepSeek-V4.1-Flash-1017）在 Messages、Responses 和 Chat Completions 里支持这些对话能力，工具调用和上下文拼接由服务端完成。指南列出的端点是 `POST https://api.deepseek.com/anthropic/v1/messages`、`POST https://api.deepseek.com/responses`、`POST https://api.deepseek.com/chat/completions`。

更新日志写明的能力：非思考模式打开 `deepseek_web_search` 后做网页或图片搜索并附引用；思考模式打开同一工具后，在多步推理里自行搜索和阅读链接；上传 PDF、Office、图片等，经纯文本提取或图文混排解析后拼进上下文；打开 `deepseek_read_url` 后识别用户消息里的链接并抓取网页。对外提供服务时要打开安全校验参数，服务会审核输入和输出，命中风险时返回拒答标识；内容安全审核、大模型登记和 AI 标识仍由调用方承担。参数的具体字段名这次没有在更新日志里对上，待核实。

Search、Fetch、OCR、ASR、TTS 也可以作为独立接口调用。官方开源了一个可导入 DeepSeek 历史对话的演示客户端，体验入口是 `https://cdn.deepseek.com/chat-demo`，代码在 `https://github.com/deepseek-ai/chat-demo`。

价格页已打开。搜索（文字、图片）和网页抓取仍是每 1,000 次 5 元 / $0.75，和 2026-11-01 已记的 Search/Fetch 计费相同，这次不另当成新标价。新出现的是：文件解析与 OCR API 每 1,000 页 1.5 元 / $0.225。语音合成每 10,000 字符刊例价 3 元 / $0.45，限时 5 折为 1.5 元 / $0.225。语音识别每小时音频刊例价 0.78 元 / $0.116，限时 5 折为 0.39 元 / $0.058。价格页的折扣表没有写出结束日期。更新日志没有把模型 token 单价写成这次调整。

猜测挂靠：新增的按页、按字符和按小时标价在 E。这是供应商的接口和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成成本或模型条目。

## 处置记录

- 2026-11-14：新建，status=open。
