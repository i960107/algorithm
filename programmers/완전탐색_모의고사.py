def solution(answers: list) -> list:
    person1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    cnt = [0] * 3

    for n1, n2, n3, answer in zip(person1, person2, person3, answers):
        if n1 == answer:
            cnt[0] += 1
        if n2 == answer:
            cnt[1] += 1
        if n3 == answer:
            cnt[2] += 1

    max_count = max(cnt)
    if max_count == 0:
        return []
    else:
        return [i + 1 for i in range(len(cnt)) if cnt[i] == max_count]


print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(solution([]))
