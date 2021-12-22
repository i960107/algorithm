from itertools import cycle


def solution_zip(answers: list) -> list:
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

    print(f'solution_zip : {cnt}')
    max_count = max(cnt)
    return [i + 1 for i in range(len(cnt)) if cnt[i] == max_count]


def solution_index(answers: list) -> list:
    # 배열자체를 반복시키는 것보다 index를 조정하는게 더 나음(공간 복잡도 측면)
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0] * 3

    for idx, answer in enumerate(answers):
        if answer == person1[idx % len(person1)]:
            cnt[0] += 1
        if answer == person2[idx % len(person2)]:
            cnt[1] += 1
        if answer == person3[idx % len(person3)]:
            cnt[2] += 1

    print(f'solution_index : {cnt}')
    return [i + 1 for i in range(len(cnt)) if cnt[i] == max(cnt)]


def solution_cycle(answers: list) -> list:
    person1 = cycle([1, 2, 3, 4, 5])
    person2 = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    person3 = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    return []


print(solution_zip([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] * 1000))
print(solution_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] * 1000))

print(solution_zip([1, 2, 3, 4, 5]))
print(solution_index([1, 2, 3, 4, 5]))

print(solution_zip([1, 4, 2, 4, 2]))
print(solution_index([1, 4, 2, 4, 2]))

print(solution_zip([]))
print(solution_index([]))
