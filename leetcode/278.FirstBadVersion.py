def firstBadVersion(n: int, bad: int) -> int:
    # search insertion position 문제 참고
    def isBadVersion(version: int) -> bool:
        if version == bad:
            return True

    l, u = 0, n
    while l <= u:
        mid = l + (u - l) // 2

        if isBadVersion(mid):
            u = mid - 1
        else:
            l = mid + 1

    return u + 1


def first_bad_version(n: int, bad: int) -> int:
    def is_bad_version(version: int) -> bool:
        if version == bad:
            return True

    l, u = 1, n

    while l < u:

        mid = l + (u - l) // 2

        if is_bad_version(mid):
            u = mid
        else:
            l = mid + 1

    # l == u 검사안된 element 1개인 채로 나옴
    return l


print(firstBadVersion(5, 4))
print(firstBadVersion(1, 1))
