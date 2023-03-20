from typing import List


def solution(data: List[int]) -> bool:
    is_encoded_utf8 = True
    bytes = 0
    for x in data:
        # bitmask해야하나..
        bin_x = bin(x)[2:].rjust(8, "0")
        if bytes:
            if not bin_x[:2] == "10":
                is_encoded_utf8 = False
                break

        else:
            for num in bin_x:
                if num == "1":
                    bytes += 1
                else:
                    break
            if bytes == 1 or bytes > 4:
                is_encoded_utf8 = False
                break
            if not bytes:
                bytes = 1
        bytes -= 1

    if bytes:
        is_encoded_utf8 = False

    return is_encoded_utf8


def solution2(data: List[int]) -> bool:
    # 문자 바이트 만큼(실제 utf-8 바이트수 - 1이 입력값) 10으로 시작 판별
    def check(size: int) -> bool:
        for i in range(start + 1, start + 1 + size):
            if not (i < len(data)) or data[i] >> 6 != 0b10:
                return False
        return True

    start = 0
    while start < len(data):
        if (data[start]) >> 3 == 0b11110 and check(3):
            start += 4
        elif (data[start]) >> 4 == 0b1110 and check(2):
            start += 3
        elif (data[start]) >> 5 == 0b110 and check(1):
            start += 2
        elif (data[start]) >> 7 == 0b0:
            start += 1
        else:
            # check결과가 false이거나 시작 문자가 10인 경우.
            return False
    return True


print(solution([197, 130, 1]))
print(solution2([197, 130, 1]))
print(solution([235, 140, 4]))
print(solution([145]))
print(solution2([235, 140, 4]))
print(solution2([145]))
# print(bin(~0b1100))
# print(0b1111 ^ 0b1100)
