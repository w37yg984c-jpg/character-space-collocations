# -*- coding: utf-8 -*-
"""把所有 collocates_*.csv 拼成一个 HTML 页面，方便对比浏览。"""

from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("output")
OUT_HTML = OUTPUT_DIR / "results.html"

# 按语料 -> target -> 设置 排序展示
ORDER = [
    ("jinsuoji", "七巧"),
    ("jinsuoji", "长安"),
    ("kongyiji", "孔乙己"),
    ("shoujie",  "小英子"),
    ("shoujie",  "明海"),
]
SETTINGS = ["window5", "window10", "sentence"]

TITLES = {
    "jinsuoji": "金锁记（张爱玲）",
    "kongyiji": "孔乙己（鲁迅）",
    "shoujie":  "受戒（汪曾祺）",
}


def df_to_html(df, max_rows=30):
    """只显示前 max_rows 行，并给 ratio_local 加色阶。"""
    df = df.head(max_rows).copy()
    df["ratio_local"] = df["ratio_local"].round(2)
    df["exp_local"] = df["exp_local"].round(2)
    df["p_value"] = df["p_value"].round(4)
    return df.to_html(index=False, border=0, classes="tbl")


def main():
    parts = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='utf-8'>",
        "<title>Collocation Results</title>",
        "<style>",
        "body{font-family:sans-serif;margin:24px;max-width:1100px}",
        "h1{border-bottom:2px solid #333;padding-bottom:6px}",
        "h2{margin-top:36px;color:#2c3e50}",
        "h3{color:#555;margin-bottom:6px}",
        ".tbl{border-collapse:collapse;margin:8px 0 24px 0;font-size:13px}",
        ".tbl td,.tbl th{border:1px solid #ccc;padding:3px 8px;text-align:right}",
        ".tbl td:nth-child(2),.tbl th:nth-child(2){text-align:left}",
        ".tbl th{background:#f0f0f0}",
        "</style></head><body>",
        "<h1>Collocation Results — Character-Space 分析</h1>",
        "<p>每个角色 × 三种设置（window=5 / window=10 / sentence）。"
        "只显示前 30 行，按 obs_local 降序。</p>",
    ]

    for corpus_key, target in ORDER:
        parts.append(f"<h2>{TITLES[corpus_key]} — target = {target}</h2>")
        for setting in SETTINGS:
            csv = OUTPUT_DIR / f"collocates_{corpus_key}_{target}_{setting}.csv"
            if not csv.exists():
                parts.append(f"<p><em>{setting}: 文件不存在</em></p>")
                continue
            df = pd.read_csv(csv)
            parts.append(f"<h3>{setting}（{len(df)} 条）</h3>")
            if df.empty:
                parts.append("<p><em>空表</em></p>")
            else:
                parts.append(df_to_html(df))

    parts.append("</body></html>")
    OUT_HTML.write_text("\n".join(parts), encoding="utf-8")
    print(f"已生成: {OUT_HTML}")


if __name__ == "__main__":
    main()