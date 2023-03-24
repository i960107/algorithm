from typing import List


def solution(food: List[int]) -> str:
    result = []
    for food_id in range(1, len(food)):
        amount = food[food_id]
        for _ in range(amount // 2):
            result.append(str(food_id))

    reverse_result = result[::-1]
    result.append("0")
    result += reverse_result
    return ''.join(result)


# 칼로리가 큰 것부텉 더하면 더 간단?
# 중간에 0을 넣고 앞뒤로 붙여줌.
def solution2(food: List[int]) -> str:
    answer = '0'
    for food_id in range(len(food) - 1, 0, -1):
        food_count = food[food_id]
        for _ in range(food_count // 2):
            answer = str(food_id) + answer + str(food_id)
    return answer


print(solution2([1, 3, 4, 6]))
print(solution2([1, 7, 1, 2]))
