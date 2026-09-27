# -*- coding: utf-8 -*-
"""build_site.py — 生成可发布到 GitHub Pages 的独立静态站点。

从 insight.db 读取数据，注入 site/template.html，产出单文件 index.html。
设计目标：
  1) 完全自包含（无外部请求、无 CDN、无字体、无分析脚本）
  2) 自带设计令牌（不依赖 Hermes / Obsidian 等宿主的 CSS 变量）
  3) 浅色/深色自适应
"""
import json
import pathlib
import sqlite3
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROJ = HERE.parent.parent          # site/ 的上一级的上一级即项目根
DB = PROJ / "pipeline" / "data" / "insight.db"
TEMPLATE = HERE / "template.html"
OUT = HERE / "index.html"

# 只取这些字段，避免把内部状态带出去
SELECT = """
    SELECT source_name, title, link, category, summary, published, score, tags
    FROM items
    WHERE dismissed = 0
    ORDER BY score DESC
    LIMIT 3000
"""


def fetch():
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    try:
        items = []
        for r in con.execute(SELECT):
            items.append({
                "src": r[0] or "",
                "title": r[1] or "",
                "link": r[2] or "",
                "cat": r[3] or "",
                "sum": (r[4] or "")[:300],   # 摘要截断，控体积
                "published": r[5] or "",
                "score": round(float(r[6] or 0), 1),
                "tags": r[7] or "",
            })
        return items
    finally:
        con.close()


def build(items):
    cats = sorted({it["cat"] for it in items if it["cat"]})
    payload = {
        "generated": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M"),
        "categories": cats,
        "items": items,
    }
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

    html = TEMPLATE.read_text(encoding="utf-8")
    if "__DATA__" not in html:
        sys.exit("模板缺少 __DATA__ 占位符")
    return html.replace("__DATA__", blob)


def main():
    if not DB.exists():
        sys.exit(f"找不到数据库: {DB}")
    items = fetch()
    html = build(items)
    OUT.write_text(html, encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    cats = sorted({it["cat"] for it in items if it["cat"]})
    print(f"✅ {OUT}  ({kb:.0f} KB)")
    print(f"   条目 {len(items)} ｜ 分类 {len(cats)} ｜ 版本文本 v1.0")
    print(f"   分类: {', '.join(cats)}")


if __name__ == "__main__":
    main()
