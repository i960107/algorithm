from collections import Counter


def solution(name: str) -> str:
    # alpha_cnt
    name_counter = Counter(name)
    # 한번에 검사하는 방법이 있나?

    half = []
    mid = []
    for x, count in sorted(name_counter.items()):
        half.extend([x] * (count // 2))
        # counter - 할수 있나? 참조형 변수 아닐텐데
        name_counter[x] -= count
        if count % 2 == 1:
            if mid:
                return "Im sorry hansoo"
            mid.append(x)

    # 왜 int object이지? -> counter 는 dictionary형이기 때문에 [0] 으로 지정하는게 인덱스가 아니라 key임!!
    # print(name_counter)
    # print(name_counter[0])
    # print(name_counter[1])

    # "".join(half[::-1]만 출력됨 왜?
    return "".join(half + mid + half[::-1])


print(solution("AABB"))
print(solution("ACACBCB"))
