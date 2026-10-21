---
date: null
kind: sample
title: 为什么输出 token 比输入贵
entry: entries/B-inference/prefill-vs-decode.md
image: publish/xhs/_sample.png
status: 已存草稿，仅自己可见
---

# 为什么输出 token 比输入贵

推理不是一口气算完的。

它分成两段：

**Prefill**：你贴进去的整段话，模型一次并行算完。这一段吃的是 GPU 算力，所以相对便宜。

**Decode**：往外一个字一个字往外吐。每吐一个字，都要把整份权重和已算过的缓存再读一遍。这一段吃的是显存带宽，卡被占得更久，所以更贵。

记住一个拆法就够：

等第一个字 = Prefill  
后面每个字 = Decode

输出越长，越贵的是后半段，不是厂商随手加的价。

做模型和接口定价时，先问这句：这个场景是「读很多、写很少」，还是「写很长」？两种请求，烧的不是同一种资源。

配图放到本文件同目录，文件名 `_sample.png`（正式每日用 `YYYY-MM-DD.png`）。封面竖版，画面分开 Prefill / Decode，主文案用「输入便宜，输出更贵」。本次样例未附图片文件。

#AI #大模型 #Token #推理 #MaaS

---

已存入创作服务平台草稿，可见范围为仅自己可见。草稿在这台 Chrome 本地，不进 App。要发布时在该窗口草稿箱点编辑，自己点发布。
