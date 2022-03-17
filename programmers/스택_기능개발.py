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

    count = 0
    answer = []
    for i in range(len(daysLefts)):
        try:
            count += 1
            if daysLefts[i] < daysLefts[i + 1]:
                answer.append(count)
                count = 0
            else:
                # 뒤 작업도 같이 배포되어야 한다면 count추가해주고 뒤 작업을 기준 day로 덮어쓰기
                daysLefts[i + 1] = daysLefts[i]
        except IndexError:
            answer.append(count)
    return answer


def solution_stack(progresses: list, speeds: list) -> list:
    answer = []
    # list 앞에서부터 pop하면 O(n). list slicing으로 뒤집은 후  pop() 하면 O(1)
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)][::-1]

    stack = []
    # 스택에 넣을 수도 있고
    cnt = 0
    while days:
        # 헐....! stack[-1]이랑 비교하면 안됨
        if (stack and stack[0] >= days[-1]) or not stack:
            stack.append(days.pop())
        else:
            cnt = len(stack)
            answer.append(cnt)
            stack = [days.pop()]

    if stack:
        answer.append(len(stack))

    # 기준 값으로 교체해가면서 할 수도 있고
    return answer


print(solution_stack([93, 30, 55], [1, 30, 5]))
print(solution_stack([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# 주의할케이스! 배포 기준이 되는 날에 완성되었지만, 자기보다 앞에 자기보다 먼저 완성되는 기능이 있을경우?
# stack의 맨 첫 원소가 비교해야 함
print(solution_stack([96, 99, 98, 97], [1, 1, 1, 1]))
