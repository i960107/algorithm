import sys, heapq
from typing import List


def solution():
    abs_h = []
    # N이 10만이므로 빠른 입력함수 사용해야
    input = sys.stdin.readline
    for _ in range(int(input())):
        curr = int(input())
        if curr:
            heapq.heappush(abs_h, (abs(curr), curr))
        else:
            print(heapq.heappop(abs_h)[1]) if abs_h else print('0')


def solution2():
    '''양수는 최소힙에 음수는 최대힙에 절대값을 넣음'''
    min_h = []
    max_h = []
    # N이 10만이므로 빠른 입력함수 사용해야
    input = sys.stdin.readline
    for _ in range(int(input())):
        curr = int(input())
        if curr > 0:
            heapq.heappush(min_h, curr)
        elif curr < 0:
            heapq.heappush(max_h, -curr)
        else:
            if min_h:
                # min_h, max_h 둘다 존재하는 경우 크기 비교 3가지
                # 둘중 하나 없는 경우 2가지
                if not max_h or min_h[0] < max_h[0]:
                    print(heapq.heappop(min_h))
                else:
                    print(-heapq.heappop(max_h))
            else:
                print(-heapq.heappop(max_h) if max_h else 0)


res = solution2([1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0])
print(res, res == [-1, 1, 0, -1, -1, 1, 1, -2, 2, 0])
