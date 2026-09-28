# AI 硬件创新情报站 / Daily AI Hardware Innovation Feed

**EN** — A daily feed of AI and smart-hardware innovation, drawn from first-party sources:
product and model announcements from OpenAI, Google, Meta and Anthropic; hardware reporting
from The Verge, TechCrunch and Wired; arXiv cs.HC and cs.RO papers on human-robot interaction
and robotics; and capital and industry analysis from a16z and The Information. Entries are
collected automatically every day at 22:00 and ranked by an insight score.

**中文** — 每日更新的 AI 与智能硬件创新情报。收录 OpenAI / Google / Meta / Anthropic 官方发布，
The Verge / TechCrunch / Wired 的产品报道，arXiv cs.HC 与 cs.RO 的人机交互与机器人论文，
以及 a16z / The Information 的产业与资本观察。每天 22:00 自动抓取，按洞察评分排序。

**在线预览（v1.0）：** https://aiscience2026.github.io/rss-insight-radar/

**更新频率 / Cadence:** 每天 22:00 自动抓取一次，新增条目次日可见。
Sources are polled once a day at 22:00; new entries appear the next day.

> 页面上的「收录条目数 / 信源数 / 时间跨度」以及中英文界面文案，均由前端实时渲染，
> 不依赖后端；英文为默认语言，右上角可切换中文。
> Entry counts, source counts and coverage span are rendered client-side from the embedded
> payload. English is the default; switch to Chinese with the toggle in the header.

---

## 特性 / Features

- **每日自动更新** — 每天 22:00 抓取一手信源
- **数字实时统计** — 收录量 / 信源数 / 时间跨度均构建时从库内算出
- **时间范围筛选** — 今天 / 近3天 / 7天 / 1个月 / 3个月 / 6个月 / 1年 / 全部（默认近7天）
- **中英双语** — 默认英文，右上角一键切换，`html[lang]` 同步更新
- **浅色 / 深色自适应** — 跟随系统 `prefers-color-scheme`
- **全文搜索** — 标题 / 摘要 / 信源三字段检索，命中词高亮
- **分类筛选 + 评分阈值** — 双维度交叉过滤，可与时间筛选叠加
- **隐私优先** — 无追踪代码、无 Cookie、无分析脚本

## 收录分类 / Categories

| 分类 | 内容 |
|---|---|
| 高校与实验室 | MIT / Stanford / Harvard / CMU / Wharton 官方新闻与研究 |
| 风投/产业分析 | a16z、Sequoia、The Information、McKinsey、Stratechery |
| AI 前沿 Newsletter | Import AI、Latent Space、Ben's Bites、HBR IdeaCast |
| 大厂官方博客 | OpenAI、Google DeepMind、Anthropic、Microsoft Research、Meta AI、Apple ML |
| 科技媒体/消费电子 | The Verge、TechCrunch、Ars Technica、Wired、Engadget、Hacker News |
| arXiv 学术线 | cs.HC（人机交互）、cs.RO（机器人） |
| 播客 | Lex Fridman、Acquired、The Knowledge Project |

## 目录结构 / Layout

```
.
├── index.html                  # 成品页面（数据已内联）
├── template.html               # 页面模板（含 __DATA__ 占位符 + i18n 字典）
└── build_site.py               # 构建脚本：DB → 注入模板 → index.html
```

## 重新构建 / Rebuild

`index.html` 是构建产物，直接改它会在下次抓取后被覆盖。
要更新数据或改版式，请改 `template.html`，然后重跑：

```bash
python build_site.py
```

脚本只读取 `source_name, title, link, category, summary, published, score, tags`
七个字段，且以只读模式（`mode=ro`）打开 SQLite，不会写入数据库。

## 新增界面文案 / Adding UI strings

所有界面文案集中在 `template.html` 的 `I18N` 字典中，`en` 与 `zh` 两个键必须对称新增：

```js
var I18N = {
  en: { newKey: "English text", ... },
  zh: { newKey: "中文文案", ... }
};
```

带变量的文案用函数形式，例如 `showing(a, b)`、`loadMore(n)`、`footerData(t, s, n, cut)`。
HTML 元素用 `data-i18n="key"`（文本）或 `data-i18n-ph="key"`（placeholder）挂载，
由 `paintStatic()` 统一刷新。

## 部署 / Deployment

仓库已通过 **Settings → Pages → Source: Deploy from a branch**（branch: `main`, path: `/`）发布。
抓取入库后重新构建并上传 `index.html` 即可生效，无需构建步骤。

## 数据与版权 / Data & License

- 摘要统一截断至 300 字符
- 条目内容版权归原作者与出版方所有，本页仅为索引，点击标题跳转原文
- 代码部分 MIT
