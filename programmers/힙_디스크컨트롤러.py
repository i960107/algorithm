from typing import List
import heapq
from collections import deque


# def solution(jobs: List[List[int]]) -> int:
#     n = len(jobs)
#     # 현재 디스크가 작업 중이 아닐때 실행할 작업의 우선순위
#     # 현재 가능(요청 시간 <= 현재시간) 작업 중 가장 빨리 끝나는 작업.
#     jobs.sort()
#     # 작업이 끝나는 시간, 작업 번호
#     queue = [(jobs[0][1] - jobs[0][0], jobs[0][0], jobs[0][0] + jobs[0][1], 0)]
#
#     # 처리한 작업을 어떻게 표시하지.
#     done = set()
#     total_time = 0
#
#     t = 0
#     while queue:
#         response_time, start, end, now = heapq.heappop(queue)
#
#         if now in done or start < t:
#             continue
#
#         done.add(now)
#
#         total_time += response_time
#         t = end
#
#         for nxt in range(n):
#             nxt_requested_at, nxt_cost = jobs[nxt]
#
#             if nxt_requested_at > t:
#                 break
#
#             nxt_end = end + nxt_cost
#             nxt_response_time = nxt_end - nxt_requested_at
#
#             # 가장 짧은 작업만 넣어주기
#             heapq.heappush(queue, (nxt_response_time, end, nxt_end, nxt))
#
#     return total_time // n


def solution_fail(jobs: List[List[int]]) -> int:
    jobs.sort()
    idx = 0

    n = len(jobs)
    total_response_time = 0
    t = 0

    queue = []
    while idx < n:
        # 현재 시간에 들어온 요청이 있다면 queue에 넣어주기
        # 매번 jobs들을 선형탐색해야 햐나?
        # jobs에서 빠진 애들을 어떻게 처리하지..
        # 요청부터 종료까지 걸린 시간이 작은 순서대로 heapq에서 빼기 위해서는?
        # 현재 시간에서 가장 멀리떨어진 요청시간이 가장
        # 요청시간 걸리는 시간

        # 종료시간을 기준으로 종료될 수 있는 작업들 중 가장 요청시간이 빠른 것을 고른다..?
        # 우선순위 큐에 있는 것들 중
        # 처음 아니고 중간에도 우선순위 큐가 빌 수 있음... -> 요청시간이 가장 빠른 것이 먼저 실행되도록 어떻게 하지..
        # 현재 시간을 기준으로 끝날 수 있는 작업을 큐에 넣고...나ㅓ라너란더ㅏ

        now = idx
        for request in range(now, n):
            requested, duration = jobs[request]
            if requested > t:
                break
            heapq.heappush(queue, (- (duration - requested), duration))
            idx += 1

        # 요청부터 종료까지 걸리시간  t + duration - requested
        # response_time이 긴 것 먼저 처리해야함.
        # duration 높고, requested 작은 것. 하지만 둘 사이에 우선수위 없음. duration - requested의 차이 큰것
        if queue:
            difference, duration = heapq.heappop(queue)
            response_time = (t - difference)
            total_response_time += response_time
            t += duration
        else:
            t += 1
    return total_response_time // n


def solution(jobs: List[List[int]]) -> int:
    # 전체 응답시간의 합, 현재 시간, 처리된 job의 개수?
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    n = len(jobs)
    while i < len(jobs):
        for requested, duration in jobs:
            if start < requested <= now:
                # 왜 응답시간이 아닌 처리시간을 기준으로 우선순위를 매기지?
                # 중복해서 들어갈 수 있지 않나?
                # 실행중인 작업이 없을때 가장 먼저 요청이 들어온 것부터 실행되나?
                heapq.heappush(heap, (duration, requested))

        if heap:
            duration, requested = heapq.heappop(heap)
            start = now
            now += duration
            answer += (now - requested)
            i += 1
        else:
            now += 1
    return answer // n


print(solution_fail([[0, 3], [1, 9], [2, 6]]))
