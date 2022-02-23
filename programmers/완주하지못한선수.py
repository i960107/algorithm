from collections import Counter


def solution(participants: list, completion: list) -> str:
    '''dictionry자료형 사용'''

    d = {}

    for person in participants:
        d[person] = d.get(person, 0) + 1

    for person in completion:
        d[person] = d.get(person) - 1

    # list(d.keys())[0]하면 부정확한 값이 됨. participants의 가장 앞 사람이 출력됨.
    # for person, cnt in d.items():
    #     if cnt > 0:
    #         return person

    # list comprehension으로 한줄로 표현 가능.
    # True/False로 출력됨. 잘못된 표현
    # return [d[person] > 0 for person in d.keys()][0]
    return [person for person in d.keys() if d[person] > 0][0]


# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "misalv", "ana"], ["mislav", "stanko", "ana"]))


def solution_others(participants: list, completion: list) -> str:
    '''Counter객체 사용하여 두 배열간 빼기'''
    answer = Counter(participants) - Counter(completion)
    # keys() keysView객체 반환. list로 타입캐스팅 필요.
    print(answer)
    answer = list(answer.keys())[0]
    return answer


print(solution_others(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution_others(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution_others(["mislav", "stanko", "misalv", "ana"], ["mislav", "stanko", "ana"]))

a = [1, 2, 2, 3, 3, 3]
b = [1, 2]
print(Counter(a) - Counter(b))
