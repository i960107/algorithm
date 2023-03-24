def solution(a: int, b: int, n: int) -> int:
    empty_bottles = n
    required = a
    prize = b

    answer = 0
    while empty_bottles >= required:
        submit = (empty_bottles // required) * required
        empty_bottles -= submit

        get = submit // required * prize
        answer += get
        empty_bottles += get
    return answer


# print(solution(2, 1, 20))
print(solution(3, 1, 20))
