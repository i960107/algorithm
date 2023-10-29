from typing import List


class Solution:
    # n은 1 이상
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        # 낮은 쪽은 항상 채워짐. 낮은 쪽이 높은 쪽을 향해서 포인터가 점점 가운데로 이동.
        # 쵀디 지점에서 좌우 포인터가 서로 만나게 되며 O(n)
        # 큰 쪽을 두고 채워감 -> 오른쪽 막히는것이 보장
        while left < right:
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
        return volume

    # def trap2(self, height: List[int]) -> int:
    #     index = 0
    #     left_max = height[0]
    #
    #     # 한쪽 방향으로만 진행하면 왜 안되지.
    #     # 오른쪽이 안 막힘.
    #     # 4,3,2,1 일때 최종 볼륨 6
    #     while index < len(height):
    #         index += 1
    #         if height[index] > left_max:
    #             left_max = height[index]
            left_max - height[index]

    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        # 큰걸 만났을때만 막아줌
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
