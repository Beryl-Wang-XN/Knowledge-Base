---
# ① 身份
name: Kimi K3.1 Pro
vendor: 月之暗面 Moonshot
version: kimi-k3.1-pro
release_date: 2026-10-23
license: 权重将开放；许可证文本这次没有打开
modality: [文本, 图像]

# ② 技术规格
params: null
architecture: null
context_window: 1M
precision: null

# ③ 能力评估
scores:
  lmarena_elo: null
  reasoning: null
  coding: null
  math: null
  chinese: null
good_at: [编程, 3D 创作, 金融研究, 长上下文]
reputation: "K3.1 系列第一个模型。开放平台写 3 万亿级参数、原生视觉、100 万上下文。精确总参数和激活参数，官方页没有给。"

# ④ 商业属性
pricing:
  input: 13
  output: 68
  cache_write: 13
  cached_input: 1.30
  currency: CNY
  unit: 每百万 token
our_price: null
cost: null
gross_margin: null

# ⑤ 运营属性
supplier: 月之暗面
deploy_mode: API
latency_ttft: null
stability: ""
call_volume: ""

sources:
  - name: Kimi《Introducing Kimi K3.1 Pro》
    url: https://www.kimi.com/en/blog/kimi-k3-1-pro
    tier: 一手
    verified: 2026-11-09
  - name: Kimi 开放平台首页
    url: https://platform.kimi.com/
    tier: 一手
    verified: 2026-11-09
  - name: Kimi Forum 发布帖
    url: https://forum.moonshot.ai/t/kimi-k3-1-pro-has-launched-start-exploring-now/629
    tier: 一手
    verified: 2026-11-09
updated: 2026-11-09
---

## 概述

2026-10-23，月之暗面在官方论坛发帖，介绍 Kimi K3.1 Pro。英文技术博客这次打开时没有显示日期，内容和论坛帖是同一篇发布说明。它是 K3.1 系列的第一个模型，博客写它是迄今能力最强的 3T-class 开源权重模型，上下文 100 万 token，由 Kimi K3 后训练而来，后训练计算明显加大。开放平台首页的中文是「3 万亿级参数」，并写原生支持视觉理解。精确总参数、激活参数，这两页都没有给。

同一天还有高速版 Kimi K3.1 Pro Highspeed。博客写速度是普速版的 2–3 倍。开放平台首页写约为 3 倍。两处都是厂商自己的说法。

当天可用的入口：Kimi.com、Kimi 手机应用、Kimi Work、Kimi Code、Kimi API。API 模型名是 `kimi-k3.1-pro` 和 `kimi-k3.1-pro-highspeed`。博客写 API 客户可以使用 Zero Data Retention。Kimi Enterprise 默认关闭，管理员可以单独打开。完整权重写的是 2026-11-04 前发布。今天是 2026-11-09，权重是否已经放出、用什么许可证，这次没有打开仓库核对，没有准确数据。

火山方舟和腾讯云 TokenHub 的价目在另一条未学的情报里，不写进本档案。

## 已核实的牌价

开放平台首页，2026-11-09 打开，单位是人民币 / 每百万 token：

| 模型 | 输入 | 输出 | 缓存写入 | 缓存命中 |
|---|---:|---:|---:|---:|
| K3.1 Pro | 13.00 | 68.00 | 13.00 | 1.30 |
| K3.1 Pro Highspeed | 26.00 | 136.00 | 26.00 | 1.30 |

首页这一张卡没有把缓存写入拆成 5 分钟和 1 小时两档。1 小时写入价没有准确数据。我方售价、成本和毛利没有准确数据。

## 厂商自己的一项评测

博客脚注写：除非另有说明，结果用推理强度 max、temperature 1.0、top-p 0.95。Terminal-Bench 4.0 用 Claude Code harness，K3.1 Pro 是 65.7%，对照是 GPT-6 Astra 58.2%、Claude Opus 5.5 66.4%。这是月之暗面自己的评测，对照分取自各家博客或官方榜的最高值。不是本库复现的分数，也不写入上面的旗舰价表。

## 选型建议 ★

适合拿来对标长上下文编程和开放权重旗舰的人民币 API 牌价。高速版输入和输出都是普速版的 2 倍，首页说速度约 3 倍，要和真实 TTFT、TPOT 分开看。精确参数量、权重许可证、云渠道价，都还不能填进报价。

## 变更记录

| 日期 | 变更 |
|---|---|
| 2026-11-09 | 建档。牌价来自开放平台首页。不进旗舰对比表。 |
