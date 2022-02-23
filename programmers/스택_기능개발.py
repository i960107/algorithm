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


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


def solution_others(progresses, speeds):
    # 람다식으로 짧게 표현
    daysLefts = list(map(lambda x: (math.ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    answer = []
    for i in range(len(daysLefts)):
        try:
            if daysLefts[i] < daysLefts[i + 1]:
                answer.append(count)
                count = 1
        except IndexError:
            # 뒤 작업도 가치 배포되어야 한다면 count추가해주고 뒤 작업을 기준 day로 덮어쓰기
            daysLefts[i + 1] = daysLefts[i]
            count += 1
            answer.append(count)
        return answer
