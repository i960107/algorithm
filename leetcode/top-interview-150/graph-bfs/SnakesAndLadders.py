import heapq
from typing import List
from collections import deque


class Solution:
    # boutrophedon style. starting from bottom left and 위로 올라가는.
    # 최소 ㅂ칸에서 6칸 까지 이동
    # 시작칸이나 마지막칸에는 뱀, 사다리 없음.
    # 최소 이동 횟수, 최단거리.. -> bfs가 낫다
    # 사다리로 이동한 곳에 또다시 사다리나 뱀이 있다면 그곳은 무시한다.
    # 한번에 한칸 또는 여섯칸 움직일 수 있음
    # 뱀은 머리 끝과 끝만 가능.
    # 뱀과 사다리는 모두 유효한 인덱스만 가리킨다.
    # 못 도착하는 경우도 있따.
    # 사다리나 뱀이 자기자신에게 연결되는 경우 있나?
    # 사다리나 뱀은 양방향인가?
    # 방문했다고 방문체크를 하면 안됨?
    # 사다리나 뱀을 타고 이동한경우 방문체크를 하지 않는다? 거기가 사다리나 뱀인 경우 또 이동해야함.
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        for row in board:
            print(row)

        n = len(board)

        num = n * n
        d = dict()
        # 인덱스가 어려움..
        for i in range(n):
            # 작아지는
            if (n % 2 == 0 and i % 2 == 0) or (n % 2 == 1 and i % 2 == 1):
                for j in range(0, n, 1):
                    d[num] = board[i][j]
                    num -= 1
            # 커지는
            else:
                for j in range(n - 1, -1, -1):
                    d[num] = board[i][j]
                    num -= 1

        queue = deque()
        queue.append((1, 0))
        # 너비 우선 탐색에서 방문한 노드
        # 먼저 queue에서 빠지면 최단 거리임
        visited = set()
        visited.add(1)

        # 자신에서 연결된 사다리나 뱀이 있는지 확인하지 않아도 됨 -> 만나면 바로 이동한다.이동한 후에 다음 턴에서는 무시. 주사위 수만큼만 이동한다.
        # 사다리나 뱀을 이동하지 않는 경우도 있나? 무조건 이동해야함.
        # bfs에서 방문 처리 어디서 해줘야하는지에 따라서 최단거리 달라짐. heapq를 쓰든가 넣고 바로 방문처리 하든가?
        # 꼭 bfs라고 나중에 큐에 넣어진게 더 짧은 거리일 수 있다... 모든 경로를 탐색해야할듯?
        # 그럼 TLE가 발생하는데...
        # 이동하기 전 방문처리 안하면 됨?
        # 자기 자신에서 사다리가 있는 경우 이동하자.
        while queue:
            print(queue)
            index, dist = queue.popleft()
            if index == n * n:
                return dist

            for k in range(1, 6 + 1):
                if index + k > n * n or index + k in visited:
                    continue

                if d[index + k] == -1:

                    queue.append((index + k, dist + 1))
                    visited.add(index + k)
                # 이동
                else:
                    if d[index + k] in visited:
                        continue
                    visited.add(index + k)
                    queue.append((d[index + k], dist + 1))

        return -1


class Solution2:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        nboard = []
        n = len(board)
        '''this loop is to rearrange the board in 2D manner'''
        # 1차원 행렬로 만듦.
        for i in range(n - 1, -1, -1):
            if i % 2 != n % 2:
                for j in range(n):
                    nboard.append(board[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    nboard.append(board[i][j])

        # 재귀 아님..?
        visited = {1}
        q = [(1, 0)]
        while q:
            a = q.pop(0)
            for i in range(6):
                try:
                    if nboard[a[0] + i] == -1:
                        t = a[0] + i + 1
                    else:
                        t = nboard[a[0] + i]
                except:
                    break
                if t in visited:
                    continue
                visited.add(t)
                print(a[0], t, a[1] + 1)
                if t == n * n:
                    return a[1] + 1
                q.append((t, a[1] + 1))
        return -1


s = Solution()
# print(s.snakesAndLadders(
#     board=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
#            [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
#
# print(s.snakesAndLadders(board=[[-1, -1], [-1, 3]]))
# print(s.snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))
# print(s.snakesAndLadders([[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]))
# print(s.snakesAndLadders([[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]))
# print(s.snakesAndLadders([[-1, 1, 1, 1], [-1, 7, 1, 1], [1, 1, 1, 1], [-1, 1, 9, 1]]))
# print(s.snakesAndLaddersReverse([[-1, 1, 1, 1], [-1, 7, 1, 1], [1, 1, 1, 1], [-1, 1, 9, 1]]))
# print(s.snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))
s2 = Solution2()
print(s2.snakesAndLadders(
    [[-1, -1, -1, 46, 47, -1, -1, -1], [51, -1, -1, 63, -1, 31, 21, -1], [-1, -1, 26, -1, -1, 38, -1, -1],
     [-1, -1, 11, -1, 14, 23, 56, 57], [11, -1, -1, -1, 49, 36, -1, 48], [-1, -1, -1, 33, 56, -1, 57, 21],
     [-1, -1, -1, -1, -1, -1, 2, -1], [-1, -1, -1, 8, 3, -1, 6, 56]]))
# #
