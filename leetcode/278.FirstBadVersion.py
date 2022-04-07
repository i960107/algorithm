def firstBadVersion(n: int) -> int:
    # search insertion position 문제 참고
    l, u = 0, n
    while l <= u:
        mid = l + (u - l) // 2

        if isBadVersion(mid):
            u = mid - 1
        else:
            l = mid + 1
    return u + 1
