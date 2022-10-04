import sys
import heapq
from typing import List


# 메모리 제한이 타 문제보다 확연히 적음.
def solution():
    '''stack 풀이'''
    input = sys.stdin.readline
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    for col in range(n):
        for row, num in enumerate(map(int, input().split())):
            arr[row][col] = num

    ans = None
    for _ in range(n):
        max_num, max_row = float("-inf"), float("-inf")
        for row in range(n):
            if arr[row] and arr[row][-1] > max_num:
                max_num, max_row = arr[row][-1], row
        ans = arr[max_row].pop()
    print(ans)


def solution2():
    hq = []
    n = int(input())
    for _ in range(n):
        for i in map(int, input().split()):
            # 우선순위 큐의 크기를 n으로 유지하면 언제나 1~n번째 큰 수들만 알 수 있음.
            if len(hq) >= n:
                heapq.heappushpop(hq, i)
            else:
                heapq.heappush(hq, i)

    print(heapq.heappop(hq))


def test(arr: List[List[int]]) -> int:
    manipulated_arr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr))]

    for k in range(1, len(arr) +1):
        max_i = 0
        for i in range(len(arr)):
            if manipulated_arr[max_i][-1] < manipulated_arr[i][-1]:
                max_i = i
        res = manipulated_arr[max_i].pop()
        if k == len(arr):
            return res


res = test([[12, 7, 9, 15, 5], [13, 8, 11, 18, 5], [21, 10, 26, 31, 16], [48, 14, 28, 35, 25], [52, 20, 32, 41, 49]])
print(res, res == 35)
