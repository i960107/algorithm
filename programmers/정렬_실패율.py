from collections import Counter


def solution_failure(N: int, stages: list) -> list:
    s = [i + 1 for i in range(N)]
    failures = [0] * N

    counter = Counter(stages)
    # dicionary 항상 가져올때 None 주의!!. 아니면 최대한 defaultdict 사용하기
    reached = counter.get(N + 1, 0)

    for stage in range(N, 0, -1):
        reached += counter.get(stage, 0)
        if reached:
            failure = counter.get(stage, 0) / reached
        else:
            failure = 0
        failures[stage - 1] = failure

    # zip은 tuple을 반환 -> 인덱스로 접근 가능
    return [s for _, s in sorted(zip(failures, s), key=lambda x: (x[0], -x[1]), reverse=True)]


def solution_others(N: int, stages: list) -> list:
    # set? dictionary? -> 추후에 삽입되는 값에 따라 달라짐
    # stage 별 실패율j
    result = {}
    counter = Counter(stages)
    # 모든 사람이 stage 1부터 시작할테니깐!
    denominator = len(stages)
    for stage in range(1, N + 1):
        if denominator != 0:
            count = counter.get(stage, 0)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    # dictionary 자체를 sort할 수 있는게 아니라 result는 result.keys()를 의미함
    # stage 낮은 순 정렬은 왜 자동으로 되지 -> python 3.7 부터 dictionary는 순서를 보장함?
    return sorted(result, key=lambda x: result[x], reverse=True)


print(solution_failure(5, [2, 1, 2, 6, 4, 3, 3]))
print(solution_failure(4, [4, 4, 4, 4, 4]))
