from typing import List
from collections import defaultdict

keyboard_str = ["가호저론남드부이프설",
                "알크청울키초트을배주",
                "개캠산대단지역구너양",
                "라로권교마쿼파송차타",
                "코불레뉴 서한산리개",
                "터강봄토캠상호론운삼",
                "보람이경아두프바트정",
                "스웨어쿼일소라가나도",
                "판자비우사거왕태요품",
                "안배차캐민광재봇북하"]
keyboard = [list(x) for x in keyboard_str]


def solution1(word: str) -> List[int]:
    d = defaultdict(list)

    for i in range(len(keyboard[0])):
        for j in range(len(keyboard)):
            d[keyboard[j][i]].append([i, j])

    prev = []
    total_distance = 0
    count = 0

    for ch in word:

        if d[ch]:

            # 이전 글자도 있고 현재 글자도 있는 경우
            if prev:

                if prev == ch:
                    count += 1
                    continue

                dist = len(keyboard) + len(keyboard[0])  # 최소 거리 구하기 위해서 불가능한 값으로 초기화
                curr = [-1, -1]

                # 더 가까운 글자 찾기
                for i, j in d[ch]:

                    cur_dist = abs(prev[0] - i) + abs(prev[1] - j)

                    if cur_dist < dist:
                        dist = cur_dist
                        curr[0], curr[1] = i, j

                    elif cur_dist == dist:
                        if i < curr[0] or (i >= curr[0] and j < curr[1]):
                            curr[0], curr[1] = i, j

                total_distance += dist
                prev[0], prev[1] = curr[0], curr[1]
                count += 1

            # 현재 글자는 있지만 이전 글자가 없는 경우
            else:
                prev = d[ch][0]

        else:
            # 현재 글자가 없는 글자인 경우
            total_distance += 20
            count += 1
            prev = []

    return [total_distance, count]


print("부스트캠프", solution1("부스트캠프"))
print("부슈트캠프", solution1("부슈트캠프"))
print("불레뉴캠프", solution1("불레뉴캠프"))
#  단어가 없는 경우 -> 거리 계산 불가. 없는 글자 규칙
print("뉴$솔레어", solution1("뉴$솔레어"))
#
print("뉴뉴", solution1("뉴뉴"))

