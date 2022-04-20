from typing import List
from collections import defaultdict


def solution_fail(tickets: List[List[str]]) -> List[str]:
    d = defaultdict(list)
    # 인접 리스트 그래프로 재구성
    for start, end in tickets:
        d[start].append(end)

    # 매 value에 대해 정렬하지 않고 tickets자체를 정렬하면 d에 삽입되는 순서가 정렬된 순서임.
    for value in d.values():
        value.sort()

    def dfs(d: dict, start: str, path: List[str]) -> List[str]:
        if len(path) == len(d):
            return path

        path.append(start)
        for arrive in d[start]:
            # 중복 가능함!d.copy()로 deepcopy가능한가?
            new_d = d.copy()
            new_d[start].remove(arrive)
            dfs(new_d, arrive, path)
        path.pop()

    answer = []
    for start in d:
        answer = dfs(d, start, [])
    return answer


def solution(tickets: List[List[str]]) -> List[str]:
    # 출발지 정해져있고, 무조건 모든 경로 한번씩 거침. 해밀턴 경로
    '''DFS로 일정 그래프 구성'''
    graph = defaultdict(list)
    # 그래프를 뒤집어서 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    route = []

    def dfs(a):
        # 마지막 값을 읽어 어휘 순 방문?
        while graph[a]:
            # d에서 pop하기 때문에 해당 경로는 사라지게 되어 재방문하지 않음.
            # queue의 연산을 수행
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    # 왜 뒤집어서 ? 재귀 호출 끝나는 순으로 즉(마지막에 방문한 공항일수록 먼저 route에 추가됨)
    return route[::-1]


def solution_queue(tickets: List[List[str]]) -> List[str]:
    '''스택연산으로 최적화 시도'''
    # 정렬 순서
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a: str):
        while graph[a]:
            # 뒤에서부터 pop() O(1) 복잡도
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')

    return route[::-1]


def solution_iterative(tickets: List[List[str]]) -> List[str]:
    '''일정 그래프 재귀아닌 반복 풀이'''
    route = []
    stack = ['JFK']

    graph = defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    # 모든 경로 방문하고 나면 모든 value가 빈배열이 됨
    # 방문한 경로가 불가능한 경우도 있음. 재귀에서는 왜 체크 안해도 되지?
    # 끊기는 경우 이상한 답 나옴
    # 탐색에 실패하면 맨 마지막에 방문?
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    # 다시 뒤집기 필요
    return route[::-1]





print(solution(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
print(solution(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# # 끊기는 경우 있을 수 있음?
print(solution(tickets=[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
print(solution_iterative(tickets=[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
