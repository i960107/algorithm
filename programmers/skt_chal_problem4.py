def solution(n: int, edges: list) -> int:
    # 하나 이상의 노드를 거쳐 연결된 개수
    # 완전 탐색?
    # 트리로 만드는 건 node 의 개수가 최대 300,000개이기 때문에 불가능
    # 동적 프로그래밍? 연결된 것
    return 0


print(solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))
print(solution(4, [[2, 3], [0, 1], [1, 2]]))
