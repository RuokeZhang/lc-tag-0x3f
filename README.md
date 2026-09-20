# LeetCode 公司高频题 · 灵神分类可视化

Static HTML visualization of company-tagged LeetCode problems, categorized by
[灵茶山艾府 (0x3F)](https://leetcode.cn/u/endlesscheng/)'s problem lists. Each
subcategory is sorted by frequency (descending). Supports Chinese/English toggle
and switches problem links between `leetcode.cn` and `leetcode.com`. Contest
difficulty ratings can be shown on demand.

## Files

- `build.py` — generator. Reads `../<company>/*.csv` and writes into
  `leetcode/<company>.html`.
- `fetch_basics.py` — fetches Blind 75, Grind 75, NeetCode 250, LC 75, Top 100,
  Top Interview 150 into `basics.json`.
- `lc_titles.json` — cached zh/en title + slug for every LC problem, fetched
  from `leetcode.cn/graphql/`.
- `ratings.json` — cached contest difficulty ratings from
  [zerotrac/leetcode_problem_rating](https://github.com/zerotrac/leetcode_problem_rating).
- `index.html` (repo root) — 302 to `/leetcode/`.
- `leetcode/index.html` — landing page linking to each company's page.
- `leetcode/<company>.html` — self-contained page (data + JS embedded).
- Deployed to `ruokezhang.com` via GitHub Pages; served at
  `ruokezhang.com/leetcode/`.

## Rebuild

```bash
python3 build.py                  # rebuild all supported companies
python3 build.py apple microsoft  # any companies with a sibling CSV dir
python3 build.py --refresh-ratings # refresh ratings, then rebuild all companies
```

## Data sources

- Company question frequency CSVs:
  [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions)
- Categorization: 灵茶山艾府's题单 series on leetcode.cn discuss
  (链表/二叉树/DP/图论/数据结构/单调栈/二分/贪心/数学/字符串/位运算/回溯/滑动窗口)
- Contest difficulty ratings:
  [zerotrac/leetcode_problem_rating](https://github.com/zerotrac/leetcode_problem_rating)
- Company marks: [Simple Icons](https://simpleicons.org/) and Wikimedia Commons

## Notes

- 一般树 subcategories are folded under 二叉树; 网格图 subcategories are folded
  under 图论 (with the source prefix preserved: e.g. `网格图·DFS`).
- Uncovered problems land in a "未分类 / Uncategorized" bucket.
