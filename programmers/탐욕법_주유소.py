from typing import List


def solution(gas: List[int], cost: List[int]) -> int:
    # O(N^2) -> time limite excceded
    tank = 0

    for start in range(len(gas)):
        # len(gas) -1 까지 아니라 len(gas)까지 검사해야함 -> circular이기 때
        for i in range(len(gas)):

            tank += gas[(i + start) % len(gas)]
            tank -= cost[(i + start) % len(gas)]
            if tank < 0:
                break
                #
        else:
            return start
        tank = 0
    else:
        return -1


# when used in a type hint, the expression none is considered equivalent to type(none)
def solution_test(gas: List[int], cost: List[int]) -> int:
    subtract = [gas[i] - cost[i] for i in range(len(gas))]
    if sum(subtract) < 0:
        return -1

    answer = 0
    for j in range(len(gas)):
        if subtract[j] >= 0:
            answer = j
            break
    return answer

    # def solution_(gas: List[int], cost: List[int]) -> None:


def solution_can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    # 모든 주유소 방문 가능 여부 판별
    # 전체 기름의 양이 전체 비용보다 클 경우 반드시 전체를 방문할 수 있다?
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    # 따라서 전체를 방문하면서 성립되지 않는 경우는 출발점을 한 칸씩 뒤로 밀어낸다
    # 성립되지 않는 지점이 있다면 그 앞은 전부 출발점이 될 수 없다. (성립 안되는 경우 무조건 한 번 이상 존재)
    for i in range(len(gas)):
        # 출발점이 안되는 지점 판별
        # 현재 탱크에 남아있는 기름에서 충전한다음 다음 지점으로 갈 수 없을때
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            # 현재 지점에서 다음지점으로 이동하고 남은 기름을 더해주기
            fuel += gas[i] - cost[i]
    return start


print(solution_can_complete_circuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])) #3
print(solution_can_complete_circuit(gas=[2, 3, 4], cost=[3, 4, 3])) # -1
print(solution_can_complete_circuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1])) #4
print(solution_can_complete_circuit(gas=[3, 1, 1], cost=[1, 2, 2])) #0
