from typing import List


class Solution:
    # 아이들은 모두 최소 한개의 캔디를 받아야한다.
    # rating이 높으면 더 많이 받아야한다.
    # 한쪽 방향으로만 신경쓰면 되나? 안됨...
    def candy(self, ratings: List[int]) -> int:
        # 첫번째 아이에게 한개 주고 시작.
        prev = 1
        total = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy = 1
            elif ratings[i] < ratings[i - 1]:
                candy = 1
            elif ratings[i] == ratings[i]:
                candy = 1
        return total


s = Solution()
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
print(s.candy([1, 2, 3, 4]))
print(s.candy([4, 3, 2, 1]))
print(s.candy([1]))
