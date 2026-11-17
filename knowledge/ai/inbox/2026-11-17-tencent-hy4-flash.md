---
title: 腾讯云 TokenHub 上架 Hy4 flash，并给出限时五折
captured: 2026-11-17
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: 腾讯云 TokenHub 模型列表
    url: https://cloud.tencent.com/document/product/1823/130051
    tier: 一手
  - name: 腾讯云 TokenHub 模型价格
    url: https://cloud.tencent.com/document/product/1823/130055
    tier: 一手
  - name: 腾讯云 TokenHub 产品页
    url: https://cloud.tencent.com/product/tokenhub
    tier: 一手
---

## 是什么

2026-11-16，腾讯云 TokenHub 的模型列表和模型价格页都写着最近更新时间 2026-11-16 12:15:30。模型列表新增 `hy4-flash`：深度思考（保留式思考）、结构化输出、Function Calling、Cache，以及图片理解。上下文 1M，最大输入 960k，最大输出 64k。这和 11 月 5 日已记的 `hy4` 不是同一个调用参数。

价格页的在线后付费表有广州和新加坡两个页签。两处抽到的 Hy4 flash 行都是：推理输入 0.5、推理输出 2、缓存命中 0.02，单位元 / 百万 tokens。缓存写入 5 分钟和 1 小时两列都是横线。页首注记写：自该说明发布之日起至北京时间 2026-11-30 12:00:00，Hy4 flash 按目录价的 50% 结算，到期恢复目录价。同页 Hy4 的 50% 折扣仍写到北京时间 2026-12-31 23:59:59，那是已经记下的期限，不另开。

产品页把 Hy4 flash 写成文本生成、深度思考和多模态理解，并写激活参数约为旗舰的四分之一。绝对参数量这次没有在上述官方页对上，标 **待核实**。产品页免费额度表把 Hy4 flash 和同页其他文本模型一起写成 100 万 tokens。

同一模型列表里，Hy4 preview 的名称格写着 2026-12-07 下线。这次没有对上这个日期是哪一天写上去的，不另开一条。

猜测挂靠：新的模型 ID 和标价在 G。这是供应商的型号和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-17：新建，status=open。
