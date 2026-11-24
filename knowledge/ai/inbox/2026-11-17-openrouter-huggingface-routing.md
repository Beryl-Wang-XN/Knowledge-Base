---
title: Hugging Face 的语言模型推理改由 OpenRouter 路由
captured: 2026-11-17
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: OpenRouter 公告
    url: https://openrouter.ai/blog/announcements/hugging-face-inference-providers/
    tier: 一手
  - name: Hugging Face 博客
    url: https://huggingface.co/blog/openrouter
    tier: 一手
---

## 是什么

2026-11-16，OpenRouter 和 Hugging Face 都宣布：Hugging Face Inference Providers 上的聊天模型改由 OpenRouter 选供应商。OpenRouter 的帖子署名日期是 11/16/2026。Hugging Face 的帖子写 Published November 16, 2026。两边都写，现有的 Hugging Face token 和调用代码可以继续用。路由按实时价格、速度和可靠性选择供应商。一个供应商变慢或失败时，同一次调用会转到下一个。

Hugging Face 写，以前一次请求只选一个供应商，失败就返回那个错误。现在可以在模型 ID 后加后缀：默认是价格、速度和可靠性的组合，`:fastest` 要吞吐，`:cheapest` 要低价，也可以写死一个供应商名。对话会留在持有这份 prompt cache 的供应商上；要用 `X-HF-Session-Id` 把头固定成一次对话的 UUID。协议写支持 OpenAI Chat Completions、Responses，以及 Anthropic Messages。

价格：Hugging Face 写，你仍付供应商的价格，账单在 Hugging Face，Hugging Face 不加价。PRO 每月 2 美元额度，Team 和 Enterprise 每个席位 2 美元。图像、视频和音频生成仍走 Hugging Face 自己的 Inference Providers，不经过 OpenRouter。语言模型不再接受用户自带的供应商 API key；图像和视频的自带 key 仍可用。

OpenRouter 写，今天有 160 个模型、来自 38 个实验室，也就是 OpenRouter 在 Hub 上有页面的全部模型。它把 10 月重建路由时的一次线上实验写成：容量错误少 46%，首 token 时间快 16.9%，吞吐高 16.3%，单次请求成本高 6.0%。Hugging Face 转述了前三个比例，没有写这 6.0%。Hugging Face 还写 OpenRouter 每月服务超过 800 万亿 token、超过 1000 万用户、600 多个模型、80 多个供应商。这些都是两篇帖子里的数字。

OpenRouter 另外写，可以把每次请求的 trace 发到用户自己的 Hugging Face Storage Bucket，这项在 beta。每个 JSON 含输入消息、模型输出、token 数和费用，不含图像和其他媒体。

猜测挂靠：请求选路和故障转移在 D。这是两家供应商的推理路由变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-17：新建，status=open。
