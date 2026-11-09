---
title: Claude Enterprise 可用项目标签按费用代码看花费（beta）
captured: 2026-11-07
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: Claude 帮助中心发布说明
    url: https://support.claude.com/en/articles/12138966-release-notes
    tier: 一手
  - name: Track spend by cost code with project tags
    url: https://support.claude.com/en/articles/18251257-track-spend-by-cost-code-with-project-tags
    tier: 一手
---

## 是什么

Claude 帮助中心发布说明的日期是 2026-11-06。符合条件的 Enterprise 组织可以给项目打上已有的费用代码（如 charge code、WBS code 或 client-matter number），并按标签查看这些项目里的大部分花费。功能在 beta。

帮助中心文章里已打开核对的边界：

- 不适用于开启了 HIPAA、客户自管密钥（CMEK）、零数据保留（含 Claude Code 的 ZDR）、最短数据保留、数据存放在美国以外，或把 Claude Desktop 接到自有模型供应商的组织。
- 标签只覆盖项目内的工作。Claude API、Claude Console，以及经 Bedrock、Vertex、gateway 或 API key 使用的 Claude Code，都不在范围内。每个项目最多 16 个标签，每个标签一个值，花费不能拆到同一标签的两个值上。
- 标签大约两小时后才开始计入花费，更早的花费不回溯。金额是折扣后、抵扣额度前，可能和发票不一致；坐席覆盖的用量不计。
- Admin API 与花费报表 API 都在 beta。文章给出的 beta header 分别是 `ce-project-tags-2026-10-09` 和 `analytics-usage-cost-2026-08-24`。金额单位写的是美分，可以有不足一美分的小数。

猜测挂靠：E（Token 计量与按项目归集花费）。这是友商的企业计费能力，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成计费条目，也不改学习计划。

## 处置记录

- 2026-11-07：新建，status=open。
