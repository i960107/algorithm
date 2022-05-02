def judgeSquareSum_fail(c: int) -> bool:
    left, right = 0, c
    # 투포인터로 선형 검색하기에는 너무 범위가
    # 같은 수일 수도 있음
    # 이게 왜 안되는지 알아보기 time limti exceed?
    while left <= right:
        curr = left * left + right * right
        if curr == c:
            return True
        elif curr < c:
            left += 1
        else:
            right -= 1
    return False


def judgeSquareSum(c: int) -> bool:
    def binary_search(s, e, n):
        '''s와 e사이의 값 중 제곱수가 n이 되는 수'''
        while s <= e:
            mid = s + (e - s) // 2

            # division by zero에러 어떻게 처리할까

            if mid * mid == n:
                return True
            elif mid * mid < n:
                s = mid + 1
            else:
                e = mid - 1
        return False

    for a in range(0, int(c ** 0.5) + 1):
        b = c - a * a
        if binary_search(0, b, b):
            return True
    return False


print(judgeSquareSum(5))
print(judgeSquareSum(3))
print(judgeSquareSum(2))
