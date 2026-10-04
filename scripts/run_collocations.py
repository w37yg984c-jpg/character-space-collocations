# -*- coding: utf-8 -*-
"""
对每个 target 词跑三种设置：
  - window h=5
  - window h=10
  - sentence（整句共现）

停用词在调用 find_collocates 之前手动过滤。
每个结果存一个 CSV：output/collocates_{corpus}_{target}_{setting}.csv
"""

import json
from pathlib import Path

from qhchina import find_collocates, load_stopwords

# ---------- 配置 ----------
OUTPUT_DIR = Path("output")

TASKS = [
    ("jinsuoji", "金锁记", "七巧"),
    ("jinsuoji", "金锁记", "长安"),
    ("kongyiji", "孔乙己", "孔乙己"),
    ("shoujie",  "受戒",   "小英子"),
    ("shoujie",  "受戒",   "明海"),
]

SETTINGS = [
    ("window5",  dict(method="window",   horizon=5)),
    ("window10", dict(method="window",   horizon=10)),
    ("sentence", dict(method="sentence")),
]

FILTERS = {"min_word_length": 2, "max_p": 0.05}

STOPWORDS = load_stopwords()
print(f"停用词数量: {len(STOPWORDS)}")


def run_one(corpus_key, target, setting_name, setting_kwargs):
    path = OUTPUT_DIR / f"{corpus_key}_tokenized.json"
    sentences = json.loads(path.read_text(encoding="utf-8"))

    # 过滤停用词
    sentences = [
        [w for w in sent if w not in STOPWORDS]
        for sent in sentences
    ]

    df = find_collocates(
        sentences,
        target_words=target,
        filters=FILTERS,
        **setting_kwargs,
    )

    out = OUTPUT_DIR / f"collocates_{corpus_key}_{target}_{setting_name}.csv"
    df.to_csv(out, index=False, encoding="utf-8-sig")
    print(f"  [{corpus_key}/{target}/{setting_name}] "
          f"{len(df)} 条 -> {out.name}")
    return df


def main():
    for corpus_key, title, target in TASKS:
        print(f"\n=== {title} / target = {target} ===")
        for setting_name, kwargs in SETTINGS:
            try:
                run_one(corpus_key, target, setting_name, kwargs)
            except Exception as e:
                print(f"  !! {setting_name} 失败: {e}")


if __name__ == "__main__":
    main()