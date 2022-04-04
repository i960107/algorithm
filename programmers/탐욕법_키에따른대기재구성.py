from typing import List


def solution(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda x: x[0])
    people.sort(key=lambda x: x[0], reverse=True)

    # for i in range(len(people) - 1, -1, -1):
    #     curr = people[i]
    #     cnt = curr[1] - (len(people) - 1 - i)
    #     while cnt > 0:
    #         people[i], people[i - 1] = people[i - 1], people[i]
    #         i -= 1
    #         cnt -= 1

    return people


print(solution([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
