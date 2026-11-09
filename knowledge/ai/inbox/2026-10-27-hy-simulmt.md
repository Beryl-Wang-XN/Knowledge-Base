---
title: 腾讯混元开源同声传译模型 Hy-SimulMT
captured: 2026-10-27
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Hy-SimulMT 仓库说明（简体中文）
    url: https://github.com/Tencent-Hunyuan/Hy-SimulMT/blob/main/README.zh-CN.md
    tier: 一手
  - name: Hugging Face 模型集合 tencent/hy-simulmt
    url: https://huggingface.co/collections/tencent/hy-simulmt
    tier: 一手
  - name: 混元开源模型页（仓库引用地址）
    url: https://hy.tencent.com/model/open-source-model/detail?id=hy-simulmt
    tier: 一手
---

## 是什么

腾讯混元仓库的新闻写明 **2026.10.26** 发布 **Hy-SimulMT**：中英双向、语音到语音的实时同声传译，边听边出译文文字和语音，并支持实时音色克隆。语音输出和音色克隆需要另配 TTS。产品体验在 Hy 翻译 App。

仓库列出的权重名是 30B-A3B 系列：只出译文，以及原文和译文一起出的 Interleave；两者都有 FP8 与 GGUF。配套推理服务叫 SimulInfer，训练工具叫 SimulTrain。说明书写：已有环境需要 vLLM ≥ 0.31，且支持 `HYV3ForCausalLM`。llama.cpp 适配当时还没进官方仓库。

延迟和质量是仓库自己的评测，不是独立榜单。RealSI 长音频上，他们写 StreamLAAL 约为 3 秒，并注明 StreamLAAL 不是首次开口延迟；GEMBA 高于所对比的开源模型，且超过五个商业 API 里的四个。短音频表（FLEURS、CoVoST2、ACL6060、RealSI-Sentence）在同一篇说明里，本次不把整表抄进知识库。另有一组 2026 年 9 月以后的 18 段、每段约 6 分钟的音频，对照六位持证译员；仓库称这次小样本里质量达到人类同传专家水平、时延往往更低，并写明不外推到音质或音色相似度。

猜测挂靠：G。若回顾时重点变成流式语音的时延和 vLLM 接法，再决定要不要改挂 B。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写入模型档案，也不把部署步骤写成知识条目。

## 处置记录

- 2026-10-27：新建，status=open。
