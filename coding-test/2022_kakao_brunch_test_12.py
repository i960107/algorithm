def solution(x: int, y: int, z: int):
    adjustment = abs(y - x)
    if adjustment > z:
        return -1
    if x <= y:
        right = adjustment + (z - adjustment) // 2
        left = z - right
    else:
        left = adjustment + (z - adjustment) // 2
        right = z - left
    return x + right


# print(solution(4, 4, 4))
# print(solution(8, 5, 3))
# print(solution(8, 6, 2))  # 8
# print(solution(4, 4, 6))
# print(solution(4, 4, 5))
print(solution(1892, 1896, 7))  # test 3  expected 1897
print(solution(659076, 659077, 8))  # test 4  expected -1
print(solution(19572320, 19572321, 10))  # test 6 expected- 1
print(solution(65913520, 65913524, 7))  # test 9 expected - 1
print(solution(100000000, 100000000, 15))  # test 11 expected -1
