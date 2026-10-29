---
title: Google 发布 Gemini 4 Carbon（限量预览，含标价）
captured: 2026-10-29
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Introducing Gemini 4 Carbon
    url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
    tier: 一手
  - name: Artificial Analysis《Gemini 4 Carbon is the new #1》
    url: https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
    tier: 工具站
---

## 是什么

2026-10-28，Google 宣布下一档前沿模型 **Gemini 4 Carbon**。官方把它放在两周前的 Gemini 4 Argon 之后，称其强项是网络安全与长程任务，并在编码、智能体、科研、全栈网页和多模态上相对 Argon 有提升。

公开范围还不是开发者、企业和消费者的普遍可用。官方写明：正在参加美国政府的自愿预发布测试；本周起只给一部分网络安全防御方，再经 Fairwind Program 逐步放到更多受信任伙伴。Artificial Analysis 同日也写：和 Argon 发布时一样，Carbon 仍在向选定用户铺开，尚未公开可用。

价格（均已打开上述原文）：

- Google：入门价与 Argon 相同，输入 **$2** / 百万 token，输出 **$10** / 百万 token；缓存输入相对输入价打 95% 折。入门期结束后为输入 **$4**、输出 **$20** / 百万 token。原文没有写明入门期截止日期。
- Artificial Analysis：按标准价 **$4 / $20** 作图，并称有 50% 发布折扣、结束日未确认；标准价下缓存输入为 **$0.20** / 百万 token。其图表不用入门价。

能力口径（只记原文中的结果，不展开攻防做法）：

- Google：Artificial Analysis Intelligence Index v5.0 排名第 1，分数 **59**。SEC-bench Pro **88.2%**，ExploitGym **54.8%**，CWE-bench **71.0%**。WebDev Arena **+89 Elo**，第 4，**1768**。内部基准上，生成安全代码的成功率相对 Argon 超过 2 倍。
- Artificial Analysis（high reasoning）：Intelligence Index v5 为 **59**，并在 9 项里的 4 项领先（HLE-Diamond、Terminal-Bench-Science、AA-Omniscience、AutomationBench-AA）。用 Antigravity CLI 时，Coding Agent Index 为 **59**，比 Claude Code + Claude Opus 5.5（max，**62**）低 3 分。标准价下每次 Intelligence Index 任务成本 **$7.76**，低于该文所写的 Opus 5.5（max，**$10.04**），高于 GPT-6 Astra（max，**$6.25**）。上下文 **1M** token；输入为文本、图像、视频、语音，输出为文本。

该文里 Terminal-Bench 4.0 与 FrontierCode 的对照句前后数字对不上，这里不抄。API 模型 ID 本次没在定价页单独核对，标 **待核实**。

猜测挂靠：模型档案在 G。对标友商且有标价，`business: true`。若回顾后重点是限量发布或缓存折扣，再决定是否同时看 F 或 E。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型档案，也不改 `registry/`。

## 处置记录

- 2026-10-29：新建，status=open。
