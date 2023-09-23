from typing import List


class Solution:
    # 아이들은 모두 최소 한개의 캔디를 받아야한다.
    # rating이 높으면 더 많이 받아야한다.
    # 한쪽 방향으로만 신경쓰면 되나? 안됨...
    # [1,2,2]일때 두번째 2는 1보다 많이 받을 필요 없음.
    # 같은 2여도 다른 candy받을 수 있음.
    def candy(self, ratings: List[int]) -> int:
        candy = [None] * len(ratings)

        sorted_index = sorted(range(len(ratings)), key=lambda i: ratings[i])

        for i in sorted_index:
            # 자신보다 작은 원소를 이웃하고 있는지
            # candy에 값이 있어도 rating이 같다면 1로 넣어주기
            left = 0
            if i - 1 >= 0 and ratings[i - 1] < ratings[i]:
                left = candy[i - 1]

            right = 0
            if i + 1 < len(ratings) and ratings[i + 1] < ratings[i]:
                right = candy[i + 1]

            candy[i] = max(left, right) + 1

        return sum(candy)

    def candy(self, R):
        n, ans = len(R), [1] * len(R)

        for i in range(n - 1):
            if R[i] < R[i + 1]:
                ans[i + 1] = 1 + ans[i]

        for i in range(n - 2, -1, -1):
            if R[i + 1] < R[i]:
                ans[i] = max(1 + ans[i + 1], ans[i])

        return sum(ans)


s = Solution()
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
print(s.candy([1, 2, 3, 4]))
print(s.candy([4, 3, 2, 1]))
print(s.candy([1]))
