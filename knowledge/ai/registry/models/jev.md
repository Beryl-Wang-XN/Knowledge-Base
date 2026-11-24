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
call_volume: "无全球调用量。OpenRouter 与 Vercel 的分母不同，见正文 2026-11-09。"

sources:
  - name: TypeSafe《Introducing System One Models & Jev》
    url: https://typesafe.ai/blog/introducing-system-one-models-and-jev
    tier: 一手
    verified: 2026-11-05
  - name: OpenRouter Decision Model Rankings
    url: https://openrouter.ai/rankings/decisions
    tier: 工具站
    verified: 2026-11-09
  - name: OpenRouter LLM Rankings
    url: https://openrouter.ai/rankings
    tier: 工具站
    verified: 2026-11-09
  - name: Vercel《AI Gateway Production Index — October 2026》
    url: https://vercel.com/blog/ai-gateway-production-index-october-2026
    tier: 一手
    verified: 2026-11-09
  - name: Modal《TypeSafe AI scales Jev to trillions of tokens in three days》
    url: https://modal.com/blog/typesafeai-case-study
    tier: 二手
    verified: 2026-11-09
updated: 2026-11-09
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

## 解决什么场景

它接的是工作流里那些又小、又频繁、答案范围事先写得死的判断：分类、路由、打分、抽取，以及决定下一步。TypeSafe 的博文把这写成嵌进普通代码的「带概率的 if」。开放写作、写代码、开放问答不在这个接口里。

Modal 转述的例子是一封客服信：「Stripe 账号连了三天仍失败。」程序同时问部门该交给谁，选项是 billing、technical、sales。示例返回 technical，置信度 0.78，三项概率分别是 0.85、0.15、0。置信度够高，后续代码就建技术单；不够就转人工。这是他们公布的示例返回，不是独立复现。

## 谁发起调用

答案空间由接入方事先写好，终端用户只提供要判断的内容。请求分成两块：现场来的 state，以及开发者写在程序里的问题、类型和可选项。Modal 转述的调用示例就是这个形状。终端用户不会在自己的 prompt 里带上选项。

这和 function calling 的方向相反。function calling 是聊天模型决定要调用某个工具，再由程序执行。Jev 是程序决定这里要做一个有界判断，再把事先定好的答案空间和用户原文一起送进去。模型不决定要不要调用自己。

## 用量口径（2026-11-09）

没有全球调用量，也没有相对全部生成式模型的 token 或花费占比。下面每个数都只在自己的分母里有效。

OpenRouter 决策榜的数据截至 2026-11-08，统计周从 2026-11-02 开始。TypeSafe 占该周决策请求的 **71.1%**，比前一周多 3%。Jev 1.13 为 10.1 亿次，Jev 1.14 为 4.99 亿次。这是决策接口内部的份额，不是全站份额。

同一周的全站文本请求按厂商计，前九名到腾讯的 2.3%，其余厂商合计 9.2%。TypeSafe 没有单独上榜，所以它的全站请求份额低于 2.3%。按 token 计的前十名里没有 Jev；第一是 DeepSeek V4.1 Flash，一周 56 万亿 token。

短上下文这一档也不能再用 9 月的 15.1% 来描述现在。11 月 2 日那一周，Jev 1.13 是 6.36 亿次，Jev 1.14 是 3.42 亿次，仍是点名模型里最多的；其余模型合成 Others，为 20 亿次。

Vercel AI Gateway 的 10 月指数只覆盖到 2026 年 9 月，10 月 15 日公布。Jev 于 9 月 17 日进入网关，头两周触达 35.3% 的付费团队，是该网关历史上最快的；首周试用的团队里 55.6% 在第二周仍使用。9 月请求数是全月最多的模型，token 占当月 1%，花费占 0.15%。头两周的花费占比是 0.27%。

Modal 在 10 月 5 日引 TypeSafe CTO 的话：上线头三天，Modal 为 Jev 送出 1 万亿 token。同文写，上线一周后 Jev 在 OpenRouter 的 1K–10K token 请求里占 15.1%。这是上线当周的数。财富 500 强占比和「每天 1 万亿 token」只见于对《华尔街日报》的转述，这次没有打开原文，不记成已核实。

## 选型建议 ★

- Jev 不是聊天模型，不能拿来替代 GPT-5.6 或 Claude 的文本生成。它对应的是分类、路由、打分、抽取这一类有界决定。
- 和 OpenAI Decisions API 看的是同一类工作：有界问题、带概率、按 input 计费、output 不加 token 费。选型时比的是延迟、价格、概率是否校准，以及输出结构能不能直接进现有代码。两边的加速倍数都先记成对方自己的评测。
- 请求占比高、token 和花费占比低，是这类调用又短又密的结果。不能把决策榜上的 71.1% 当成它在全部生成式流量里的份额。
- 我方售价和成本没有准确数据。early access 还没有写成可直接上架的 SKU。网络结构和 RLCD 的算法这次不写；已排成单独一课。

## 变更记录

| 日期 | 变更（价格/能力/版本） |
|------|----------------------|
| 2026-11-05 | 按 TypeSafe 2026-09-15 博文建档。牌价取他们公布的 $0.042 / 百万 input token，output 免费。速度和成本倍数标成厂商评测。 |
| 2026-11-09 | 追问写回场景、调用方式和用量口径。场景是答案范围事先写死的分类、路由、打分和抽取。调用由程序带着事先写好的答案空间发起。用量只记 OpenRouter、Vercel、Modal 各自的分母，不记全球份额。 |
