---
title: Gemini API 为 Gemini 3.8 TTS 增加 Voice remixing
captured: 2026-11-05
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Gemini API release notes（2026-11-04）
    url: https://aistudio.google.com/docs/changelog
    tier: 一手
  - name: Voice remixing
    url: https://aistudio.google.com/docs/voice-remixing
    tier: 一手
---

## 是什么

Gemini API 发布说明的 2026-11-04 条目发布 Voice remixing。它改的是已有的预置音色或用 Voice design 做好的音色，用自然语言说明相对修改，生成一个新的、独立保存的音色，不改原来的音色。

发布说明写的调用方式是 `POST /v1beta/voices`，创建模型用 `gemini-3.8-flash-tts`，得到 `voice_...` ID 后，再用 Gemini 3.8 Flash TTS 或 Gemini 3.8 Flash-Lite TTS 合成。指南里还写了：付费档（Tier 1 及以上）才能用；每个项目最多 200 个 `store=True` 的音色，设计和 remix、复刻的保存音色共用这个额度；不用则 1 年后过期，再次合成或把它当作下一次 remix 的底音色会重置这 1 年。

发布说明和这份指南都没有单独标价。语音合成是否沿用这两枚 TTS 模型的原价，标 **待核实**。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写入模型档案。

## 处置记录

- 2026-11-05：新建，status=open。
