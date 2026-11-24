---
title: Claude 组织 webhook 增加客户自有存储的失败和恢复事件
captured: 2026-11-24
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
---

## 是什么

Claude Platform 发布说明的 2026-11-23 节另写：组织 webhook 增加两种事件，仍是 beta。用作客户自有存储的桶没通过每日检查时发送 `external_storage.failed`，再次通过时发送 `external_storage.recovered`。

这和已记的 `external_key.failed` / `external_key.recovered` 不是同一对事件。那一对写在 2026-11-16 节，针对密钥管理服务拒绝客户自管加密密钥。这一对写在 11 月 23 日，针对客户自有存储桶的每日检查。

发布说明只写出事件名和触发条件。载荷、重试，以及「每日检查」失败几次才发送，这次没有另开文档。没有单独标价。同日的 Enterprise Frontier Safeguards 另记一条。

猜测挂靠：供应商平台的事件通知在 F。这是友商接口变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改已有的密钥 webhook 条目。

## 处置记录

- 2026-11-24：新建，status=open。
