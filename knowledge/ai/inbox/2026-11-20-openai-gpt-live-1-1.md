---
title: GPT-Live-1.1 上线，两款 Live 模型增加 WebRTC 待机价
captured: 2026-11-20
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: GPT-Live-1.1 模型页
    url: https://developers.openai.com/api/docs/models/gpt-live-1.1
    tier: 一手
  - name: OpenAI API 定价页 GPT-Live
    url: https://developers.openai.com/api/docs/pricing
    tier: 一手
  - name: Managing GPT-Live sessions
    url: https://developers.openai.com/api/docs/guides/live-conversations
    tier: 一手
---

## 是什么

OpenAI API changelog 在 2026-11-19 写下 GPT-Live-1.1（`gpt-live-1.1`），接口是 `v1/live/sessions`。changelog 写它改进多语言语音对话里的发音、口音一致性和转写，并让开发者用现有 Live 会话配置换成这个模型 ID，再用自然语言说明何时把任务交给自己的后端。同一节写，可以为 GPT-Live-1 和 GPT-Live-1.1 的 WebRTC 会话配置待机：不活动时暂停推理，有人说话再恢复。新闻室产品列表这次没有对上同日帖。

模型页已打开。它是全双工语音模型，能在说话时听。相对 GPT-Live-1，转写更准，跨语言的口音和声音更稳。输入是音频和文本，输出是音频和文本。默认快照就是 `gpt-live-1.1`。支持流式和函数调用。Chat Completions、Responses、Realtime、Batch、微调、嵌入、图像、视频和审核都不支持。语音会话按时长计费，后端模型和工具另计。并发会话限额和 GPT-Live-1 分开，各算各的，并跨推理区域合计；模型页没有给出分档数字，待核实。知识截止这次没有在模型页上看到，待核实。

定价页的 GPT-Live 表已打开。`gpt-live-1.1` 和 `gpt-live-1` 都是活跃每分钟 $0.05、待机每分钟 $0.02。页上写语音会话按秒计。1.1 模型页写，较低的待机价用于推理暂停期间的 WebRTC 会话。是否按整分钟进位，1.1 模型页和定价页这一节都没有写，待核实。

会话指南的待机一节已打开。创建 WebRTC 会话时，把 `session.wake_policy.type` 设为 `speech`，会等说话再开始推理。`session.idle_timeout_s` 取 5 到 60 的整数，表示多少秒没有输入或输出转写就回到待机。不填这个超时，第一次唤醒之后推理会一直保持活跃，直到会话结束。可选的 `session.wake_policy.vad_threshold` 从 0 到 1，默认 0.5，第一次唤醒和每次暂停后都用。待机时麦克风音轨要保持打开，连接和会话 ID 不变，恢复时带回对话历史。`session.paused` 表示进入待机，`session.resumed` 表示推理已就绪。指南写待机时长的单价低于活跃时长。把麦克风静音不会结束会话，会话仍按活跃计。指南这一节讲的是 WebRTC；SIP 是否能待机，changelog 和这一节都没有写，待核实。

猜测挂靠：新的语音模型 ID 和按时长标价在 G。这是厂商型号和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-20：新建，status=open。
