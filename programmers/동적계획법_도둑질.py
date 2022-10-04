from typing import List


# def solution(money: list) -> int:
#     answer = 0
#     # l = [i for i in range(len(money))]
#     # sorted_index = sorted(l, key=lambda x: money[x], reverse=True)
#     #
#     # for i in sorted_index:
#     #     left = i - 1
#     #     right = i + 1 if i + 1 < len(money) else 0
#     #     # 양 옆에 집이 안털렸으면.큰 값부터 더해간다고 최댓값 되지 않음..
#     #     if money[left] != -1 and money[right] != -1:
#     #         answer += money[i]
#     #         money[i] = -1
#     #
#     # 최대한 많은 집을 털어야하는것 아님.
#     # 최대한 많은 돈을 털어야한다.
#     max_house = (len(money) + 1) % 2
#     case1 = sum(money[i] for i in range(0, len(money), 2))
#     case2 = sum(money[i] for i in range(1, len(money), 2))
#     return max(case1, case2)
#
#
# def solution_others(money: list) -> int:
#     # 도둑이 훔칠 수 있는 돈의 최댓값을 저장하는 dp 배열 생성
#     # dp[i] 는 i번째 집까지 털었을때 훔칠 수 있는 돈의 최댓값
#     # dp[i]= max((바로 전집까지 훔칠 수 있는 최대값) (전전집까지 털고, 현재집 터는 경우))
#     # 1번집을 털경우 마지막 전집까지, 1번집을 안 털경우 마지막 집까지, 두 경우느 중 큰 값을 반환
#     # 배열 미리 할당해두어야 index에러 안남?
#     dp1 = [0] * len(money)
#     dp1[0] = money[0]
#     dp2 = [0] * len(money)
#     for i in range(1, len(money) - 1):
#         # i==1 일때 dp[i-2]는 어떻게 처리되지? dp[-1]
#         # -len(arr) <= i < len(arr) 인 i에 대해서는 index error발생안함
#         dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
#     # 털지 않을때 i ==1 이고 마지막 집 털지 말지 어떻게 결정?
#     # dp는 i번째까지 털었을때를 말함.
#     for i in range(1, len(money)):
#         dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
#     return max(dp1[-2], dp2[-1])
#
#
# # def solution_test(money:list)->int:
# #
# #     return 0

def solution(money: List[int]) -> int:
    n = len(money)


    dp1 = [0] * (n-1)
    dp1[0] = money[-2]
    dp1[1]
    dp1[1]

    dp2 = [0] * (n-1)


print(solution([1, 2, 3, 1]))
print(solution([1, 2, 3, 1, 4]))
print(solution([1, 1, 1, 1]))
#
