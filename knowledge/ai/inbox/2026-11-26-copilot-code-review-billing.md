---
title: Copilot 代码评审未设置时将默认向组织计费
captured: 2026-11-26
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: GitHub Changelog
    url: https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization/
    tier: 一手
---

## 是什么

GitHub Changelog 写于 2026-11-25。还没选定 Copilot 代码评审怎么计费时，从 2026-12-30 起，持有 Copilot 许可证的成员所做的评审改向仓库所属组织计费。要维持现在的计费，需在那之前选 Member。适用范围是有 Copilot Business 或 Copilot Enterprise 的组织与企业。

现在如果没有保存选择，持有付费 Copilot 许可证的成员做评审，用的是成员自己的 Copilot 额度。2026-12-30 起，这些评审改向组织计费。没有打开 AI Credits 付费用量、有计费锁定，或没有可计费客户的账户，会改成 Member。已经选过 Member 或 Organization 的保持原选择。没有 Copilot 许可证的成员那一项设置不变。

在默认改掉之前，未设置的选项显示为 Default (Member)，并带这次变更的提示。企业若接管这项设置，由企业所有者选择。向组织计费需要打开 AI Credits 付费用量，并可能增加组织花费。具体单价这次没有打开，标 **待核实**。

猜测挂靠：计费归属在 E。这是友商产品的计费规则变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-26：新建，status=open。
