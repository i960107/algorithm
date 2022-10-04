from collections import defaultdict

dp_mem = defaultdict(int)


def fibo_memoization(n: int) -> int:
    '''하향식 - 메모이제이션'''
    # 화이트보드 테스트로 자주 등장 -> 여러 번 반복해 완벽하게 숙지하기

    # 하위 문제에 대한 정답을 계산했는지 확인해가며 문제를 자연스럽게 재귀로 풀어나간다
    # 브루트 포스와 달리 이미 계산한 값은 저장해뒀다가 바로 return
    # 이미 계산한 값으 계산하지 않음

    # 값 할당이 여러번 일어남
    # dp = [None] * (n + 1)

    # 재귀 멈추는 조건 있어야함
    # dp_mem에 1과 0은 없음
    if n <= 1:
        return n

    # 확인할때마다 그 key의 쌍 생김(defaultdict)
    # dp_mem[0] = 0 일 수 있음 따로 체크 필요
    if dp_mem[n]:
        return dp_mem[n]

    # 하위 문제를 풀지 않았다면 하위 문제를 풀기
    # 꼭 값 삽입해주어야함
    dp_mem[n] = fibo_memoization(n - 2) + fibo_memoization(n - 1)

    return dp_mem[n]


def fibo_tabulation(n: int) -> int:
    '''상향식 - 타뷸레이션'''
    # 작은 하위 문제부터 문제를 풀어나가며 큰 문제의 정답을 만든다
    # 데이터를 테이블 형태로 만들면서 문제를 풀이
    dp = [None] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]


print(fibo_memoization(7))
print(fibo_tabulation(7))


def fibo_tabulation_improved(n: int) -> int:
    '''두 변수만 이용해 공간 절약'''
    # 공간복잡도 O(1)
    x, y = 0, 1
    for _ in range(2, n + 1):
        x, y = y, x + y
    return y


