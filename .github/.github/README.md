# 创新洞察雷达 · RSS Insight Radar

自包含的 RSS 情报仪表盘。从 33 个直连 RSS/Atom 信源抓取条目，按「洞察评分」排序，
全部数据内联于单个 `index.html` 中——无后端、无构建步骤、无外部请求。

**在线预览（v1.0）：** 见本仓库的 GitHub Pages。

---

## 特性

- **单文件部署** — 数据、样式、逻辑全部内联，`.html` 扔到任何静态托管即可运行
- **零外部依赖** — 无 CDN、无 Web Font、无分析脚本、无追踪代码，可用离线打开
- **浅色 / 深色自适应** — 跟随系统 `prefers-color-scheme`，自带设计令牌
- **洞察评分排序** — 关键词启发式打分（非模型判断），便于快速定位高价值条目
- **全文搜索** — 标题 / 摘要 / 信源三字段检索，命中词高亮
- **分类筛选 + 评分阈值** — 双维度交叉过滤
- **隐私优先** — 不含任何个人身份信息，条目均为公开信源引用

## 收录分类

| 分类 | 内容 |
|---|---|
| 高校与实验室 | MIT / Stanford / Harvard / CMU / Wharton 官方新闻与研究 |
| 风投/产业分析 | a16z、Sequoia、The Information、McKinsey、Stratechery |
| AI 前沿 Newsletter | Import AI、Latent Space、Ben's Bites、HBR IdeaCast |
| 大厂官方博客 | OpenAI、Google DeepMind、Anthropic、Microsoft Research、Meta AI、Apple ML |
| 科技媒体/消费电子 | The Verge、TechCrunch、Ars Technica、Wired、Engadget、Hacker News |
| arXiv 学术线 | cs.HC（人机交互）、cs.RO（机器人） |
| 播客 | Lex Fridman、Acquired、The Knowledge Project |

## 目录结构

```
.
├── index.html                  # 成品：单文件站点（数据已内联）
├── template.html               # 页面模板（含 __DATA__ 占位符）
├── build_site.py               # 构建脚本：DB → 注入模板 → index.html
└── .github/workflows/deploy.yml # GitHub Pages 自动部署
```

## 重新构建

`index.html` 是构建产物，直接改它会在下次抓取时被覆盖。
要更新数据，请改 `template.html` 或数据源，然后重跑：

```bash
python build_site.py
```

脚本只读取 `source_name, title, link, category, summary, published, score, tags`
八个字段，且以只读模式（`mode=ro`）打开 SQLite，不会写入数据库。

## 部署

推送到 `main` 分支即自动部署。仓库设置中开启
**Settings → Pages → Source: GitHub Actions** 即可。

## 数据与评分说明

- 评分由关键词启发式计算，反映「与产品创新 / 人机交互主题的相关度」，**非模型判断**，也不代表内容质量
- 摘要统一截断至 300 字符以控制体积
- 条目内容版权归原作者与出版方所有，本页仅为索引

## 许可

代码部分 MIT。条目内容版权归各信源所有。
