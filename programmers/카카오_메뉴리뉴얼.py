from typing import List
from collections import Counter
from itertools import combinations


def get_new_course(orders: List[str], course: List[int]) -> List[str]:
    candidates = dict()

    for order in orders:
        for c in course:
            course_candidates = candidates.get(c, Counter())
            course_candidates.update(''.join(sorted(x)) for x in combinations(order, c))
            candidates[c] = course_candidates

    answer = []
    for c in candidates:
        if not candidates[c]:
            continue
        candidates[c] = sorted(candidates[c].items(), key=lambda x: (-x[1]))

        picked = candidates[c][0][1]

        if picked < 2:
            continue

        for candidate in candidates[c]:
            if candidate[1] == picked:
                answer.append(candidate[0])
            else:
                break

    return sorted(answer)


print(get_new_course(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(get_new_course(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(get_new_course(["XYZ", "XWY", "WXA"], [2, 3, 4]))
