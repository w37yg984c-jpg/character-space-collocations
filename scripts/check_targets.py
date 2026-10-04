# -*- coding: utf-8 -*-
"""检查目标角色名在三篇文本中出现的频次"""

import json
from pathlib import Path

CORPORA = {
    "金锁记": ("output/jinsuoji_tokenized.json", ["曹七巧", "七巧", "长安", "长白", "芝寿"]),
    "孔乙己": ("output/kongyiji_tokenized.json", ["孔乙己"]),
    "受戒":   ("output/shoujie_tokenized.json",  ["明海", "小明子", "小英子", "英子", "舅舅"]),
}

for title, (path, targets) in CORPORA.items():
    sents = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"\n=== {title} ===")
    for w in targets:
        n = sum(s.count(w) for s in sents)
        print(f"  {w}: {n} 次")