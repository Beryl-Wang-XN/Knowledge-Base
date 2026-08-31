---
# ① 身份
name: 模型名称                  # 如 DeepSeek-V3
vendor: 厂商                    # 如 DeepSeek
version: 版本
release_date: 2024-12
license: 开源/闭源              # 如 开源(MIT) / 闭源
modality: [文本]                # 文本 / 多模态(图/音/视频)

# ② 技术规格
params: 671B (MoE, 37B激活)     # 参数量（含激活量）
architecture: MoE               # 稠密 Dense / MoE
context_window: 128K
precision: FP8                  # 训练/推理精度

# ③ 能力评估（分维度，null=待联网核实，绝不凭记忆瞎填）
scores:
  lmarena_elo: null
  reasoning: null
  coding: null
  math: null
  chinese: null
good_at: []                     # 擅长场景
reputation: ""                  # 口碑一句话

# ④ 商业属性（价格务必联网核实）
pricing:
  input: null                   # 每百万 token
  output: null
  currency: USD
our_price: null                 # 我方售价
cost: null                      # 我方成本
gross_margin: null              # 毛利

# ⑤ 运营属性
supplier: ""                    # 供应商
deploy_mode: ""                 # 自部署 / API转售
latency_ttft: null              # 首 token 延迟
stability: ""
call_volume: ""                 # 调用量级

# 扩展维度（按需启用，步骤4待确认）
# license_terms: ""             # 合规/授权条款
# rate_limit: ""                # 限流配额
# api_compat: ""                # API 兼容性（是否兼容 OpenAI 格式）

# 元数据
sources: []                     # 数据来源链接
updated: 2026-09-01
---

## 概述

（这个模型是什么、定位、适合什么场景）

## 选型建议 ★

（在我们平台上，什么场景推荐它、对标哪个模型、竞争位置——业务回流点）

## 变更记录

| 日期 | 变更（价格/能力/版本） |
|------|----------------------|
| 2026-09-01 | 建档 |
