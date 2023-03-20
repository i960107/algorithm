def solution(n: int) -> int:
    # 어떻게 문자열이랑 비트 연산을 하지?
    # string을 int로 바꿔야하나.
    # 해밍 가중치
    return bin(n).count("1")


def solution2(n: int) -> int:
    # 어떻게 길이만큼 해줄수 있을까..
    hamming_weight = "0b" + "1" * 32
    return bin(n & int(hamming_weight, 2)).count("1")

# 파이썬의 문자열 기능을 사용하지 않고 비트연산만으로
def solution2(n: int) -> int:
    hamming_weight = "0b" + "1" * 32
    return bin(n & int(hamming_weight, 2)).count("1")

# 32비트 binary 로 표현하기
def _bin(n: int):
    # 비트 연산의 결과는 int로 저장됨
    i = 1 << 31

    answer = []
    while i > 0:
        # 왜 n 그대로지...?
        # print(n & i)  # 결과도 Int형임
        if (n & i) >= 1:
            answer.append("1")
        else:
            answer.append("0")
        i >>= 1
        # i //= 2
    return ''.join(answer)


# print(_bin(7))
# 입력이 어떻게 int형이 된다는거ㅑㅇ..
# 0b붙이면 string 형식아니고 SIgned int로 저장됨.
print(solution2(0b00000000000000000000000000001011))
