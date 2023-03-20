def solution(x: int, y: int) -> int:
    result = bin(x ^ y)
    return sum(1 for x in result if x == "1")


def solution2(x: int, y: int) -> int:
    return bin(x ^ y).count("1")


print(solution(1, 4))
print(solution2(1, 4))
