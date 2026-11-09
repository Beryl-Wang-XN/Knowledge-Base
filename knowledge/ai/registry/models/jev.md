---
# ① 身份
name: Jev
vendor: TypeSafe
version: early access
release_date: 2026-09-15
license: 闭源
modality: [文本]

# ② 技术规格
params: null
architecture: null
context_window: null
precision: null

# ③ 能力评估
scores:
  lmarena_elo: null
  reasoning: null
  coding: null
  math: null
  chinese: null
good_at: [分类, 路由, 打分, 抽取, 有界决策]
reputation: "TypeSafe 自称的第一款 System One 模型。不生成文本，输出事先规定好结构的概率决定。"

# ④ 商业属性
pricing:
  input: 0.042
  output: 0
  currency: USD
  unit: 每百万 input token
our_price: null
cost: null
gross_margin: null

# ⑤ 运营属性
supplier: TypeSafe
deploy_mode: API
latency_ttft: null
stability: ""
call_volume: ""

sources:
  - name: TypeSafe《Introducing System One Models & Jev》
    url: https://typesafe.ai/blog/introducing-system-one-models-and-jev
    tier: 一手
    verified: 2026-11-05
updated: 2026-11-05
---

## 概述

2026-09-15，TypeSafe 创始人 Diogo Almeida 在官方博文里发布第一款 System One 模型 **Jev**，当时是 early access。博文把它写成给软件直接调用的决策函数：非结构化状态进去，带类型的概率决定出来。它不生成字符串。可选输出和结构要事先定好，博文称因此不会产生类型错误。每次输出都带校准过的概率和置信度。采样是并行的，一次查询给出全部输出，不是一个 token 一个 token往外吐。

训练方法是他们自己命名的 Reinforcement Learning for Calibrated Decisions（RLCD）。名字来自 Kahneman 的 System 1，以及经济学家 William Stanley Jevons。博文写，Jev 的选择基数上限是 255；更高基数要先独立打分，再做一次显式选择。

## 已核实的产品口径

以下都来自同一篇博文，是 TypeSafe 自己的说法，不是独立复现。

- 公布牌价：input **$0.042 / 百万 token**（他们也写成每十亿 token 42 美元）。output 标成免费。他们同时写明，现在还不能证明这个价格没有补贴。
- 他们给出的端到端响应时间是 **70–500 毫秒**。相对前沿模型「同样的 System One 查询」快 **40–200 倍**，是他们的对比口径。
- 主页上的 **193.6 倍更快、444.6 倍更便宜**来自他们自己的 workflow eval。参照答案是 GPT-6 Astra 和 Fable 5.1 的平均。博文写，这偏他们口径的高位，工作流由他们的能力团队制作，可能有偏差，而且这个参照会偏向 OpenAI 和 Anthropic。
- 公开榜单分数、参数量、上下文长度，这篇没有给。档案里这些字段是没有准确数据。

## 选型建议 ★

- Jev 不是聊天模型，不能拿来替代 GPT-5.6 或 Claude 的文本生成。它对应的是分类、路由、打分、抽取这一类有界决定。
- 和 OpenAI Decisions API 看的是同一类工作：有界问题、带概率、按 input 计费、output 不加 token 费。选型时比的是延迟、价格、概率是否校准，以及输出结构能不能直接进现有代码。两边的加速倍数都先记成对方自己的评测。
- 我方售价、成本和调用量没有准确数据。early access 还没有写成可直接上架的 SKU。

## 变更记录

| 日期 | 变更（价格/能力/版本） |
|------|----------------------|
| 2026-11-05 | 按 TypeSafe 2026-09-15 博文建档。牌价取他们公布的 $0.042 / 百万 input token，output 免费。速度和成本倍数标成厂商评测。 |
