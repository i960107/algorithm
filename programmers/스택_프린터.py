from collections import Counter


def solution(priorities: list, location: int) -> int:
    answer = 0
    counter = Counter(priorities)

    # 값이 targetP인 counter자체 삭제. -1아님
    # counter.pop(targetP)

    #왜안되는거야 ㅠㅠㅠㅠㅠ 복잡도는 더 낮은것 같은데..

    front = 0
    targetP = max(counter)
    targetPCount = counter.get(targetP)
    while answer <= len(priorities):
        if priorities[front] == targetP:
            targetPCount -= 1
            answer += 1
            if targetPCount == 0:
                counter.pop(targetP)
                targetP = max(counter)
                targetPCount = counter.get(targetP)
            if front == location:
                break

        front = (front + 1) % len(priorities)

    return answer


# def solution(priorities: list, location: int) -> int:
# 아래 경우 때문에  이같은 풀이는 안됨
# print(solution([1, 1, 9, 1, 1, 1, 1], 0))
#     answer = 0
#
#     counter = Counter(priorities)
#     maxPriority = max(priorities)
#     targetPriority = priorities[location]
#
#     for i in range(maxPriority, targetPriority):
#         answer += counter.get(targetPriority)
#
#     print(f'타겟보다 우선순위 높은 프린터물 개수  {answer}')
#     i = 0
#     while i <= location:
#         if priorities[i] == targetPriority:
#             answer += 1
#
#         i += 1
#     return answer

def solution_others(priorities: list, location: int):
    answer = 0
    array1 = [c for c in range(len(priorities))]  # 인덱스 위치 저장
    array2 = priorities.copy()  # 값 저장

    i = 0
    while True:
        if array2[i] < max(array2[i + 1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1
        if array2 == sorted(array2, reverse=True):
            break
    return array1.index(location) + 1


def solution_others2(priorities: list, location: int):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        # O(n)인데?
        cur = queue.pop(0)
        # 하나라도 우선순위가 높은 것 있으면
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 4, 8, 2, 9, 3, 3], 2))
print(solution([2, 4, 8, 2, 9, 3, 3], 4))
