from typing import List


# from bisect import bisect_right


# def solution(required: int, possible: List[int]) -> int:
#     possible.sort()
#
#     for h in range(possible[-1], 0, -1):
#         # 삽입할 위치. 일치하는 값이 없다면 x 보다 큰 수 중 최소값의 인덱스
#         pos = bisect_right(possible, h)
#         # 얻게 되는 떡의 길이 구하기 각 떡 당 최소로 얻을 수 있는 떡의 길이
#         get = (possible[pos + 1] if pos < len(possible) - 1 else possible[-1] - h) * (len(possible) - 1 - pos)
#         print(h, pos, possible[pos] if pos < len(possible) else 0, get)
#         if get >= required:
#             return get
#
#
# def solution2(required: int, arr: List[int]) -> int:
#     answer = 0
#     # 떡을 정렬할 필요 없음. 높이는 0에서 최대 원소까지
#     start, end = 0, max(arr)
#
#     while start <= end:
#
#         tot = 0
#         mid = start + (end - start) // 2
#         for x in arr:
#             if x > mid:
#                 tot += (x - mid)
#
#         if tot < required:
#             end = mid - 1
#         else:
#             answer = mid
#             start = mid + 1
#     return answer


# res = solution(6, [19, 15, 10, 17])
# print(res, res == 15)

def solution(n: int, m: int, cakes: List[int]) -> int:
    lo, hi = 0, max(cakes)

    answer = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        cut_cakes = get_cut_cakes(mid, cakes)

        if cut_cakes < m:
            hi = mid - 1

        else:
            lo = mid + 1
            answer = mid

    return answer


def get_cut_cakes(h: int, cakes: List[int]) -> int:
    return sum([x - h for x in cakes if x >= h])


print(solution(4, 6, [19, 15, 10, 17]))
