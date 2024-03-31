class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 어떤 수의 trailing zeroes 의 개수는
        # 소인수분해 결과에 10 (2 *5)가 몇번 들어갔는지에 따라 다름.

        count2 = 0
        temp_n = n
        while temp_n:
            if temp_n % 2 != 0:
                break
            count2 += 1
            temp_n = temp_n // 2

        count5 = 0
        temp_n = n
        while temp_n:
            if temp_n % 5 != 0:
                break
            count5 += 1
            temp_n = temp_n // 5

        return min(count2, count5)

    def trailingZeroes2(self, n: int) -> int:
        # 1 ~ n중에 5의 배수. 25의 배수.
        temp = 5
        count = 0
        while temp <= n:
            count += (n // temp)
            temp *= 5
        return count


s = Solution()
print(s.trailingZeroes2(3))
print(s.trailingZeroes2(5))

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

rows, cols = len(arr), len(arr[0])
new_arr = [[0] * rows for _ in range(cols)]
for c in range(cols):
    for r in range(rows):
        # new_arr[c][r] = arr[r][c]
        new_arr[c][rows - 1 - r] = arr[r][c]
for row in new_arr:
    print(row)
