# 呈现层规范 (presentation)

> 被 SKILL.md 引用。描述 AI 知识库的多端呈现产出：静态 HTML 站点、quiz、小红书、播客。
> 核心原则：**数据源唯一**（`knowledge/ai/*.md`），**一次写作多端产出**。

## 数据流

```
entries/ + registry/          daily/YYYY-MM-DD.md           手写文稿
（完整条目，系统查阅）         （今日卡片 + quiz，推送）      publish/xhs、publish/podcast
            │                        │                         │
            └──────── scripts/build_site.py ──────────────────┘
                     （小红书文稿不进站点；播客有同名音频时嵌入每日页播放器）
                              │
                    site/index.html + site/daily/*.html（内嵌 quiz）
                    + site/modules/*（条目详情）
```

每日页的数据源是 `knowledge/ai/daily/YYYY-MM-DD.md`，模板为 `knowledge/ai/_templates/daily.md`。不要从长条目临时摘要出 HTML。`kind: sample` 只验证版式，不写入 `progress.md`。

## 一、静态 HTML 站点

纯静态（HTML + CSS + 少量原生 JS），无需服务器，双击即开，可一键传 GitHub Pages。

建议产物目录（构建生成，勿手改）：

```
knowledge/ai/daily/YYYY-MM-DD.md    # 每日页数据源（样例为 daily/_sample.md）
knowledge/ai/site/                  # 构建产物，gitignore，勿手改
├── index.html               # 首页：每日归档 + 模块入口
├── daily/YYYY-MM-DD.html     # 每日学习页（可累计、可翻历史），内嵌当天 quiz
└── modules/                  # 模块 Tab 页 + 各条目详情；registry.html 为模型库
```

样式和 quiz 脚本由 `scripts/build_site.py` 内联进每个页面。

- **每日页**：呈现计划里的下一课（含「对我的意义」）+ 当天点名的回顾 + quiz。
- **模块 Tab 页**：聚合该模块 `entries/` 下所有条目；G 页渲染 `registry/index.md` 对比表 + 各档案。
- **历史归档**：`index.html` 列出所有 `daily/` 页，可回翻。

## 二、Quiz

- 写在当日 `daily/*.md` 的 `## Quiz` 下，3–5 题。每题一个 `###` 序号，选项 `- [ ]`，唯一正确答案 `- [x]`，解析用一段引用 `>`。判断题同样写成两个选项。
- `scripts/build_site.py` 把它嵌进当日 HTML。点「看答案」后标出对错并显示解析。
- 题和解析只使用当天条目里已核实的内容。

## 三、小红书

文案写在 `knowledge/ai/publish/xhs/YYYY-MM-DD.md`。写完后，用用户本机已登录的 Chrome 打开小红书创作服务平台，把这篇预填进草稿。不点「发布」。

文案文件包含：
- 标题（吸睛、含关键词；平台标题上限 20 字，超了要改短）
- 正文（口语化、分点、emoji 适度，控制在 1000 字内）
- 标签（`#AI #大模型` 等，写在正文末尾）
- 封面：有图就放同目录（正式每日 `YYYY-MM-DD.png`，样例 `_sample.png`），并在文案里写明文件名。没有图时写明封面主文案，发布时用平台「文字配图」生成。样例目前没有附图片文件，封面主文案是「输入便宜，输出更贵」。
- front matter 的 `status`：预填成功后写成「已存草稿，仅自己可见」。

发布配置固定为：
- 可见范围：**仅自己可见**（在「更多设置」里把「公开可见」改掉）
- 只点「暂存离开」，不点「发布」

操作顺序（2026-10-21 用样例走通）：
1. 打开 `https://creator.xiaohongshu.com/publish/publish`。未登录就停下来，让用户在窗口里自己登录。不要代收或代填验证码。
2. 进入「上传图文」。有封面文件就上传；没有就点「文字配图」，写入封面主文案，生成后选一张，点「下一步」。
3. 填入标题和正文（含标签）。
4. 在「更多设置」把可见范围改成「仅自己可见」。
5. 点「暂存离开」。底部两个按钮包在自定义组件里，坐标点击可能只点到外层；要触发保存草稿，不要触发发布。
6. 打开草稿箱，确认「图文笔记」里有这篇，再改文案文件的 `status`。

约束：
- 草稿存在这台 Chrome 本地。清除该站数据会丢，也不会出现在小红书 App 的草稿箱。
- 用户要发出去时，在这个窗口的草稿箱点「编辑」，自己点「发布」。
- 不需要、也没有可调用的小红书发布 MCP。官方代发接口仍未对这个场景开放。

