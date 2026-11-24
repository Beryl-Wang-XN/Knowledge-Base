---
title: LingSante-3.1-flash 的 MXFP4 量化权重上线
captured: 2026-11-23
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: LingSante-3.1-flash-MXFP4 模型卡
    url: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4
    tier: 一手
  - name: LingSante-3.1-flash 模型卡
    url: https://huggingface.co/inclusionAI/LingSante-3.1-flash
    tier: 一手
  - name: Hugging Face 模型接口
    url: https://huggingface.co/api/models/inclusionAI/LingSante-3.1-flash-MXFP4
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

Hugging Face 接口写，`inclusionAI/LingSante-3.1-flash-MXFP4` 的 `createdAt` 是 2026-11-22T03:19:38Z，许可证 MIT。这是本窗口里新出现的仓库。源模型仓库 `inclusionAI/LingSante-3.1-flash` 的 `createdAt` 是 2026-11-19T04:30:30Z，落在更早的窗口，这次不把源权重补记成当天发布；该仓库 `lastModified` 是 2026-11-22T17:58:08Z。没有打开到厂商博客或新闻稿。

MXFP4 模型卡写，这是 LingSante-3.1-flash 的训练后量化，算法是 Round-to-Nearest，没有校准，也没有额外训练。主模型大约 560B 参数、每 token 大约激活 25B，配置的上下文是 262,144。检查点全部文件 291.72 GiB。路由专家的 `gate_proj`、`up_proj`、`down_proj` 用 MXFP4；稠密 MLP、共享专家、KDA 和注意力矩阵保留 FP8；嵌入、`lm_head`、路由权重等保留 BF16。服务时专家激活可选 Humming 的 W4A8 或 W4A16。推荐部署是 4 张 NVIDIA H20-3e，TP4 / EP4 / DP1。模型卡写它用于研究和评估，不是医疗器械，不能单独作为诊断、处方或治疗依据。量化可能改变生成文本、推理、工具选择和停止行为。

源模型卡写的是总参数 560B、每 token 激活 25B、上下文 1M。两张卡的上下文数字没有对齐。MXFP4 卡上的基准图注明是源模型的成绩，不是量化检查点的测量；图里的具体分数这次没有抄。源模型卡正文写，医疗专业行为基准上排在开源模型里的第二，只在 GPT-6 Astra 之后，没有给出那个名次对应的数字。

Artificial Analysis changelog 的 22 Nov 2026 把 LingSante-3.1-flash 列在新的语言模型评估结果里。这次打开的更新日志没有写出它的 Intelligence Index。没有标价；源模型卡上的 Computrix API 链接这次没有打开。

猜测挂靠：模型身份和规格在 G。这是新的开源权重，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。11 月 19 日创建的源权重不在今天补写。

## 处置记录

- 2026-11-23：新建，status=open。
