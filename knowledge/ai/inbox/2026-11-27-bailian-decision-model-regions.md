---
title: 百炼决策模型扩到弗吉尼亚、法兰克福、东京和香港
captured: 2026-11-27
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
  - name: 决策模型 System One API
    url: https://help.aliyun.com/zh/model-studio/decision-model-api
    tier: 一手
  - name: 阿里云百炼模型价格
    url: https://help.aliyun.com/zh/model-studio/model-pricing
    tier: 一手
  - name: 阿里云国际站模型价格
    url: https://www.alibabacloud.com/help/zh/model-studio/model-pricing
    tier: 一手
---

## 是什么

百炼中文上架页把 `decision-model` 写进四个地域的 2026-11-26。美国（弗吉尼亚）、德国（法兰克福）、日本（东京）和中国香港各自的 2026 年列表，第一条都是这个模型，说明仍是面向高频业务判断的结构化决策模型。华北 2（北京）和新加坡的上架日期仍是 2026-11-25，已在 11 月 26 日那条里，不并进去。这四个新地域的条目没有另写「服务部署范围」一行。

API 页的请求地址表现在有这四个地域，模型名旁边写的是正式版 `decision-model`。地址分别是 `https://{WorkspaceId}.us-east-1.maas.aliyuncs.com/compatible-mode/v1/systemone`、`https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1/systemone`、`https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1/systemone` 和 `https://{WorkspaceId}.cn-hongkong.maas.aliyuncs.com/compatible-mode/v1/systemone`。同一页的模型参数仍列出正式版和 `decision-model-preview`。价格页里这四个地域只有 `decision-model`，没有预览版那一行。

中文价格页按输入 token 计费。弗吉尼亚、法兰克福、东京和香港的 `decision-model` 都是 0.3 元 / 百万 token，无免费额度。国际站价格页这四地都写成 $0.042 / 百万 token，同样无免费额度。RPM 和 TPM 这次没有另开模型信息页，标 **待核实**。

同一份 API 页把正式版的可选参数 `image` 写成单图输入。11 月 26 日那条打开时，参数说明还没有写清图片怎么传。

猜测挂靠：新地域的模型身份和目录价在 G。这是供应商的部署和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-27：新建，status=open。
