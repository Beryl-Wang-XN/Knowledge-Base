---
title: OpenRouter 图像响应拿掉必填 b64_json，并增加语音模型列表
captured: 2026-11-20
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: OpenRouter API changelog
    url: https://openrouter.ai/docs/changelog
    tier: 一手
---

## 是什么

OpenRouter API changelog 有一节日期是 2026-11-19。破坏性变更写：`ImageGenerationResponse.data` 上必填的 `b64_json` 被拿掉，用于 `POST /images`。同一节的 schema 变更写，图像请求新增 `response_format`；图像响应新增 `expires_at` 和 `data.url`，并写 `b64_json` 属性有更新。changelog 没有写更新后的 `b64_json` 是否还能返回，待核实。

新端点是 `GET /audio/speech/models` 和 `GET /audio/speech/models/{author}/{slug}`，用来列出和读取文本转语音模型。这次没有打开这两个接口，目录里有哪些模型、什么单价，待核实。`POST /audio/transcriptions` 的请求 schema 新增 `prompt`。视频生成响应新增 `progress` 和 `status_detail`。

同一节里还有 SCIM 组映射、workspace 描述，以及 `POST /credits/purchases` 的 `x-payment-info`，都是描述或 schema 附注，不另开。公告博客最新仍是 2026-11-16，没有对上这一节的产品帖。2026-11-18 那一节的推理格式改名落在上一窗口，不补记。

猜测挂靠：图像和语音接口的返回与目录在 D。这是路由供应商的接口变更，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-20：新建，status=open。
