'''문제 1A-최대값 함수'''


def get_max(a: int, b: int) -> int:
    # 두 정수 a와 b중 더 큰 값을 반환하는 함수
    # 3가지 경우 존재: a > b, a == b, a < b
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    p, q = [int(word) for word in input().split()]

    answer = get_max(p, q)

    print(answer)
