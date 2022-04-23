from typing import List, Optional
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(t1: TreeNode, t2: TreeNode):
    '''반복 풀이'''
    stack1 = deque([t1])
    stack2 = deque([t2])

    while stack1 or stack2:

        e1, e2 = None, None
        if stack1:
            e1 = stack1.popleft()
            stack1.append(e1.left)
            stack1.append(e1.right)
        if stack2:
            e2 = stack2.popleft()
            stack2.append(e2.left)
            stack2.append(e2.right)

        sum_e = 0
        sum_e += e1 if e1 else 0
        sum_e += e2 if e2 else 0


def solution_recursive(t1: TreeNode, t2: TreeNode):
    '''재귀 풀이'''
    # 후위 순회
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = solution_recursive(t1.left, t2.left)
        node.right = solution_recursive(t1.left, t2.left)
        return node
    else:
        # 존재하는 노드만 리턴.양쪽 모두 없다면 None이 될 것
        return t1 or t2
