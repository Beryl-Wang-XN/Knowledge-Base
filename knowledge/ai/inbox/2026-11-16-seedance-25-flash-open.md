---
title: 火山方舟列出 Seedance 2.5 flash 的模型 ID，并写明已经全面开放
captured: 2026-11-16
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: 火山方舟模型发布公告
    url: https://docs.volcengine.com/docs/ark/model-release-announcement
    tier: 一手
  - name: 火山方舟 Doubao Seedance 2.5 教程
    url: https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
    tier: 一手
  - name: 火山方舟模型价格
    url: https://ark.volcengine.com/region:cn-beijing/docs/model-pricing
    tier: 一手
  - name: 火山方舟创建视频生成任务 API
    url: https://docs.volcengine.com/docs/ark/create-video-generation-task-api
    tier: 一手
---

## 是什么

2026-11-15，火山方舟把 Seedance 2.5 flash 写进了模型发布公告。页上的最近更新时间是 2026.11.15 13:55:01。202611 一节新增一行：`doubao-seedance-2-5-flash-261115`，视频生成模型，版本说明是新发布。说明文字写它支持文生视频、首帧和首尾帧生视频、全模态参考生视频、视频编辑和视频延长，不支持样片模式，支持 480p 和 720p。11 月 14 日那条只记下了「北京时间 2026-11-15 14:00 开放」，当时目录没有这一行，模型 ID 也没对上。

教程的更新时间是 2026-11-15。能力表的 Model ID 一列现在有 `doubao-seedance-2-5-flash-261115`，旁边仍是 Seedance 2.5 的 `doubao-seedance-2-5-260628`。页首写 Doubao-Seedance-2.5-flash 全面开放，并写较 2.5 速度翻倍、价格降低约 34%、最长 30 秒、480P / 720P、最多可参考 10 张图、5 段视频和 5 段音频。能力表里，flash 的参考素材上限是 20（10 张图 + 5 个视频 + 5 个音频），输出时长是 4–30 秒，样片模式一格是不支持；2.5 的参考上限是 50（30 张图 + 10 个视频 + 10 个音频），样片模式是支持。创建视频生成任务的文档更新时间是 2026.11.15 13:55:07，写 Seedance 2.5 和 Seedance 2.5 flash 已全面公开，可以调用 API 和在线体验。

价格页已打开，它自己的更新时间仍是 2026-11-13，早于上面三页。在线推理按 token 计，单位是元 / 百万 tokens，离线推理写暂不支持。`doubao-seedance-2.5-flash` 只按输入是否包含视频区分，输出分辨率写的是 480p 和 720p：输入不含视频 46.00，输入包含视频 28.00。同页 `doubao-seedance-2.5` 在 480p / 720p 是不含视频 70.00、包含视频 42.00，1080p 另有一档；flash 这一行没有 1080p。页上写只对成功生成的视频计费。

价格示例按 token 用量公式估算，条件是 16:9、输出 5 秒。输入不含视频时，flash 的 480p 是 2.21 元 / 个、0.44 元 / 秒，720p 是 4.97 元 / 个、0.99 元 / 秒，1080p 写不支持。同表 2.5 是 480p 3.36 元 / 个、0.67 元 / 秒，720p 7.56 元 / 个、1.51 元 / 秒，1080p 18.71 元 / 个、3.74 元 / 秒。输入包含视频、输出仍是 5 秒时，flash 按输入 2–30 秒给区间：480p 是 2.42–9.42 元 / 个，720p 是 5.44–21.17 元 / 个，最低价对应输入 2–4 秒，最高价对应输入 30 秒，1080p 不支持。

猜测挂靠：新的视频模型 ID 和标价在 G。这是供应商的型号和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。11 月 14 日那条已经记下预定开放时间，这一条只补目录里新出现的模型 ID 和已打开的价格表。

## 处置记录

- 2026-11-16：新建，status=open。
