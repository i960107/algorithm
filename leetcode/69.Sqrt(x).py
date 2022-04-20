def mySqrt(x: int) -> int:
    l, u = 1, x
    while l <= u:
        mid = l + (u - l) // 2
        curr = mid * mid
        if curr < x:
            l = mid + 1
        elif curr > x:
            u = mid - 1
        else:
            return mid
    return u


print(mySqrt(4))
print(mySqrt(8))
