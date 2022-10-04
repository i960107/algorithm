import math
from typing import List


def solution(alp: int, cop: int, problems: List[List[int]]) -> int:
    # 필요한 알고력,코딩력 오름차순 보상 알고력 코딩력 내림차순
    # 단순히 보상이 크다고 좋은게 아님 단위시간당으로 따져야함. 정렬할때 보상 고려할 필요 없음
    problems.sort(key=lambda x: (x[0], x[1]))
    # 단위 시간당 보상을 기록해둠 매범 계산하지 않도록
    problem_unit_cost = []

    # pointer 이전(포함 안함)까지의 문제는 풀 수 있음
    threshold = 0
    # 현재 풀수 있는 문제들 중 가장 시간이 적게 들면서 다음문제까지 필요한 알고력, 코딩력을 채울 수 있는 방법을 택해야함.
    cost = 0
    while threshold < len(problems):
        required_alp = problems[threshold][0] - alp
        required_cop = problems[threshold][1] - cop

        if required_alp <= 0 and required_cop <= 0:
            problem_unit_cost.append(
                [problems[threshold][2] / problems[threshold][4],
                 problems[threshold][3] / problems[threshold][4]])
            threshold += 1

        else:
            # 문제를 풀지않고 필요한만큼 알고,코딩력 높이는데 드는 시간
            min_cost = required_alp + required_cop
            min_problem = [-1] * len(problem_unit_cost)

            for i, (unit_alp, unit_cop) in enumerate(problem_unit_cost):
                # 문제를 풀고 필요한 코딩, 알고력을 달성하는 경우

                required_time_for_alp = math.ceil(required_alp / unit_alp) if unit_alp != 0 else required_alp
                required_time_for_cop = math.ceil(required_cop / unit_cop) if unit_cop != 0 else required_cop

                # 필요한 alg을 채울만큼 문제를 풀고 cop의 나머지는 문제를 풀지 않고 채우는 경우
                case1 = required_time_for_alp + ((required_cop - unit_cop * required_time_for_alp)
                                                 if required_cop - unit_cop * required_time_for_alp > 0 else 0)

                if case1 < min_cost:
                    min_problem = [required_time_for_alp, if requiredco]
                # 필요한 cop 채울만큼 문제를 풀고 alg 나머지는 문제를 풀지 않고 채우는 경우
                case2 = required_time_for_cop + ((required_alp - unit_alp * required_time_for_cop)
                                                 if required_alp - unit_alp * required_time_for_cop > 0 else 0)
                # 필요한 alg,cop모두 문제를 풀어서 채우는 경우
                case3 = max(required_time_for_alp, required_time_for_cop)

                curr_cost = min(case1, case2, case3)

                if curr_cost < min_cost:
                    min_cost = curr_cost
                    min_problem = i

            # 최소 시간 걸리는 방법으로 필요한 만큼 공부
            cost += min_cost
            # 문제를 푼 경우
            if min_problem != -1:
                alp += problems[min_problem][2] * min_cost
                cop += problems[min_problem][3] * min_cost
            # 문제를 풀지 않은 경우
            else:
                alp += required_alp
                cop += required_cop

    return cost


# print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
