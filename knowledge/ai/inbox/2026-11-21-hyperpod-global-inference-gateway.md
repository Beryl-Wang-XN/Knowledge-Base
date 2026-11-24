---
title: SageMaker HyperPod 推出跨集群的 Global Inference Gateway
captured: 2026-11-21
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS 机器学习博客
    url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-global-inference-gateway-one-endpoint-across-regions-and-clusters/
    tier: 一手
---

## 是什么

AWS 机器学习博客的日期是 2026-11-20。Amazon SageMaker HyperPod 推出 Global Inference Gateway：一个由 SageMaker 托管的网关，把请求路由到已登记的多个集群，可以在同一个区域，也可以跨区域。集群内部仍由原来的 Inference Gateway 按 pod 放置。请求走 AWS 骨干网，用 SigV4 和 IAM 认证，经 AWS PrivateLink 到达集群。博客写网关不记录、也不保存提示词和补全。接口写成与 OpenAI 兼容，请求要带 SigV4 签名。

默认路由权重是区域邻近 0.40、队列深度 0.25、KV 余量 0.20、错误率 0.15。四个权重都要给的话，每个取 0.0 到 1.0，并且加起来等于 1.0；设成 0 表示关掉该信号。不填则用上面的默认值。集群失败时，流量转到下一个得分更高的健康集群；还没开始流式输出的失败请求会在另一个集群重试一次。没有健康集群时返回 503。

可用区域写了 13 个：美国东部（弗吉尼亚北部）、美国东部（俄亥俄）、美国西部（加利福尼亚北部）、美国西部（俄勒冈）、南美（圣保罗）、欧洲（法兰克福）、欧洲（爱尔兰）、欧洲（伦敦）、欧洲（斯德哥尔摩）、亚太（东京）、亚太（孟买）、亚太（新加坡）和亚太（悉尼）。

博客没有写出网关本身的单价或加价，待核实。它写明：已经发布、但没有加入任何网关的集群收不到流量，它前面的 Network Load Balancer 仍在运行并会计费。11 月 18 日已记的跨区域实时端点路由是另一项，不并进来。

猜测挂靠：跨集群的推理路由在 D。这是供应商的推理服务，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改 `registry/`。

## 处置记录

- 2026-11-21：新建，status=open。