## 四、播客

口播稿写在 `knowledge/ai/publish/podcast/YYYY-MM-DD.md`。写完后用 `scripts/synthesize_podcast.py` 合成同名音频，再构建站点，每日页放播放器。另外在小宇宙主播后台预填一条草稿，方便手机上听。两处都不代点发布，页面也不会自动出声。

文案文件包含：
- 口播全文（自然口语）。正式每日稿按当天卡片写到可朗读约 20–30 分钟；样例只覆盖一个知识点时可以更短，不另编内容凑时长。
- 分段标记 `## 【…】`。合成时只读这些分段里的正文：去掉分段标题，去掉第一个分段之前的说明，去掉文末 `---` 之后的流程说明。
- front matter 的 `title` 是单集标题，小宇宙上限 60 字。
- front matter 的 `status`：音频生成后写成「已生成音频，待播放」。小宇宙草稿存好后补上「小宇宙草稿待发布」。

本地播放（音色晓晓，2026-10-21 用户确认）：
1. 音色写在 `knowledge/ai/kb.config.yaml` 的 `publish.podcast`：`edge-tts` 的 `zh-CN-XiaoxiaoNeural`（晓晓）。
2. 合成：`python3 scripts/synthesize_podcast.py knowledge/ai/publish/podcast/YYYY-MM-DD.md`。样例把路径换成 `_sample.md`。脚本输出同名 `.m4a`。合成时要联网，不需要语音账号。依赖：`python3 -m pip install --user edge-tts`。
3. 看将要朗读的文本：同一命令加 `--print`。小宇宙 Show Notes 用这段文本。
4. `python3 scripts/build_site.py ai` 会把该音频拷进站点，并在对应每日页放一个播放器。稿子在、音频不在时，构建会在终端提示先合成。
5. 打开每日页后点播放。浏览器不允许页面自己出声。

小宇宙（主播后台预填，不代发布）：

节目写在 `kb.config.yaml` 的 `publish.xiaoyuzhou`。当前节目 pid `6ad87d5c40b919d77a370338`，标题是 `beryl's AI learning`（2026-10-21 按用户选定改名，审核状态为待审核）。节目标题最多 20 字；更长的名字先停下来问，不要擅自截短。

1. 打开 `https://podcaster.xiaoyuzhoufm.com`。未登录就停下来，让用户自己扫码登录。不要代收或代填验证码。
2. 还没有节目时先停下来问，不擅自创建公开节目。节目标题最多 20 字。
3. 自有节目创建单集前，账号必须完成主体认证。未认证时「创建单集」只弹出「需完成主体认证后，才能继续操作」。这时停下来，让用户自己完成实名认证或企业认证（弹窗里的「去认证」，或账户设置里的实名认证，路径 `/qualification/real-name`）。不要代填证件。
4. 认证完成后：打开该节目的单集列表，点「创建单集」（路由 `/podcast/<pid>/episode/create`）。上传刚合成的 m4a。单集标题用口播稿 front matter 的 `title`。Show Notes 用 `--print` 打出的正文。保存草稿。
5. 不点「发布」，也不调用 `/v1/episode/hosted/publish`。草稿在小宇宙服务器上。用户在小宇宙 App 的创作中心打开这条即可试听。公开发给听众要用户自己点发布。小宇宙没有「仅自己可见」；未发布的草稿就是不公开的状态。
6. 在内容管理里确认这条是未发布草稿后，再改文案 `status`。创建页若要求封面而节目没有可用封面，停下来问用户，不要擅自做一张公开封面。

用 Chrome 操作时带上完整页面地址。同时开着多个主播后台标签时，打到当前这个节目的标签，避免把单页应用刷回首页。

## 构建脚本约定

- **前端复用优先**：构建 HTML 站点前，先查找是否有成熟的前端 skill / 模板可复用（可用 find-skills 或从 GitHub 下载），能用现成的就不从零手写，以保证质量与效率。
- 脚本是仓库根目录的 `scripts/build_site.py`。样式和 quiz 脚本内联在页面里。
- 条目页读 `entries/` 与 `registry/`；每日页读 `daily/*.md`。小红书文稿不进站点。播客有同名音频时，拷进 `site/audio/` 并嵌入当日页播放器；没有音频时只在终端提示。
- 站点为**构建产物**：源改在 Markdown，站点由脚本重建，勿手改 `site/`。
- 版式样例：`daily/_sample.md`（Prefill vs Decode）。正式学习再写带日期的每日页。
