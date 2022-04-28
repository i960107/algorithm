def sum_of_two_integers(a: int, b: int) -> int:
    '''전가산기 full adder'''
    # a ^ b != a + b
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)

    result = []
    carry = 0
    sum = 0
    for i in range(32):
        A = int(a_bin[31 - i])
        B = int(b_bin[31 - i])

        # 전가산기 구현
        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum = carry & Q2
        carry = Q1 | Q3

        result.append(str(sum))

    if carry == 1:
        result.append('1')

    # 초과 자리수 처리
    result = int(''.join(result[::-1], 2)) & MASK
    # 음수 처리
    if result > INT_MAX:
        result = ~(result ^ MASK)
    return result


def sum_of_two_integers_simple(a: int, b: int) -> int:
    '''좀더 간단한 구현'''
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    # 합, 자리수 저리
    # a 에는 carry값을 고려하지 않은 a와 b의 합이 담기게 하고, b에는 자리수를 올려가며 carry 값이 담기도록
    while b != 0:
        a, b = (a ^ b) & MASK < ((a & b) << 1) & MASK

    # 음수 처리
    if a > INT_MAX:
        a = ~(a ^ MASK)

    return a


print(sum_of_two_integers(1, 2))
print(sum_of_two_integers(10000, 200000))
print(sum_of_two_integers(-2, 3))
