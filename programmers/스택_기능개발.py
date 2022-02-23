import math


def solution(progresses: list, speeds: list) -> list:
    answer = []
    daysLefts = []

    for progress, speed in zip(progresses, speeds):
        daysLeft = math.ceil((100 - progress) / speed)
        daysLefts.append(daysLeft)

    i = 0
    while i <= len(progresses) - 1:
        curr = daysLefts[i]
        count = 1
        while i + 1 <= len(progresses) - 1 and curr >= daysLefts[i + 1]:
            count += 1
            i = i + 1
        answer.append(count)
        i += 1
    return answer


def solution_others(progresses, speeds):
    # 람다식으로 짧게 표현
    daysLefts = list(map(lambda x: (math.ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    answer = []
    for i in range(len(daysLefts)):
        try:
            # 뒤 원소가 다른 배포 그룹이다
            if daysLefts[i] < daysLefts[i + 1]:
                answer.append(count)
                count = 1
            # 뒤 원소가 같은 배포그룹이다
            else:
                daysLefts[i + 1] = daysLefts[i]
                count += 1
        except IndexError:
            # 마지막 원소를 에러 발생할 것이기 때문에 except로 캐치 후 배열에 추가해주기.
            # 이미 이전 원소 순환문에서 이번 원소의 배포그룹 정해짐.
            answer.append(count)

    return answer


def solution_practice(progresses: list, speeds: list) -> list:
    '''배포까지 남은 기간을 담은 배열을 만든 후
    1번째 원소부터 끝까지 순회화면서 해당 인덱스 값을 이전 인덱스 값과 비교해서
    해당 인덱스가 같은 배포그룹인지 결정'''
    answer = []
    remain = [None] * len(progresses)

    for i in range(len(progresses)):
        remain[i] = math.ceil((100 - progresses[i]) / speeds[i])

    d_count = 1

    for i in range(1, len(remain)):
        if remain[i] <= remain[i - 1]:
            d_count += 1
            remain[i] = remain[i - 1]
        else:
            answer.append(d_count)
            d_count = 1

    answer.append(d_count)
    return answer


print(solution_practice([93, 30, 55], [1, 30, 5]))
print(solution_others([93, 30, 55], [1, 30, 5]))
print(solution_practice([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution_others([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
