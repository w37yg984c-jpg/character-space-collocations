# Collocations and Character-Space in Three Modern Chinese Novels

## 1. Corpus and Scale

This study analyses three modern Chinese short stories/novellas: 
Zhang Ailing's The Golden Cangue (金锁记), Lu Xun's Kong Yiji (孔乙己), and Wang Zengqi's Ordination (受戒). All three were obtained from publicly available full-text sources online. After traditional-to-simplified conversion and sentence segmentation, the corpora contain approximately:
The Golden Cangue: 29602 characters, 1140 sentences
Kong Yiji: 2584 characters, 126 sentences
Ordination: 2279 characters, 163 sentences

The target characters analysed are Qiqiao (七巧) and Chang'an (长安) in The Golden Cangue, Kong Yiji (孔乙己) in the eponymous story, and Minghai (明海) / Xiao Yingzi (小英子) in Ordination. The full name of the main character in The Golden Cangue is Cao Qiqiao, but Zhang Ailing liked to call her Qiqiao in the novel.

## 2. Method and Statistical Setup

For each target character, collocates were identified with `find_collocates` (qhchina). For every co-occurring word, the method builds a 2×2 contingency table counting: (a)co-occurrences of the word with the target inside the window; (b) occurrences of the word elsewhere in the corpus; (c) target occurrences without the word; (d) all remaining tokens. 

Fisher's exact test is then applied with `alternative="greater"`, because we are interested only in words that appear near the target more often than chance predicts. A p-value below 0.05 indicates that such over-representation is unlikely under independence.

Three settings were compared for every target: a 5-token window, a 10-token window, and whole-sentence co-occurrence. Filters kept only words of at least two characters with p < 0.05.

## 3. Results

In The Golden Cangue, Qiqiao's collocates cluster into three groups which are body parts(身子, 袖子...), controlling verbs(盘问, 吩咐...), and kinship/power terms (老妈子, 媳妇...). Her space is thus defined by physical presence and domestic authority. Notably, introspective words (觉得, 不觉) are absent.

Chang'an, by contrast, is surrounded by interior states (觉得, 不觉...), romantic relations (世舫, 订婚), and indoor objects (口琴, 屋子, 火炉). Her collocates contain almost no body parts.

This contrast is significant for Woloch's concept of character-space. Mother and daughter inhabit the same household yet are assigned by the narrative to structurally different lexical environments: Qiqiao is externalised through action and power; Chang'an is internalised through feeling and romance. They are in different fields.

## 4. Methodological Reflection

Scaling up the corpus would stabilise the statistics but not change the fundamental limitation. Whether Qiqiao's smiling is sincere or ironic cannot be determined statistically.Woloch's character-space is thus only partially operationalisable. They miss something like what the narrative withholds, displaces, or conveys through others. A collocational profile can show the places of the characters and the places they are not in.