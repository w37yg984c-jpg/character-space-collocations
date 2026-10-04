# -*- coding: utf-8 -*-
"""
预处理三篇小说：
1. 读取 UTF-8 文本
2. 繁转简（OpenCC t2s）
3. 清洗噪声（去缩进、多余空行、网页残留）
4. 分句
5. jieba 分词
6. 保存分好词的句子到 output/{name}_tokenized.json
7. 打印每篇的统计（字符数、句数、词数）
"""

import json
import re
from pathlib import Path

import jieba
from opencc import OpenCC

# ---------- 配置 ----------
DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

CORPORA = {
    "jinsuoji": {"file": "jinsuoji.txt", "title": "金锁记", "author": "张爱玲"},
    "kongyiji": {"file": "kongyiji.txt", "title": "孔乙己", "author": "鲁迅"},
    "shoujie":  {"file": "shoujie.txt",  "title": "受戒",   "author": "汪曾祺"},
}

# 繁 -> 简
cc = OpenCC("t2s")

# 句末标点
SENT_SPLIT_PATTERN = re.compile(r"(?<=[。！？!?…；;\n])")


def clean_text(text: str) -> str:
    """去除常见噪声，但保留段落结构。"""
    # 繁转简
    text = cc.convert(text)

    # 去掉每行开头的空格/全角空格缩进
    text = re.sub(r"^[ \t\u3000]+", "", text, flags=re.MULTILINE)

    # 去掉网页残留符号
    text = re.sub(r"（这里空行）", "", text)
    text = re.sub(r"\[?\d+\]?", "", text)
    text = re.sub(r"返回目录|上一篇|下一篇|www\.[^\s]+", "", text)

    # 连续空行压成一个换行
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()


def split_sentences(text: str):
    """按句末标点分句，去掉空句和过短句。"""
    parts = SENT_SPLIT_PATTERN.split(text)
    sentences = []
    for p in parts:
        p = p.strip()
        p = re.sub(r"^[。！？!?…；;，,、\s]+", "", p)
        if len(p) < 2:
            continue
        sentences.append(p)
    return sentences


def tokenize(sentence: str):
    """jieba 分词，去掉空白 token。"""
    tokens = [w.strip() for w in jieba.lcut(sentence)]
    tokens = [w for w in tokens if w]
    return tokens


def main():
    summary = []
    for key, info in CORPORA.items():
        path = DATA_DIR / info["file"]
        print(f"\n=== 处理 {info['title']}（{info['author']}）===")

        raw = path.read_text(encoding="utf-8")
        text = clean_text(raw)
        sentences = split_sentences(text)

        tokenized = [tokenize(s) for s in sentences]
        n_chars = sum(len(s) for s in sentences)
        n_sents = len(tokenized)
        n_tokens = sum(len(t) for t in tokenized)

        summary.append({
            "key": key,
            "title": info["title"],
            "author": info["author"],
            "chars": n_chars,
            "sentences": n_sents,
            "tokens": n_tokens,
        })

        out = OUTPUT_DIR / f"{key}_tokenized.json"
        with out.open("w", encoding="utf-8") as f:
            json.dump(tokenized, f, ensure_ascii=False)
        print(f"  字符数: {n_chars}")
        print(f"  句数:   {n_sents}")
        print(f"  词数:   {n_tokens}")
        print(f"  已保存: {out}")

    print("\n=== 汇总 ===")
    for s in summary:
        print(f"{s['title']:6s} | {s['author']:4s} | "
              f"字符 {s['chars']:>6d} | 句 {s['sentences']:>5d} | 词 {s['tokens']:>6d}")


if __name__ == "__main__":
    main()