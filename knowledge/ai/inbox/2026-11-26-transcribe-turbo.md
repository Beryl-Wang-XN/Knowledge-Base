---
title: Amazon Transcribe Turbo 进入公开预览
captured: 2026-11-26
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Amazon Transcribe Turbo public preview
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/transcribe-turbo-preview/
    tier: 一手
---

## 是什么

AWS What's New 写于 2026-11-25：Amazon Transcribe Turbo 是下一代语音转文字模型，在 US East（Ohio）对批量转写和流式转写公开预览。它提高准确率，支持自定义词表，并按各语言区域的习惯格式化数字、日期、货币、电话号码和地址。

流式支持英语、葡萄牙语、法语、意大利语、德语和西班牙语。相对当前生产模型，英语词错误率大约低 14%，其余这些语言大约低 11%，格式化准确率提高 20 分以上。批量转写的英语 Turbo 已在大多数 AWS 区域一般可用；葡萄牙语、法语、意大利语、德语、西班牙语、中文、日语、韩语和阿拉伯语进入预览，词错误率大约低 16%。基础模型不需要改 API、代码或 SDK。

流式还为语音智能体加了两项能力，上线时是英语，其余语言写到 2026 年 12 月底。语义话轮判断看说了什么和韵律，不只看静音。帖子写响应大约 615 毫秒，打断率 5%，并且可以调节。运行时 ASR 提示在每一轮送入菜单选项、预期名称和预期实体类型。帖子写，在英语客服数据上，菜单路由准确率从 87% 升到 97%。这两项不另收费。打开方式是打开 `EndOfTurnDetection`，并在 `ConfigureEvent` 里发送提示。基础转写的单价这次没有打开定价页，标 **待核实**。

猜测挂靠：模型身份在 G。这是云厂商的新语音模型，并写明两项能力不另收费，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-26：新建，status=open。
