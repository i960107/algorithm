from typing import List
import heapq


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


def solution_priority_queue(people: List[List[int]]) -> List[List[int]]:
    '''우선순위 큐 이용'''
    # 우선순위 큐 자체가 매번 그때끄때의 최소 또는 최댓값을 추출하기 때문에, 그리디에 어울리는 대표적인 자료구조
    heap = []

    # 키 역순, 인덱스 삽입
    # O(NlogN)
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    result = []

    # 키 역순, 인덱스 추출
    # 복잡도?
    # O(N^2)
    while heap:
        # O(LogN)
        person = heapq.heappop(heap)
        print(person)
        # 지금 result에 있는 사람들은 다 자기보다 키가 큼. person[1]이 index가 됨
        # O(N)
        result.insert(person[1], [-person[0], person[1]])
    return result


def solution_test(people: List[List[int]]) -> List[List[int]]:
    # heap을 사용하는 것과 배열을 사용하는 것의 차이?
    result = []
    people.sort(key=lambda x: (x[0], -x[1]))

    while people:
        person = people.pop()
        print(person)
        # insert index 에러 안나나?
        result.insert(person[1], person)

    return result


print(solution_priority_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
print(solution_test([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
