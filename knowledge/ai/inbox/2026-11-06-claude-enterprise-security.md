---
title: Claude Enterprise 安全中心、自助 IP allowlist 与成员签出
captured: 2026-11-06
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Claude 产品更新与文章 More visibility and control over Claude Enterprise
    url: https://claude.com/resources/articles/claude-enterprise-security-updates
    tier: 一手
  - name: Claude 帮助中心 Release notes
    url: https://support.claude.com/en/articles/12138966-release-notes
    tier: 一手
  - name: Claude Platform release notes
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
---

## 是什么

2026-11-05，Claude 帮助中心和产品更新列出 Enterprise 的安全与管理功能。文章描述的是同一批控制，不是新模型，也没有新标价。

文章写明：安全中心在 Organization settings，把聊天、Cowork、Claude Code 的设置和 Anthropic 推荐配置对照，可下载报告；它是建议，不是认证。安全中心为 beta。有 Compliance API 的组织可以读同一份检查结果。

Inference hooks 在这篇文章里写成一般可用，分 prompt hooks 和 pre-tool-call hooks，把提示和工具调用交给客户已有的安全工具检查。平台发布说明在 2026-10-20 已经写过 inference hooks 退出 beta，所以这次不把它记成第二次发布，只记下 11-05 文章的公开说明。

集中管理为 beta：父组织在 admin.claude.com 有独立控制台，统一管 SSO、SCIM、域名验证、组和 Compliance API key。可以接多个身份提供商。父角色默认不能进入下级组织，但父级创建的 Compliance API key 可以跨组织读取。设置完成后不能撤销。

访问控制：平台发布说明写，Admin API `POST /v1/organizations/users/{user_id}/sign_out` 为 beta，请求要带 `admin-user-sign-out-2026-10-08`。它结束该成员在各浏览器和设备上的登录会话、受信任设备，以及该组织的 OAuth token；成员仍留在组织里，可以马上再登录。文章补充：它不结束 API key、已经在跑的云会话和已排程的例程。

IP allowlist 改为管理员自助，beta。平台发布说明写，每个组织最多 1,000 条 IPv4、IPv6 或 CIDR；不在名单上的地址访问被覆盖的服务会被拒绝。具体覆盖哪些服务，发布说明指向 IP allowlisting 文档，本次没有逐项打开，覆盖范围待核实。文章还写了可在受管电脑的 Claude Desktop 上拦截个人和其他外部账号。

文章把 Cowork 虚拟机里的 EDR 传感器写成 recently announced，本次不把它的首发日当成 11-05。帮助中心同日还有 Personal Finance，那是美国 Pro / Max / Ultra 的消费端账户连接，不是模型、价格或推理服务变更，不另开一条。

猜测挂靠：友商的企业准入与管理控制，F。`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成竞品条目。

## 处置记录

- 2026-11-06：新建，status=open。
