# AI 学习打卡表

> 每日记录学习情况。配合 `learning-plan.md` 使用。
> 状态：✅ 已学习 ｜ ⏭️ 跳过 ｜ 🔜 待进行 ｜ 🏗️ 建设

## 当前进度

> 状态更新：2026-11-09。

- **所处阶段**：阶段一已打卡两课。10 月 22 日是 KV Cache 与并发，11 月 5 日是 Prefill 与 Decode。B、D、E、G 的条目仍在库里。A、C、F 有条目。
- **正式每日页**：`daily/2026-11-05.md`。上一课是 `daily/2026-10-22.md`。`daily/_sample.md` 仍只是版式样例。
- **inbox**：Jev、Agent Compute Engine、Decisions API、SGLang Trainium 已并入档案或条目。Agent Skills 捐给 AAIF 标成 dropped。10 月 24 日到 11 月 8 日已有的定时情报在本地 inbox，状态仍是 open，尚未学习。拉取请求 #3–#15 已于 2026-11-05 关闭；#16–#18 是 11 月 6 日至 8 日仍按旧方式开出的请求，文件已收回，请求关闭且不合并。10 月 26 日、10 月 30 日和 11 月 9 日 8:00 没有产物，不补拉。
- **8:00 自动化约定（2026-11-09 起）**：每天只把新情报写入 `knowledge/ai/inbox/` 并直接推送到 `feature/beryl-build-knowledge-base`；不新开分支、不新开拉取请求，不写 entries、registry、daily、publish、progress 或学习计划。若某天未推送，当天留空，不在次日补写。
- **没有准确数据的字段**：写在对应条目和模型档案里。
- **档案还没建**：Kimi、智谱 GLM、豆包。Jev 已建档，不在旗舰价表里。
- **下一课**：从回顾排入的课仍是空的。下次按阶段一里还没作为每日页学过的下一个知识点。

## 打卡记录

| 日期 | 状态 | 主轨·学了什么 | 副轨·情报要点 |
|------|------|--------------|--------------|
| 2026-11-05 | ✅ | **Prefill 与 Decode 为什么特性相反，以及这怎么变成输入、输出不同价**。Prefill 一次并行整段输入，卡在算力，决定 TTFT；Decode 每步 1 个 token，反复搬运权重和 KV Cache，卡在显存带宽，决定 TPOT | 点名四条：Jev 不生成文本，公布价 $0.042/百万 input、output 不加价；Agent Compute Engine 客户预览在未来数月，凭证在 microVM 外；Decisions API 为 GPT-6 Luna，$0.10/$0.01 每百万 input，不改 GPT-5.6；SGLang Trainium beta 用 Trainium3 做 rollout、单台 H200 训练，无吞吐数字 |
| 2026-10-22 | ✅ | **KV Cache 为什么占显存，以及这怎么变成并发和成本**。用已核实的 vLLM 论文量级：13B 在 A100 40GB 上权重大约 65%、缓存大约 30%；传统管理有效利用 20.4%–38.2%，PagedAttention 浪费低于 4% | 点名三条：DeepInfer 开源但不含 KV cache 与负载均衡；OpenShell 用 inference.local 把凭证留在网关；OpenAI 模型将进 Google Cloud Model Garden，公告无价格 |
| 2026-08-31 | 🏗️ | **B 推理模块深度核实升级**：用 web_fetch 核实一手源（Orca 论文、PagedAttention 论文、FlashAttention 论文、投机解码论文、vLLM/SGLang/TensorRT-LLM 官方文档、Artificial Analysis 方法论），将 7 条全部重写为丰富版 | 核实到的关键数据：Orca 在 GPT-3 175B 上 **36.9×** 吞吐；投机解码 **2-3×** 无损加速；PagedAttention 吞吐 **2-4×**；**TensorRT-LLM 已移除 TensorRT 后端改用 PyTorch 后端**（修正旧条目错误）；TTFT/TPOT 官方定义 |
| 2026-08-31 | 🏗️ | **backfill 全量首建**：A(4)+B(7)+C(4)+D(4)+E(3)+F(3)=25 条条目 + 5 个模型档案 + 静态站点 | Qwen3.8-Max（2.4T/95B MoE）；GPU 规格；推理引擎格局 |
