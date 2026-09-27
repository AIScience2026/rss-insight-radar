# AI 硬件创新情报站 · Daily AI Hardware Innovation Feed

每日更新的 AI 与智能硬件创新情报。收录 OpenAI / Google / Meta / Anthropic 官方发布，
The Verge / TechCrunch / Wired 的产品报道，arXiv cs.HC 与 cs.RO 的人机交互与机器人论文，
以及 a16z / The Information 的产业与资本观察。

**在线预览（v1.0）：** https://aiscience2026.github.io/rss-insight-radar/

**更新频率：** 每天 22:00 自动抓取一次（33 个一手信源），新增条目次日可见，累计 3000 余条。

---

## 收录范围

| 分类 | 内容 | 典型信源 |
|---|---|---|
| 大厂官方发布 | 模型、硬件、产品功能的一手公告 | OpenAI、Google DeepMind、Meta AI、Anthropic、Microsoft Research、Apple ML |
| 科技媒体 | 产品评测、发布报道、行业事件 | The Verge、TechCrunch、Ars Technica、Wired、Engadget |
| arXiv 学术线 | 人机交互与机器人方向论文 | cs.HC、cs.RO |
| 产业与资本 | 融资、并购、商业模式分析 | a16z、Sequoia、The Information、McKinsey、Stratechery |
| AI 前沿 Newsletter | 一线从业者的深度观察 | Import AI、Latent Space、Ben's Bites、HBR IdeaCast |
| 高校与实验室 | 研究机构发布 | MIT News、Stanford News、Harvard Gazette、CMU HCI、Wharton |

按「洞察评分」排序——评分由关键词启发式计算，反映与 AI 硬件 / 人机交互主题的相关度，
**非模型判断，不代表内容质量**。评分阈值可自行调整。

## 特性

- **每日自动更新** — 每天 22:00 抓取 33 个一手信源
- **浅色 / 深色自适应** — 跟随系统 `prefers-color-scheme`
- **全文搜索** — 标题 / 摘要 / 信源三字段检索，命中词高亮
- **分类筛选 + 评分阈值** — 双维度交叉过滤
- **隐私优先** — 无追踪代码、无 Cookie、无分析脚本

## 目录结构

```
.
├── index.html                  # 成品页面
├── template.html               # 页面模板（含 __DATA__ 占位符）
└── build_site.py               # 构建脚本：DB → 注入模板 → index.html
```

## 重新构建

`index.html` 是构建产物，直接改它会在下次抓取后被覆盖。
要更新数据或改版式，请改 `template.html`，然后重跑：

```bash
python build_site.py
```

脚本只读取 `source_name, title, link, category, summary, published, score, tags`
七个字段，且以只读模式（`mode=ro`）打开 SQLite，不会写入数据库。

## 部署

仓库已通过 **Settings → Pages → Source: Deploy from a branch**（branch: `main`, path: `/`）发布。
抓取入库后重新构建并上传 `index.html` 即可生效，无需构建步骤。

## 数据与版权

- 摘要统一截断至 300 字符
- 条目内容版权归原作者与出版方所有，本页仅为索引，点击标题跳转原文

## 许可

代码部分 MIT。条目内容版权归各信源所有。
