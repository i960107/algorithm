from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BST는 여러가지 버전으로 만들 수 있지만
    # 오름차순그대로 BST를 만들면 높이가 n이 된다
    # 균형이진트리로 만들려면 divide-and-conquer가 필요하다.

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def _sortedArrayToBST(arr: List[int]) -> Optional[TreeNode]:
            if not arr:
                return None
            n = len(arr)
            mid = n // 2
            left = _sortedArrayToBST(nums[0: mid - 1])
            right = _sortedArrayToBST(nums[mid + 1: n - 1])
            return TreeNode(nums[mid], left, right)

        return _sortedArrayToBST(nums)

    # 배열 자체를 넘기기 보다 인덱스를 넘기는 것이 더 빠르고 메모리 낭비 적음.
    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(nums) - 1)

