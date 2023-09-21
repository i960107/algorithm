from typing import List


class Solution:
    # n은 1 이상
    def trap(self, height: List[int]) -> int:
        new_height = []
        for h in height:
            if new_height and new_height[-1] >= h:
                new_height.append(new_height[-1])
            else:
                new_height.append(h)
        print(height)
        print(new_height)
        result = [h1 - h2 for h1, h2 in zip(new_height, height)]
        print(result)
        # 언제 막아주느냔.


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
