def solution(money: list) -> int:
    answer = 0
    # l = [i for i in range(len(money))]
    # sorted_index = sorted(l, key=lambda x: money[x], reverse=True)
    #
    # for i in sorted_index:
    #     left = i - 1
    #     right = i + 1 if i + 1 < len(money) else 0
    #     # 양 옆에 집이 안털렸으면.큰 값부터 더해간다고 최댓값 되지 않음..
    #     if money[left] != -1 and money[right] != -1:
    #         answer += money[i]
    #         money[i] = -1
    #

    return answer


# def solution_test(money:list)->int:
#
#     return 0
# print(solution([1, 2, 3, 1]))