---
title: NVIDIA 公开 Nemotron 3.5 Parse 的合成数据和 DFlash2
captured: 2026-11-27
from: intel
module: B
business: true
status: open
review_after:
entry:
sources:
  - name: Building on Nemotron 3.5 Parse
    url: https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin
    tier: 一手
---

## 是什么

NVIDIA 在 Hugging Face 的博客写于 2026-11-26。帖子说 Nemotron 3.5 Parse 是已经发布的小型文档模型，这次补上三份训练用合成数据、一份微调配方，以及可选的 DFlash2 投机解码。帖子没有目录价。

三份数据是 Synthetic Charts V1（9.98M 条）、Synthetic Tables V1（1M 条）和 OCR Synthetic Multilingual v2（7.9M 条）。每份包含图像、标注、生成说明和训练格式。

帖子把 Parse 3.5 相对 Parse 2.0 的结构写成：页面预处理从固定 2048×1664 画布改成 NaViT 动态矩形输入；图像到文本从编码器—解码器交叉注意力改成压缩视觉 token 的因果前缀；解码器自注意力改成 GQA-8，16 个 query head、8 个 key/value head。内置多 token 预测头做一字前瞻。DFlash2 由小草稿模型一次提议最多 32 个 token，Parse 一起验证。文中测到的 32 token 配置里，平均接受大约 14 个草稿 token，加上目标 token 后每步大约前进 15 个输出 token。

单卡 H200、BF16、同一批 2,078 页的单次解析里，相对关掉投机解码的 Parse 3.5，DFlash2 在并发 1 时吞吐提高 7.62 倍，并发 512 时提高 1.52 倍。并发 512 时，Parse 3.5 无投机解码是 13.48 页/秒，加上 DFlash2 是 20.44 页/秒，Parse 2.0 是 2.98 页/秒。相对 Parse 2.0，这两个数字分别是 4.53 倍和 6.86 倍。图注写 Parse 2.0 每个点一次试验，Parse 3.5 是三次试验的中位数。

双遍和三遍重解析相对单遍，在已发表的参考评测里分别多 2.18 和 2.46 个 ParseBench 分。SFT 对照 GRPO 的分数来自开发检查点，帖子写明不是最终发布的模型：循环标记从 126 页降到 29 页，触到 9,000 token 上限的输出从 185 降到 35，总分从 66.24 到 71.38。牙科表格配方的 pass@1 从基座 0.00% 到 SFT 后 95.85%，再到 RLVR 后 96.58%。微调配方用 NeMo Automodel 做 SFT、NeMo RL 做 GRPO，并用 vLLM 生成候选答案。

猜测挂靠：投机解码和页面吞吐在 B。这是供应商放出的推理加速，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-27：新建，status=open。
