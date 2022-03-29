def solution(n: int) -> int:
    def get_count_of_1_binary(num: int) -> int:
        cnt = 0
        num, remainder = num // 2, num % 2
        while num > 0:
            if remainder == 1:
                cnt += 1
            num, remainder = num // 2, num % 2
        if remainder == 1:
            cnt += 1
        return cnt

    count = get_count_of_1_binary(n)
    answer = n + 1
    while count != get_count_of_1_binary(answer):
        answer += 1
    return answer


print(solution(78))
print(solution(15))
