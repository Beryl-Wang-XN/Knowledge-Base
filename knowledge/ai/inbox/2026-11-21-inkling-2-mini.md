---
title: Thinking Machines 发布开源权重 Inkling 2 Mini
captured: 2026-11-21
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Thinking Machines 公告
    url: https://thinkingmachines.ai/news/inkling-2-mini/
    tier: 一手
  - name: Inkling 2 Mini 模型卡
    url: https://thinkingmachines.ai/model-card/inkling-2-mini/
    tier: 一手
  - name: Artificial Analysis 文章
    url: https://artificialanalysis.ai/articles/inkling-2-mini
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

Thinking Machines 在 2026-11-20 发布 Inkling 2 Mini，并同时放出研究用的可变循环模型。公告写它是循环 transformer：中间层对每个 token 跑三遍，用更少的输出 token 做推理。模型卡写发布日是 2026-11-20，许可证 Apache 2.0，输入是文本和图像，输出是文本，上下文最长 1M token。

参数两边都写了，口径不完全一样。公告写总参数 26.4B、激活 3.4B，算上循环后每个 token 的权值激活是 5.4B；对照表的激活/总参数一行写成 5.4/26.4。模型卡写 26.4B、激活 3.4B，并注明每多一轮循环大约增加 1.0B 有效激活参数，三轮下来每个 token 的有效激活参数是 5.4B。架构是 24 层，中间 12 层共享权重跑三遍，相当于 24 层权重做 48 次层计算；每层把 token 路由到 128 个专家里的 8 个。大部分权重是 NVFP4，最后四层是 MXFP8。公告写内存占用大约 20GB，可在笔记本上本地跑。Artificial Analysis 同日文章写成总参数 26B、激活 5.4B（含三轮循环），每个文本 token 使用 3.1B 不重复权重。3.1B 和模型卡的 3.4B 对不上，这次不改写成一个数。

Artificial Analysis changelog 和文章都写 Intelligence Index 为 20。公告自己的对照表把 AA Index（v5.0）写成 20.1。两边没有对齐。文章还写它在 Intelligence Index 上与 Qwen3.8 27B（xhigh）和 Nanbeige4.3-33B 打平，激活参数大约少 5 倍和 6 倍；同一分数下输出 token 大约比 Qwen3.8 27B 多 38%，计算量大约少 2.8 倍。公告开头给出的自测分数包括 DeepSWE v1.1 的 48.2% 和 Vals Index v2.2 的 46.5%。长对照表留在公告原文。

推理和微调写在 Tinker 上，对话在 Tinker Playground。开源推理写到 SGLang、vLLM、Ollama、Unsloth、NVIDIA Dynamo、TokenSpeed 和 Llama App。权重在 Hugging Face。Artificial Analysis 文章把首方标价写成每百万 token 输入 $0.15、输出 $0.50、缓存命中 $0.015，并据此写成每项 Intelligence Index 任务 $0.59、9.0 分钟，对照 Qwen3.8 27B 为 $3.53 和 38.2 分钟。公告和模型卡没有这组单价，Tinker 定价页这次没有打开，标价待核实。

猜测挂靠：新的开源权重模型和榜单分数在 G。这是厂商型号和价格信号，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-21：新建，status=open。
