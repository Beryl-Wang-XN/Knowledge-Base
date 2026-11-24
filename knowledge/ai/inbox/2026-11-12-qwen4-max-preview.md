---
title: 百炼上架 Qwen4-Max-Preview，仅 Token Plan，预览到 11 月 25 日
captured: 2026-11-12
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: 阿里云百炼模型上架与更新
    url: https://help.aliyun.com/zh/model-studio/newly-released-models
    tier: 一手
  - name: 百炼 qwen4-max-preview 模型页
    url: https://help.aliyun.com/zh/model-studio/qwen4-max-preview
    tier: 一手
  - name: 百炼 Token Plan 个人版
    url: https://help.aliyun.com/zh/model-studio/token-plan-personal-overview
    tier: 一手
  - name: 百炼 Token Plan 团队版
    url: https://help.aliyun.com/zh/model-studio/token-plan-team-overview
    tier: 一手
---

## 是什么

百炼「模型上架与更新」靠前的 2026 年一节把 `qwen4-max-preview` 写在 2026-11-11。模型页写它是通义千问新一代旗舰多模态预览：文本生成、图片和视频理解、默认开启思考，并支持联网搜索、工具调用、JSON Object / JSON Schema。兼容 OpenAI Chat Completions、Responses 和 Anthropic Messages。上下文 1M token。最大输出 393,216 token，思考和最终回答共用这一档。`reasoning_effort` 可选 `low`、`medium` 或默认的 `xhigh`，不能和 `thinking_budget` 同时设。自这个模型起，Chat Completions 的 `max_tokens` 与 `max_completion_tokens` 等价，都限制思考加回答的总量。

接入只走 Token Plan，模型页写明不支持按量计费，所以没有打开到一份按百万 token 的目录价。个人版和团队版都写仅华北 2（北京），Base URL 是 `https://token-plan.cn-beijing.maas.aliyuncs.com`。别名 `qwen4.0-max-preview`，两个 ID 都能调，账单统一显示别名。预览期是北京时间 2026-11-11 10:00 到 2026-11-25 24:00，页上写期间不做变更，预览结束后下线。个人版和团队版都写：限时活动 Credits 低至 2 折（相当于 5 倍用量），每晚 22:00 到次日 08:00 再享 4 折，即原标准的 0.8 折。按量标价没有，标价以外的单次 Credits 仍写以控制台为准。

上架页后面单独标成「国际」的 2026 年一节，最新仍是 2026-11-05 的 `kimi-k3.1-pro`，没有 `qwen4-max-preview`。

猜测挂靠：模型档案在 G。新模型和套餐抵扣是对标友商与价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-12：新建，status=open。
