from typing import List, Set
from collections import defaultdict
from collections import deque


def solution_fail(n: int, prerequisites: List[List[int]]) -> bool:
    d = defaultdict(list)
    # prerequisites에 명시되어있지 않으면 가능
    for c1, c2 in prerequisites:
        d[c1].append(c2)

    def dfs(i, path: List[int]):
        if len(path) == n:
            return True
        # prerequisite 다 수강했는지 확인
        if d[i]:
            for pre in d[i]:
                if pre not in path:
                    return False
        # 다음으로 뭘 들어야하지?
        for j in range(n):
            if j not in path:
                dfs(j, path + [i])

    for i in range(n):
        if dfs(i, []):
            return True

    return False


# 시간 매우 오래걸림
def solution(n: int, prerequisites: List[List[int]]) -> bool:
    '''DFS로 순환 구조 판별'''
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    # 이미 방문했던 노드를 저장. 중복 방문하게 된다면 순환 구조임.
    traced = set()

    def dfs(i):
        # 순환 구조이면 false?
        # 언제 순환 참조 확인이 끝났다고 할 수 있지?
        # if len(visited) == len(d): return True
        # 특별히 확인하지 않음 깊이 우선 탐색이 return False하지 않고 끝냈다면 True

        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 탐색. 그렇지 않으면 형제 노드가 방문한 노드까지 남게 됨
        traced.remove(i)

        return True

    # n개의 코스내 모든 순열에 대해서 prerequisite 만족하면서 전체 과목 수강가능하지 확인 X
    # prerequisite이 순환 형태인지 확인
    # dictionary changed size during iteration. graph를 defaultdict에서 분리해서 고정시킬 필요가 있다. 새로운 복사본을 만듬.
    # prerequisite의 끝을 찾아 들어간다
    # 매 회마다 set()을 생성한다.. 아님. sibling사이의 중복은 괜찮음!. 형제 노드간 서로 관련성이 없어야 한다.
    # [[0,1],[0,1],[1,2]]일때 이 그래프는 순환이 존재하지 않음.
    # 존재하지 않는 키를 조회할때 graph값이 변경된다. prerequisite을 따라가는데 더이상 prerequisite이 없을때 graph에 key가 없어서
    # 새로 생성됨.
    for x in list(graph):
        if not dfs(x):
            return False

    return True


def solution2(n: int, prerequisites: List[List[int]]) -> bool:
    '''가지치기를 이용한 최적화'''
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    # 이미 방문했던 노드를 저장. 중복 방문하게 된다면 순환 구조임.
    traced = set()
    # 한번 방문했던 그래프는 두 번 이상 방문하지 않도록 무조건 true로 return.
    # 이미 방문한 그래프라면 True가 증명되어있음
    visited = set()

    def dfs(i):
        # 순환 구조이면 false?
        if i in traced:
            return False

        # 이미 방문했던 노드이면 True
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 탐색. 그렇지 않으면 형제 노드가 방문한 노드까지 남게 됨
        traced.remove(i)
        visited.add(i)

        return True

    # n개의 코스내 모든 순열에 대해서 prerequisite 만족하면서 전체 과목 수강가능하지 확인 X
    # prerequisite이 순환 형태인지 확인
    for x in list(graph):
        if not dfs(x):
            return False

    return True


def solution3(n: int, prerequisites: List[List[int]]) -> bool:
    ''' kahn's algorithm'''
    graph = defaultdict(list)
    # 선행 과목 수
    indegrees = [0] * n

    # key를 선행과목으로 들어야하는 과목들 = value
    for i, j in prerequisites:
        graph[j].append(i)
        indegrees[i] += 1

    # 선행 과목이 없는 과목
    q = deque()

    for i, degree in enumerate(indegrees):
        if indegrees == 0:
            q.append(i)

    topo_count = 0

    while q:
        node = q.popleft()
        topo_count += 1
        # 선행 과목이 없는 괌고을 선행과목으로 하는 node들 탐색
        for child in graph[node]:

            indegrees[child] -=1

            if indegrees[child] == 0:
                q.append(child)

    return True if topo_count == n else False


print(solution(2, [[1, 0]]))
print(solution(2, [[1, 0], [0, 1]]))
print(solution(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
# time exceed error
print(solution(100,
               [[1, 0], [2, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [5, 3], [5, 4], [6, 4], [6, 5], [7, 5],
                [7, 6],
                [8, 6],
                [8, 7], [9, 7], [9, 8], [10, 8], [10, 9], [11, 9], [11, 10], [12, 10], [12, 11], [13, 11],
                [13, 12],
                [14, 12],
                [14, 13], [15, 13], [15, 14], [16, 14], [16, 15], [17, 15], [17, 16], [18, 16], [18, 17],
                [19, 17],
                [19, 18],
                [20, 18], [20, 19], [21, 19], [21, 20], [22, 20], [22, 21], [23, 21], [23, 22], [24, 22],
                [24, 23],
                [25, 23],
                [25, 24], [26, 24], [26, 25], [27, 25], [27, 26], [28, 26], [28, 27], [29, 27], [29, 28],
                [30, 28],
                [30, 29],
                [31, 29], [31, 30], [32, 30], [32, 31], [33, 31], [33, 32], [34, 32], [34, 33], [35, 33],
                [35, 34],
                [36, 34],
                [36, 35], [37, 35], [37, 36], [38, 36], [38, 37], [39, 37], [39, 38], [40, 38], [40, 39],
                [41, 39],
                [41, 40],
                [42, 40], [42, 41], [43, 41], [43, 42], [44, 42], [44, 43], [45, 43], [45, 44], [46, 44],
                [46, 45],
                [47, 45],
                [47, 46], [48, 46], [48, 47], [49, 47], [49, 48], [50, 48], [50, 49], [51, 49], [51, 50],
                [52, 50],
                [52, 51],
                [53, 51], [53, 52], [54, 52], [54, 53], [55, 53], [55, 54], [56, 54], [56, 55], [57, 55],
                [57, 56],
                [58, 56],
                [58, 57], [59, 57], [59, 58], [60, 58], [60, 59], [61, 59], [61, 60], [62, 60], [62, 61],
                [63, 61],
                [63, 62],
                [64, 62], [64, 63], [65, 63], [65, 64], [66, 64], [66, 65], [67, 65], [67, 66], [68, 66],
                [68, 67],
                [69, 67],
                [69, 68], [70, 68], [70, 69], [71, 69], [71, 70], [72, 70], [72, 71], [73, 71], [73, 72],
                [74, 72],
                [74, 73],
                [75, 73], [75, 74], [76, 74], [76, 75], [77, 75], [77, 76], [78, 76], [78, 77], [79, 77],
                [79, 78],
                [80, 78],
                [80, 79], [81, 79], [81, 80], [82, 80], [82, 81], [83, 81], [83, 82], [84, 82], [84, 83],
                [85, 83],
                [85, 84],
                [86, 84], [86, 85], [87, 85], [87, 86], [88, 86], [88, 87], [89, 87], [89, 88], [90, 88],
                [90, 89],
                [91, 89],
                [91, 90], [92, 90], [92, 91], [93, 91], [93, 92], [94, 92], [94, 93], [95, 93], [95, 94],
                [96, 94],
                [96, 95],
                [97, 95], [97, 96], [98, 96], [98, 97], [99, 97]]))

print(solution(2, [[1, 0]]))
print(solution(2, [[1, 0], [0, 1]]))
