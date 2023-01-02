from itertools import combinations

'''소수경로'''


def solution(num1: int, num2: int) -> int:
    # 총 4*3*2*1 = 24가지의 경우의 수
    # 어떻게 조합을 관리할까. -> combinations? set?
    # for combi in combinations(range(4), 4):
    #     print(combi)
    # (0,1,2,3) 1가지의 경우만 출력됨.
    return 0


n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    print(solution(num1, num2))
