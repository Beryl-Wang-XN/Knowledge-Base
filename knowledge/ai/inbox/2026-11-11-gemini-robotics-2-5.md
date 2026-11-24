---
title: Google DeepMind 发布 Gemini Robotics 2.5
captured: 2026-11-11
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Google DeepMind 博客 Gemini Robotics 2.5
    url: https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/
    tier: 一手
---

## 是什么

2026-11-10，Google DeepMind 发布 Gemini Robotics 2.5，称为目前最强的 vision-language-action 模型，正在向机器人合作伙伴铺开。博客没有写公开 API、模型 ID 或标价。

能力对照写的是相对先前基线：按任务类型，成功率高 30% 到 100%，完成速度快 20% 到 30%。评测覆盖 200 多项任务。机器人形态沿用先前模型，点名 Apptronik Apollo 2 和 Franka Duo。

同一篇里的产线试点：与 Apptronik、Mercedes-Benz 合作，Apollo 2 在匈牙利 Kecskemét 和德国 Sindelfingen 的在产汽车生产线上做零件分拣配套。流程跟踪用 Gemini Robotics ER，手和手臂的动作用 Gemini Robotics 2.5。博客写成功率 96%。

安全部分也在这篇里，不另开一条。推理时的引导使绕过障碍的安全完成率提高 33%，附近有人时提高 43%。新的开源基准 ASIMOV-Jailbreak 用来测把不安全请求伪装进场景的提示，规模是数百条提示、数十个场景。博客写 Gemini 4 Argon 的越狱抵抗率是 99.5%，上一基线 Gemini Robotics ER 2 是 82%。

猜测挂靠：模型档案在 G。新的供应商模型正在铺给合作伙伴，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-11：新建，status=open。
