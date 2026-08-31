# 呈现层规范 (presentation)

> 被 SKILL.md 引用。描述 AI 知识库的多端呈现产出：静态 HTML 站点、quiz、小红书、播客。
> 核心原则：**数据源唯一**（`knowledge/ai/*.md`），**一次写作多端产出**。

## 数据流

```
knowledge/ai/*.md（唯一数据源：entries/ + registry/ + inbox/）
            │
     构建脚本（建议 Python，复用仓库 shared/ 工具层）
   ┌────────┼─────────────┬──────────────┐
   ▼        ▼             ▼              ▼
HTML站点   quiz(内嵌)   小红书文案(.md)   播客口播稿(.md)
```

## 一、静态 HTML 站点

纯静态（HTML + CSS + 少量原生 JS），无需服务器，双击即开，可一键传 GitHub Pages。

建议产物目录（构建生成，勿手改）：

```
knowledge/ai/site/
├── index.html               # 首页：最新每日 + 模块入口 + 历史归档
├── daily/YYYY-MM-DD.html     # 每日学习页（可累计、可翻历史），内嵌当天 quiz
├── modules/                  # 模块 Tab 页（系统查阅，随每日更新刷新）
│   ├── A-model.html
│   ├── B-inference.html
│   ├── C-compute.html
│   ├── D-serving.html
│   ├── E-economics.html
│   ├── F-landscape.html
│   └── G-registry.html       # 模型档案库对比表 + 各模型档案
└── assets/                   # css / js
```

- **每日页**：呈现当天主轨知识点（含「对我的意义」）+ 副轨情报要点 + quiz。
- **模块 Tab 页**：聚合该模块 `entries/` 下所有条目；G 页渲染 `registry/index.md` 对比表 + 各档案。
- **历史归档**：`index.html` 列出所有 `daily/` 页，可回翻。

## 二、Quiz

- 基于当天主轨内容出 3-5 题（选择/判断），内嵌在当日 HTML 页。
- 纯前端交互：点选即时对答案 + 给解析。答案与解析源自当天条目「关键点」。

## 三、小红书文案

产出为 `knowledge/ai/publish/xhs/YYYY-MM-DD.md`，包含：
- 标题（吸睛、含关键词）
- 正文（口语化、分点、emoji 适度、控制在小红书篇幅）
- 标签（#AI #大模型 等）
- **配图**：用 AI 生成（image_gen），存同目录，供用户下载
- 结尾注明：**待用户手动发布**（本 skill 无法自动发布）

## 四、播客口播稿

产出为 `knowledge/ai/publish/podcast/YYYY-MM-DD.md`，包含：
- 口播全文（自然口语、可直接朗读、约 20-30 分钟内容量）
- 分段标记（便于用户 TTS 分段合成）
- 结尾注明：**待用户用第三方 TTS 转音频**（本 skill 无法生成音频）

## 构建脚本约定

- **前端复用优先**：构建 HTML 站点前，先查找是否有成熟的前端 skill / 模板可复用（可用 find-skills 或从 GitHub 下载），能用现成的就不从零手写，以保证质量与效率。
- 语言建议 Python，复用仓库根 `shared/`（已有 config/indexer 等）。
- 脚本读取 `knowledge/ai/**/*.md` 的 front matter + 正文，渲染为上述 HTML。
- 站点为**构建产物**：源改在 Markdown，站点由脚本重建，勿手改 `site/`。
- 实现时机：待积累 2-3 天真实条目（或 backfill 完成）后再落地脚本，确保有内容可渲染调试。
