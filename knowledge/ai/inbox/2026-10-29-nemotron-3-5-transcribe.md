---
title: NVIDIA 开源 Nemotron 3.5 Transcribe 语音模型
captured: 2026-10-29
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: NVIDIA Hugging Face 博文 Nemotron 3.5 Transcribe and Granary v2
    url: https://huggingface.co/blog/nvidia/nemotron-transcribe-granary
    tier: 一手
  - name: Hugging Face 模型卡 NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
    url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
    tier: 一手
  - name: NVIDIA 研究页 Nemotron 3.5 Transcribe
    url: https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/
    tier: 一手
---

## 是什么

2026-10-28，NVIDIA 发布开源权重语音模型 **Nemotron 3.5 Transcribe**（模型卡 ID：`nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B`）。模型卡写明发布日为 Build.Nvidia.com、GitHub（NeMo Speech）、Hugging Face、NGC 均为 2026-10-28。许可证 **OpenMDW-1.1**，可用于商业或非商业用途。面向录好的音频，不是实时流式。

模型卡中的规格：总参数 **34B**，含音频编码器在内激活约 **4.3B**；架构是 Mamba-2–Transformer 混合 MoE，加上并行的语音编码器和说话人编码器。精度有 BF16，以及 FP8、NVFP4。上下文 **65,536** token，录音最长 1 小时。输入为音频和文本，输出为文本，可选词级时间戳。部署示例为 1 张 H100 80GB。支持原生多 token 预测的投机解码。思考开关由 chat template 控制。

语言和任务：模型卡写 40 种语言，任务包括逐字或书面转写、带上下文的转写、说话人转写、语音翻译、语种识别和音频问答。NVIDIA 博文进一步写：40 种语言转写，其中 31 种可与英语互译，13 种做说话人归属，最多 8 个说话人。音频问答按博文是用英语训练的。博文称量化版本即将推出，本地的 NeMo-Speech.cpp 也即将推出；当天可用 vLLM 与 SGLang-Omni 自托管。托管端点写了 Baseten、DeepInfra、Simplismart。各端点的价格标 **待核实**。

同日配套数据 **Granary v2**：博文写公开 manifest 覆盖 **463,062** 小时、48 种语言、16 个来源语料，并说明这是数据集规模，不是 Transcribe 的完整训练配比。

榜单数字只记两边对得上的，对不上的标待核实：

- 模型卡与博文一致：多语 Open ASR（7 种语言）平均 WER **4.62**；长音频平均 WER **10.98**。
- 英文 WER 不一致：模型卡对 9 个公开集写平均 WER **4.71**；博文对英文 Open ASR 榜写平均 WER **5.33**（并注明不含 API 模型）。标 **待核实**，先不要入库。
- 博文转述 Artificial Analysis 语音榜 AA-WER **2.8%**、以及 David AI / VoiceArena 的名次。本次没有打开这些榜的原页，标 **待核实**。

猜测挂靠：模型档案在 G。NVIDIA 是供应商，且已有第三方托管端点，`business: true`。若回顾后重点是语音推理的吞吐或投机解码，再决定是否另挂 B。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型档案，也不改 `registry/`。

## 处置记录

- 2026-10-29：新建，status=open。
