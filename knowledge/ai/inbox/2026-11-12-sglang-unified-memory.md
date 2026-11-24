---
title: SGLang 试验统一显存，混合注意力不再事先切池
captured: 2026-11-12
from: intel
module: B-inference
business: false
status: open
review_after:
entry:
sources:
  - name: LMSYS Unified Memory in SGLang
    url: https://www.lmsys.org/blog/2026-11-11-unified-memory
    tier: 一手
  - name: SGLang Releases
    url: https://github.com/sgl-project/sglang/releases
    tier: 一手
---

## 是什么

LMSYS 于 2026-11-11 发了 SGLang 统一显存的说明。混合模型把全注意力 KV、滑动窗口 KV 和循环状态放在一起。默认实现用 `--swa-full-tokens-ratio` 和 `--mamba-full-memory-ratio` 在启动时把显存切成互不相通的池。新旗标 `--enable-unified-memory` 改成一块 arena：全注意力从高地址往下长，有界状态从低地址往上长，空闲字节留在中间，按各自的页或槽大小取用。博文写它仍是试验功能，还不是默认内存系统。

博文点名的模型包括 GPT-OSS、Muse Spark、Qwen3.5，以及 Kimi K3 / K3.1。K3.1 的 DSA 索引和 MLA KV 要打进同一个 token 条目。全注意力模型、带滑动窗口的 MLA，以及 DeepSeek-V4，博文写目前不支持。优先级抢占在这个旗标下关掉。PD 分离要求 Mooncake，并且不能和流水线并行、投机解码或 DCP 同时开。

吞吐数字是这篇自己的测量，条件写在文中：提交 `daa171846f`，每台服务器一张 H200，和默认分池比，两次运行取平均。GPT-OSS-20B、512 输入 / 1,536 输出、1,024 并发时，统一显存大约同时跑 1,000 个请求，默认分池是 618，吞吐高 14%，首 token 时间 6 秒对 43 秒。同一节还写 Qwen3.5-4B 在短上下文上和分池接近，没有把全部表格抄进来。GitHub Releases 本次看到的最新标签仍是 2026-11-02 的 v0.5.23，这篇没有对应的新版本号。

猜测挂靠：推理显存和准入在 B。不是新的对外标价或厂商上架，`business: false`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成推理条目。

## 处置记录

- 2026-11-12：新建，status=open。
