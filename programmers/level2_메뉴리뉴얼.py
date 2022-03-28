from typing import List
from itertools import combinations


def solution_menu_renewal(orders: List[str], course: List[int]) -> List[str]:
    answer = []
    d = {}
    for order in orders:
        # combination 구한후 정렬하면 여러번 정렬필요. 정렬 후 조합 구하면 정렬된 결과
        order = sorted(menu for menu in order)
        for i in range(2, len(order) + 1):
            for combi in combinations(order, i):
                combi = ''.join(combi)
                cnt = dict(d.get(i, {})).get(combi, 0) + 1
                if i not in d:
                    d[i] = {}
                d[i][combi] = cnt

    for cnt in course:
        sorted_order = sorted(d.get(cnt, {}).items(), key=lambda x: x[1], reverse=True)
        answer += [menu for menu, picked in sorted_order if picked == sorted_order[0][1] and picked >= 2]
    return sorted(answer)


print(solution_menu_renewal(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution_menu_renewal(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution_menu_renewal(["XYZ", "XWY", "WXA"], [2, 3, 4]))
