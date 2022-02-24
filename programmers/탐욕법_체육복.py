def solution1(n: int, lost: list, reserve: list) -> int:
    answer = 0
    # 맨 앞, 맨 뒤 dummy 원소 추가. index out of range error 방지.
    uniform = [1] * (n + 2)

    for num in lost:
        uniform[num] -= 1

    for num in reserve:
        uniform[num] += 1

    for i in range(1, n + 1):
        if uniform[i] == 2 and uniform[i - 1] == 0:
            # list slicing 으로 한번에 두 원소 값 바꿀 수 있음
            uniform[i - 1:i + 1] = [1, 1]
        elif uniform[i] == 2 and uniform[i + 1] == 0:
            uniform[i:i + 2] = [1, 1]

    return len([i for i in range(1, n + 1) if uniform[i] >= 1])


def solution2(n: int, lost: list, reserve: list) -> int:
    # set형으로 교집합 구하기
    # 체육복을 가져왔으면서 잃어버린 학생 빌릴 필요 없음
    s = set(lost) & set(reserve)
    # 체육복을 잃어버렸지만 가져오지 않았기 때문에 빌려야 하는 학생
    l = set(lost) - set(reserve)
    # 체육복을 가져왔으면 잃어버리지 않은 학생. 빌려줄 수 있는 학생
    r = set(reserve) - s

    # list형 아니기 때문에 r.sort() 메소드 없음
    # sorted(r)의 결과는 list임. set을 순환할때는 검사되는 순서 보장할 수 없음.
    for x in sorted(r):
        # 집합에 속해 있는지 in 으로 상수 시간에 검색 가능
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    # 전체 학생 수 - 빌려야 하지만 빌리지 못한 학생
    return n - len(l)


print(solution1(5, [2, 4], [1, 3, 5]))
print(solution1(5, [2, 4], [3]))
print(solution1(3, [3], [1]))
