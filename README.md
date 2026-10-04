# Character-Space and Collocations in Three Modern Chinese Novels

This repository contains a collocation analysis of three modern Chinese
novels. Using statistical collocation methods, it examines how target
characters are represented in the text through words that significantly
co-occur with their names. The analysis is framed by Alex Woloch's
concept of "character-space."

## Corpus

| Title | Author | Source |
|-------|--------|--------|
| 《金锁记》 | 张爱玲 | https://s.bailushuyuan.org/%E9%87%91%E9%94%81%E8%AE%B0 |
| 《孔乙己》 | 鲁迅 | https://zh.wikisource.org/wiki/%E5%AD%94%E4%B9%99%E5%B7%B1 |
| 《受戒》 | 汪曾祺 | https://millionbook.net/xd/w/wangzengqi/wzqw/035.htm |

Corpus sizes (after cleaning):

| Work | Characters | Sentences | Tokens |
|------|-----------:|----------:|-------:|
| 金锁记 | 29,602 | 1,140 | 20,435 |
| 孔乙己 | 2,584 | 126 | 1,788 |
| 受戒 | 2,279 | 163 | 1,582 |

## Target characters

- 七巧 — *金锁记*
- 长安 — *金锁记*
- 孔乙己 — *孔乙己*
- 明海, 小英子 — *受戒*

## Method

- Traditional-to-simplified conversion: OpenCC (t2s)
- Sentence segmentation and tokenisation: jieba
- Stopword removal: `qhchina.load_stopwords()` (806 entries)
- Collocation extraction: `qhchina.find_collocates`
- Statistical test: Fisher's exact test, one-tailed (`alternative="greater"`)
- Filters: `min_word_length=2`, `max_p=0.05`
- Three settings compared: window=5, window=10, sentence-level

## Repository structure

```
.
├── README.md
├── .gitignore
├── data/                    # raw text corpora (UTF-8)
├── scripts/
│   ├── preprocess.py        # cleaning, segmentation, tokenisation
│   ├── check_targets.py     # target frequency check
│   ├── run_collocations.py  # main collocation analysis
│   └── build_html.py        # generate combined HTML report
├── output/
│   ├── *_tokenized.json     # intermediate tokenised sentences
│   ├── collocates_*.csv     # one CSV per run
│   └── results.html         # all tables in one page
├── report.md
└── report.pdf
```

## How to reproduce

```bash
pip install qhchina jieba opencc-python-reimplemented pandas
python scripts/preprocess.py
python scripts/run_collocations.py
python scripts/build_html.py
```

## Output

- `output/collocates_*.csv` — one CSV per run (target × setting)
- `output/results.html` — all collocation tables on one page
- `report.md` / `report.pdf` — analysis and interpretation