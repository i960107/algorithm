from sys import stdin


def solution_timeout(n: int) -> int:
    answer = 0
    # O(N^2) 아닌 O(N)
    for i in range(1, n + 1):
        count = 0
        for j in range(i, n + 1, i):
            count += 1
        answer += (i * count)
    return answer


max = 1000000
dp = [1] * (max + 1)
# 누적합
s = [0] * (max + 1)

# O( NlogN)
# 이게 dp값 맞음? 그냥 약수의 합을 기록한 거 아님?
for i in range(2, max + 1):
    for j in range(i, max + 1, i):
        dp[j] += i

# 누적합을 활용하는 문제는 아닌듯.
for i in range(1, max + 1):
    s[i] = s[i - 1] + dp[i]

read = stdin.readline
# 여러개 숫자에 대해서 계산함으로 하나의 배열 재활용
T = int(input())

for _ in range(T):
    N = int(read())
    print(s[N])
