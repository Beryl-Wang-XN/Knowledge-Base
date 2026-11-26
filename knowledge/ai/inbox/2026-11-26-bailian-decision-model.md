---
title: 百炼上架决策模型正式版 decision-model
captured: 2026-11-26
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
  - name: Model releases and updates
    url: https://help.aliyun.com/en/model-studio/newly-released-models
    tier: 一手
  - name: 决策模型 System One API
    url: https://help.aliyun.com/zh/model-studio/decision-model-api
    tier: 一手
  - name: 阿里云百炼模型价格
    url: https://help.aliyun.com/zh/model-studio/model-pricing
    tier: 一手
---

## 是什么

百炼中文和英文上架页的 2026 年一节都把 `decision-model` 写在 2026-11-25。上架说明写它是面向高频业务判断的结构化决策模型，可根据文本、图片或业务状态并行完成分类、是非判断与评分，并返回概率分布和置信度。靠后单独成节的国际 2026 年列表没有 2026-11-25 的这一行，国际决策模型仍停在 2026-09-24。

API 页写正式版的模型名是 `decision-model`，`decision-model-preview` 仍是预览版。调用走 `POST /compatible-mode/v1/systemone`。华北 2（北京）的地址是 `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/systemone`，新加坡是 `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/systemone`。一次请求带业务 `state` 和若干问题，类型是 `choice`、`noul`、`score`。问题数上限 16。`choice` 选项不超过 255。`score` 等级为 2 到 255。上下文上限 65,536 token。接口不生成文本，页上写延迟和成本与输出长度无关。返回里 `noul` 是 P(yes)，`score` 是等级索引的概率加权期望。

价格页写决策模型按输入 token 计费。华北 2（北京）的 `decision-model` 输入是 0.3 元 / 百万 token，免费额度 100 万 token；同页写免费额度自开通百炼、模型发布或申请通过之日起 90 天内，以较晚者为准。新加坡输入是 0.306 元 / 百万 token，无免费额度。同一张表里 `decision-model-preview` 两地都仍是限时免费。正式版模型信息页这次打开是 404，RPM 和 TPM 标 **待核实**。上架说明写了图片；这次打开的 API 参数说明把 `state` 写成工单文本、对话或结构化对象，图片怎么传标 **待核实**。

猜测挂靠：模型身份和标价在 G。这是供应商的新模型和目录价，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-26：新建，status=open。
