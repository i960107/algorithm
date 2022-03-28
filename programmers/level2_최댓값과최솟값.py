def solution_max_min(s: str) -> str:
    # numbers = list(map(lambda x: int(x[1:]) if x[0] != '-' else int(x[1:]) * -1, s.split()))
    numbers = list(map(lambda x: int(x), s.split()))
    if not numbers:
        return ""
    else:
        min_num, max_num = numbers[0], numbers[0]
        # 최솟값과 최대값을 각각 구하는 것보다 한번 순환하면서 찾는게 더 빠름
        for i in range(len(numbers)):
            if numbers[i] < min_num:
                min_num = numbers[i]
            # 모든 수가 같은 경우 혹은 숫자가 하나인 경우 최솟값 == 최댓값 초기값 설정시 커버되고
            # 이외 경우라면  최솟값 != 최댓값
            # 최솟값이라면 최댓값이 될 수 없고, 최솟값이 아닌 경우에만 최대값이 될 수 있기 때문에
            # 별도의 조건문이 아니라 elif로 처리하기
            elif numbers[i] > max_num:
                max_num = numbers[i]
        return str(min_num) + " " + str(max_num)


print(solution_max_min("1 2 3 4"))
print(solution_max_min("-1 -2 -3 -4"))
print(solution_max_min("-1 -1"))

# int()로 음수를 표현한 문자열 정수로 표현가능
# 반대로, 음수 정수형 -> - 포함한 문자열도 가능
print(int("-4") == -4)  # True
print(int("4") == 4)
