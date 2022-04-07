def isPerfectSquare(num: int) -> bool:
    l, u = 1, num
    while l <= u:
        mid = l + (u - l) // 2
        if mid ** 2 < num:
            l = mid + 1
        elif mid ** 2 > num:
            u = mid - 1
        else:
            return True
    return False


print(isPerfectSquare(16))  # true
print(isPerfectSquare(14))  # false
