def arrange_coins(n: int) -> int:
    '''find the maximum k such that k(k+1)/2<=N'''
    left, right = 0, n
    while left <= right:
        k = left + (right - left) // 2
        # 현재까지 row까지 필요한 coin의 개수
        curr = k * (k + 1) / 2
        if curr == n:
            return k
        if n < curr:
            right = k - 1
        else:
            left = k + 1

    # left > right 빠져나옴
    # 모든 값 검사 끝난 상황
    # left: n > curr, right:n<curr
    # search_insertion_position과 비
    return left - 1


print(arrange_coins(5))
print(arrange_coins(8))
