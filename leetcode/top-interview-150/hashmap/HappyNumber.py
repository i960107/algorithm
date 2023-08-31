class Solution:
    # 왜 hashmap으로 분류되엇을까?
    # hashmap dict
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            sum = 0
            for c in str(n):
                sum += int(c) ** 2
            if sum in visited:
                if sum == 1:
                    return True
                else:
                    return False
            visited.add(sum)
            n = sum


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
