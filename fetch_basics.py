#!/usr/bin/env python3
"""Fetch the union of well-known "basic" LeetCode lists and save to basics.json.

Sources:
- LeetCode 75 (official study plan: leetcode-75)
- Top 100 Liked (official: top-100-liked)
- Top Interview 150 (official: top-interview-150)
- NeetCode 150 (hardcoded, sourced from https://neetcode.io/practice)
- Blind 75 (hardcoded, canonical original list)
- Grind 75 (hardcoded, from techinterviewhandbook.org/grind75)
"""

import json
import urllib.request
from pathlib import Path

BASE = Path(__file__).parent


def fetch_study_plan(slug):
    query = "query studyPlanV2Detail($planSlug: String!) { studyPlanV2Detail(planSlug: $planSlug) { planSubGroups { questions { questionFrontendId } } } }"
    data = json.dumps({"query": query, "variables": {"planSlug": slug}}).encode()
    req = urllib.request.Request('https://leetcode.cn/graphql/', data=data, headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://leetcode.cn/',
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        resp = json.loads(r.read())
    detail = resp['data']['studyPlanV2Detail']
    ids = []
    for group in detail['planSubGroups']:
        for q in group['questions']:
            ids.append(int(q['questionFrontendId']))
    return ids


# NeetCode 150 (curated from neetcode.io/practice)
NEETCODE_150 = [
    217, 242, 1, 49, 347, 271, 238, 36, 128,
    125, 167, 15, 11, 42,
    121, 3, 424, 567, 76, 239,
    20, 155, 150, 22, 739, 853, 84,
    704, 74, 153, 33, 875, 981, 4,
    206, 21, 143, 19, 141, 287, 138, 2, 25, 23,
    226, 104, 543, 110, 100, 572, 235, 105, 124, 297, 98, 230, 199, 1448, 337,
    208, 211, 212,
    703, 1046, 973, 215, 621, 355, 295,
    78, 39, 40, 46, 47, 77, 90, 79, 131, 51,
    200, 133, 417, 207, 210, 261, 323, 130, 269, 127, 695,
    743, 787, 1584,
    70, 746, 198, 213, 5, 647, 91, 322, 152, 300, 139,
    62, 1143, 309, 518, 494, 97, 329, 115, 72,
    53, 55, 45, 763, 678, 846, 1899, 134,
    57, 56, 435, 252, 253, 1851,
    48, 54, 73, 202, 66, 43, 50, 2013,
    136, 191, 338, 190, 268, 371, 7,
]

# Blind 75 (original)
BLIND_75 = [
    1, 121, 217, 238, 53, 152, 153, 33, 15, 11,
    371, 191, 338, 268, 190,
    70, 322, 300, 1143, 139, 377, 198, 213, 91, 62, 55,
    133, 417, 207, 210, 269, 261, 323,
    57, 56, 435, 252, 253,
    141, 21, 23, 143, 19, 206,
    73, 54, 48, 79,
    3, 424, 76, 271, 242, 49, 20, 125, 5, 647,
    226, 104, 100, 572, 105, 297, 98, 230, 235, 124, 208, 211, 212,
    347, 295,
]

# Grind 75 (from techinterviewhandbook.org/grind75)
GRIND_75 = [
    1, 20, 21, 121, 125, 226, 242, 704, 733, 235, 110, 141, 232, 278,
    383, 70, 409, 206, 169, 67, 543, 108, 100, 217, 268, 344, 977, 15,
    3, 102, 133, 322, 200, 238, 155, 98, 208, 57, 542, 973, 300, 692,
    79, 33, 39, 46, 56, 981, 75, 139, 416, 8, 54, 78, 199, 5, 62, 105,
    11, 17, 23, 84, 240, 76, 143, 297, 114, 45, 218, 763, 295, 146, 138,
    124, 236, 32, 224, 269, 72, 312, 273, 887, 41, 4,
]


def main():
    lc_75 = fetch_study_plan('leetcode-75')
    top_100 = fetch_study_plan('top-100-liked')
    interview_150 = fetch_study_plan('top-interview-150')

    print(f"LeetCode 75:       {len(lc_75):3d} problems")
    print(f"Top 100 Liked:     {len(top_100):3d} problems")
    print(f"Top Interview 150: {len(interview_150):3d} problems")
    print(f"NeetCode 150:      {len(set(NEETCODE_150)):3d} problems")
    print(f"Blind 75:          {len(set(BLIND_75)):3d} problems")
    print(f"Grind 75:          {len(set(GRIND_75)):3d} problems")

    basics = {
        'lc_75': lc_75,
        'top_100': top_100,
        'interview_150': interview_150,
        'neetcode_150': NEETCODE_150,
        'blind_75': BLIND_75,
        'grind_75': GRIND_75,
    }
    union = set()
    for ids in basics.values():
        union.update(ids)
    print(f"Union total:       {len(union):3d} unique problems")

    basics['union'] = sorted(union)
    (BASE / 'basics.json').write_text(json.dumps(basics, indent=None), encoding='utf-8')
    print(f"Saved to basics.json")


if __name__ == '__main__':
    main()
