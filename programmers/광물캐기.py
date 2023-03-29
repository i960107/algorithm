from typing import List
from collections import deque


def solution(picks: List[int], minerals: List[str]) -> int:
    # 곡갱이의 수가 모자란 경우는 없나..?
    # 곡괭이의 수가 모자란 경우 못 캐는 광물은 미리 빼주기
    # 남아있는 minerals의 모든 광물 캘 수 있음
    group_elements = 5
    if sum(picks) * group_elements < len(minerals):
        for _ in range(len(minerals) - (sum(picks) * group_elements)):
            minerals.pop()
    # 더 약한 광물을 더 센 곡괭이로 쳐야하는 경우 없나?
    n = len(minerals)
    multiple = 5

    elements = {
        "diamond": 25,
        "iron": 5,
        "stone": 1
    }

    # 곡괭이가 남는 경우 있을 수도 -> 큰 곡괭이부터 사용
    # pick_tools = deque(["diamond"] * picks[0] + ["iron"] * picks[1] + ["stone"] * picks[2])
    # 최소한의 피로도
    # 같은 강도를 가졌는데 다르게 캐야할 수 있음.
    groups = []
    for i in range(0, len(minerals), group_elements):
        group_sum = 0
        group = []
        for count in range(group_elements):
            if i + count >= n:
                break
            mineral = minerals[i + count]
            group.append(elements[mineral])
            group_sum += elements[mineral]
        groups.append((group_sum, group))

    # 마지막 그룹의 경우 원소의 개수 < group element일 수 있지만 맨 앞에서 조정해주었기 때문에 순서만 정하면 됨.
    groups.sort()
    total_fatigue = 0
    # 곡괭이가 남는 경우 있을 수 있음
    for pick_name, pick_count in zip(("diamond", "iron", "stone"), picks):
        pick_intensity = elements[pick_name]
        for _ in range(pick_count):
            fatigue = 0
            if not groups:
                break
            _, group = groups.pop()
            for mineral_intensity in group:
                if mineral_intensity >= pick_intensity:
                    fatigue += (mineral_intensity // pick_intensity)
                else:
                    fatigue += 1
            total_fatigue += fatigue
    return total_fatigue

    # 등수
    # 처음 부터 파야함!
    # 팔 수 있는 광물의 개수는 min(곡괭이의 개수 * 5, )
    # intensity_ranks = [0] * ((n // group_elements) + 1)
    # for rank, (x, i) in enumerate(sorted([(x, i) for i, x in enumerate(intensities)], reverse=True)):
    #     intensity_ranks[rank] = i
    #
    # total_fatigue = 0
    # for group in intensity_ranks:
    #     start_index = group_elements * group
    #     fatigue = 0
    #     if len(pick_tools) == 0:
    #         break
    #     pick_tool_intensity = elements[pick_tools.popleft()]
    #     for count in range(group_elements):
    #         if start_index + count >= n:
    #             break
    #         mineral_intensity = elements[minerals[start_index + count]]
    #         fatigue += multiple ** (
    #             mineral_intensity - pick_tool_intensity if pick_tool_intensity <= mineral_intensity else 0)
    #     total_fatigue += fatigue
    #
    # return total_fatigue


def solution_dfs(picks: List[int], minerals: List[str]) -> int:
    intensity = {
        "diamond": 3,
        "iron": 2,
        "stone": 1,

    }

    def dfs(left_picks: List[int], now: int, fatigue: int):
        if now >= len(minerals) or sum(left_picks) == 0:
            nonlocal min_fatigue
            if min_fatigue > fatigue:
                min_fatigue = fatigue
            return
        for pick_index, pick in enumerate(("diamond", "iron", "stone")):
            if left_picks[pick_index] == 0:
                continue
            nxt_fatigue = fatigue
            index = now
            for _ in range(5):
                if index >= len(minerals):
                    break
                pick_intensity = intensity[pick]
                mineral_intensity = intensity[minerals[index]]
                if pick_intensity >= mineral_intensity:
                    nxt_fatigue += 1
                else:
                    nxt_fatigue += 5 ** (mineral_intensity - pick_intensity)
                index += 1

            nxt_left_picks = left_picks[::]
            nxt_left_picks[pick_index] -= 1
            dfs(nxt_left_picks, index, nxt_fatigue)

    min_fatigue = int(1e9)
    dfs(picks, 0, 0)
    return min_fatigue


print(solution_dfs([0, 1, 1],
                   ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron",
                    "diamond"]))

print(solution_dfs([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
