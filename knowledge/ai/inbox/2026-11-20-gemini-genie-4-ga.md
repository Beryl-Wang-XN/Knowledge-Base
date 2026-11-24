---
title: Genie 4 在 Interactions API 一般可用，视频输出每百万 $17.50
captured: 2026-11-20
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
  - name: Genie 4 模型页
    url: https://ai.google.dev/gemini-api/docs/models/genie-4
    tier: 一手
  - name: Gemini API 定价页 Genie 4
    url: https://ai.google.dev/gemini-api/docs/pricing#genie-4
    tier: 一手
---

## 是什么

Gemini API changelog 在 2026-11-19 写下 Genie 4（`models/genie-4`）一般可用。它走 Interactions API 的 `v1beta`，做实时、可操控的世界生成：流式输出 24 fps、16:9 视频，以及同步的 48 kHz 立体声。可以用文本、一张 16:9 参考图，或两者一起作为世界种子，会话中用 WASD、方向键和文本事件操控。changelog 写付费层标价是每百万输入 token $1.50、每百万文本输出 token $9.00、每百万视频输出 token $17.50，并写成大约每秒 $0.10，立体声包含在内。2026-10-27 的研究预览是另一阶段，不并进去。

模型页和定价页都已打开。模型代码也接受 `genie-4`。输入是 `world_setup` 的文本、一张 16:9 参考图，以及中途的文本操控和键盘、相机动作。输出是 1280×720、24 fps 的视频流，音频打进视频输出 token：WebSocket 上是 16-bit PCM，WebRTC 上是 Opus。每帧 240 个视频输出 token，24 fps 时每秒 5,760 token。单次会话最长 120 秒；视觉连贯和物体恒常性在前 45 到 90 秒最稳。WebRTC 上参考图要压到 48 KB 以下的 JPEG，避免 base64 事件超过 64 KB 的 SCTP 数据通道。服务区域写的是美国、西欧和日本。上下文缓存、函数调用、Batch、Flex、Priority、Live API 和图像生成都标成不支持。离线固定时长、多轮视频编辑和最高 4K 放大，模型页指向 Gemini Omni 1.2 Flash，不在这一条里。

定价页的 Genie 4 一节：没有免费层。付费层输入 $1.50（文本或参考图），文本输出 $9.00，视频输出 $17.50，立体声包含在视频价里。上下文缓存标成不可用。付费层写的是不用于改进产品。脚注把有效价格写成大约每秒 $0.10、大约每分钟 $6.05，并写要调用 `complete()` 结束会话，服务端生成和计费才会马上停。Batch、Flex、Priority 不支持。速率限制页这次没有打开，待核实。changelog 点名的交互生成指南和提示指南这次没有打开。

同日 changelog 的工具检索另记。

猜测挂靠：新的可调用模型 ID 和标价在 G。这是厂商型号和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-20：新建，status=open。
