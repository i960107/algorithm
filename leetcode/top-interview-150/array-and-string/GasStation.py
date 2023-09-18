from typing import List


class Solution:
    # unlimited gas tank
    # clockwise direction
    # 갈 수 없는 경우도 존재
    # 가능한 경우 1가지만 존재. 출발점은 유일하다
    # 10 ^ 5 -> 선형 탐색 가능.
    # 시작한 곳으로 돌아와야함.
    # cost 가 안 들 수 도 있음
    # 모든 주유소를 방문할 수 있는 인덱스를 출력하는 것.
    def canCompleteCircuitFail(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # brute force, 전체 circle을 돌면서 비용이 가스를 초과하는 경우가 없는지 체크하는 것
        # O(N^2) TLE 발생
        for start in range(n):
            tank = 0
            for k in range(n):
                tank += gas[(start + k) % n]
                tank -= cost[(start + k) % n]
                if tank < 0:
                    break
            if tank >= 0:
                return start
        return - 1

    # 전체 기름의 양이 전체 비용보다 큰 경우 반드시 전체를 방문할 수 있는 출발점이 존재한다.
    # 성립되지 않는 지점이 있다면 그 앞은 전부 출발점이 될 수 없다.
    # 성립되지 않는 지점을 출발점에서 제외한다.
    # greedy
    # 마지막으로 start에 저장되어있는 인덱스부터는 비용이 모자르지 않는다.
    # 어려운 문제 unique함. 직관적으로 이해하기 어려움
    # diff >= 0인 분에서 출발할 수 있음. 그 이후 누적값이 < 0이 되지 않아야한다.
    # 왜 greedy인가? 누적 diff >= 0인 부분만 선택한다.
    # array끝에 도달하면 다시 인덱스 0으로 가서 확인하지 않아도 된다.
    # 이미 sum을 체크해서 가능한 값이 있다는 것을 확인했고,값은 하나. 누적값이 매번 >0 이상이었다면 가장 빠른 인덱스에서 누적된 가스가 가장 많으므로
    # 이후에 더 많은 가스를 사용할 수 있게 됨.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 이전에서 누적되어온 fuel 합쳐서 이동할 수 없는 경우
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(s.canCompleteCircuit([3], [4]))
print(s.canCompleteCircuit([0], [0]))
print(s.canCompleteCircuit([0, 0, 0, 2], [0, 0, 1, 0]))
