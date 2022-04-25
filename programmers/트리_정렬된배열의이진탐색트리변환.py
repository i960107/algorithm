from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 정렬된 배열이면 가장 가운데 원소가 TreeNode가 되야함
        if not nums:
            return None

        # 먄악 mid = (len(nums) -1) // 2 이 된다면?
        # 배열의 모든 원소를 커버하면 되므로 상관 없음
        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])

        node.left = self.convertArrayToBST(nums[:mid])
        # list index out of bound 에러 발생하지 않나?
        # python list slicing은 index에러 발생시키지 않음. 인덱스 벗어나면 None을 반환
        node.right = self.convertArrayToBST(nums[mid + 1:])

        return node


s = Solution()
root = s.convertArrayToBST([-10, -3, 0, 5, 9])
