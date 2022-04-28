def hamming_distance_fail(x: int, y: int) -> int:
    # 해밍 거리 : 자연어 처리서 널리 쓰임. 두 정수 또는 두 문자열의 차이
    bin_x = bin(x)
    bin_y = bin(y)
    print(bin_x, bin_y)
    count = 0
    for a, b in zip(bin_x, bin_y):
        print(a, b)
        if a != b:
            count += 1
    return count


def hamming_distance(x: int, y: int) -> int:
    print(bin(x))  # 0b1
    print(bin(y))  # 0b100
    print(x ^ y)  # 5
    print(bin(x ^ y))  # 0b101
    return bin(x ^ y).count('1')


print(hamming_distance(1, 4))
