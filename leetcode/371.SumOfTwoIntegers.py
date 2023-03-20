def solution_fail(x: int, y: int) -> int:
    result = ''
    up = False
    mask = "0b1111"
    for a, b in zip(bin(x ^ mask)[:-2:-1], bin(y)[:-2:-1]):
        a = int(a)
        b = int(b)
        temp = 1 if up else 0
        up = False
        if a | b and not a ^ b:
            up = True
            temp ^= 1
        elif a | b and a ^ b:
            temp ^= 1
            up = (temp != "1")
        elif not a | b and a ^ b:
            temp ^= 1
        result += str(temp)
        print(a, b, temp)
    return int(result)


def solution(a: int, b: int) -> int:
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

        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum = carry ^ Q2
        carry = Q1 | Q3

        result.append(str(sum))
    if carry == 1:
        result.append("1")
    result = int(''.join(result[::-1]),2) & MASK

    if result > INT_MAX:
        result = ~(result ^ MASK)

    return result


def solution_simple(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a > INT_MAX:
        a = ~(a ^ MASK)
    return a


print(solution(1, 2))
print(solution(-2, 3))
