from typing import List, Final


class SolutionA:
    EMPTY: Final = -1

    def __init__(self, n: int, profits: List[int]):
        self.n = n
        self.profits = profits
        self.memo = [[self.EMPTY] * 3 for _ in range(n)]

    # last_index 날에 연속으로 c번째 근무 한다면 얻을 수 있는 최대 인센티브
    def get_maximum_incentive(self, last_index: int, count: int) -> int:
        if last_index < 0:
            return 0
        elif self.memo[last_index][count] != self.EMPTY:
            return self.memo[last_index][count]

        # CASE1:last_index날에 근무하지 않고 얻을 수 있는 최대 인센티브
        # 이전 날까지 얻을 수 있는 최대 인센티브(0, 1, 2일 연속 근무하는 모든 경우 포함)
        if count == 0:
            answer = max(self.get_maximum_incentive(last_index - 1, 0),
                         self.get_maximum_incentive(last_index - 1, 1),
                         self.get_maximum_incentive(last_index - 1, 2),
                         )

        # CASE2:last_index날에 근무하고 얻을 수 있는 최대 인센티브
        else:
            answer = self.get_maximum_incentive(last_index - 1, count - 1) + self.profits[last_index]

        self.memo[last_index][count] = answer

        return answer


class SolutionB:
    EMPTY: Final = -1

    def __init__(self, n: int, profits: List[int]):
        self.n = n
        self.profits = profits
        self.memo = [self.EMPTY] * n

    # last_index 날에 마지막으로 근무 했을때 얻을 수 있는 최대 인센티브
    def get_maximum_incentive(self, last_index: int) -> int:

        if last_index < 0:
            return 0

        elif last_index == 0:
            self.memo[0] = self.profits[0]
            return self.profits[0]

        elif self.memo[last_index] != self.EMPTY:
            return self.memo[last_index]

        # case 1: 이틀전에 마지막으로 근무했다면, 어제는 근무하지 않고 오늘 근무
        # case 2: 사흘전에 마지막으로 근무했다면, 어제 근무하고 오늘 근무
        answer = max(self.get_maximum_incentive(last_index - 2),
                     self.get_maximum_incentive(last_index - 3) + self.profits[last_index - 1]) \
                 + profits[last_index]

        self.memo[last_index] = answer
        return answer


n = int(input())
profits = list(map(int, input().split()))

# 방법 1
# n-1날까지 0,1,2일 연속 근무한 각각의 경우에 얻을 수 있는 최대 인센티브 중 최댓값이 정답

a = SolutionA(n, profits)

res = max(a.get_maximum_incentive(n - 1, 0),
          a.get_maximum_incentive(n - 1, 1),
          a.get_maximum_incentive(n - 1, 2)
          )
print(res)

# 방법 2
# 0 ~ n-1 각 날까지 근무했을때 얻을 수 있는 최대 인센티브 중 최대 값이 정답

b = SolutionB(n, profits)
for last_index in range(n):
    res = max(res, b.get_maximum_incentive(last_index))

print(res)
