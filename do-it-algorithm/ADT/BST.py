from __future__ import annotations
from typing import Any, Optional, List


class Node:
    def __init__(self, key: int, val: Any, left: Node = None, right: Node = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key) + str(self.val)


class BST:
    def __init__(self):
        self.root = None

    def add(self, key: int, value: Any):
        def add_node(curr: Node, key: int, value: Any) -> bool:
            if curr.key == key:
                return False
            if curr.key < key:
                if curr.right is None:
                    curr.right = Node(key, value)
                else:
                    add_node(curr.right, key, value)
            else:
                if curr.left is None:
                    curr.left = Node(key, value)
                else:
                    add_node(curr.left, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value)
            return True
        return add_node(self.root, key, value)

    def search(self, key: int):
        curr = self.root

        while curr:
            if curr.key == key:
                return curr
            elif curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        return None

    def remove(self, key: int):
        curr = self.root
        parent = None
        is_left_child = False
        while curr:
            if curr.key == key:
                break
            parent = curr
            if curr.key < key:
                curr = curr.right
                is_left_child = False
            else:
                curr = curr.left
                is_left_child = True

        if curr is None:
            return False

        degree = 0
        if curr.left is not None:
            degree += 1
        if curr.right is not None:
            degree += 1

        if degree <= 1:
            if curr is self.root:
                self.root = None
            elif is_left_child:
                parent.left = curr.right if curr.right else curr.left
            else:
                parent.right = curr.right if curr.right else curr.left
        elif degree == 2:
            parent = curr
            substitute = curr.right
            is_right_child = True
            while substitute.left is not None:
                parent = substitute
                substitute = substitute.left
                is_right_child = False

            # substitue의 자식 또는 1. 오른쪽 서브트리에서 가장 작은 값을 구하므로 right만 존재.
            curr.key = substitute.key
            curr.val = substitute.val
            if is_right_child:
                parent.right = substitute.right
            else:
                parent.left = substitute.right
        return True

    def delete(self, key: int) -> None:
        self.deleteRecursively(self.root, key)

    def deleteRecursively(self, curr: Optional[Node], key: int):
        if curr is None:
            return None
        if curr.key == key:
            degree = (curr.left is not None) + (curr.right is not None)
            if degree == 0:
                return None
            elif degree == 1:
                return curr.left if curr.left is not None else curr.right
            else:
                substitute = self.findMinInRightSubtree(curr.right)
                curr.key = substitute.key
                curr.val = substitute.val
                # None 또는 subsitute.right 반환
                curr.right = self.deleteRecursively(curr.right, substitute.key)
        elif curr.key < key:
            curr.right = self.deleteRecursively(curr.right, key)
        else:
            curr.left = self.deleteRecursively(curr.left, key)
        return curr

    def findMinInRightSubtree(self, curr: Optional[Node]) -> Node:
        if curr.left is not None:
            return self.findMinInRightSubtree(curr.left)
        return curr

    def dump(self) -> List[int]:
        def dump_subtree(curr: Optional[Node], result: List[int]) -> None:
            if curr is None:
                return
            dump_subtree(curr.left, result)
            result.append(curr.val)
            dump_subtree(curr.right, result)

        result = []
        dump_subtree(self.root, result)
        return result


bst = BST()
# bst.add(3, "수현")
# bst.add(5, "이슬")
# bst.add(2, "진경")
# bst.add(4, "화수")
# print(bst.remove(4))
# print(bst.search(4))
# print(bst.add(4, "화수"))
# print(bst.dump())

bst.add(1, "수연")
bst.add(10, "예지")
bst.add(5, "동혁")
bst.add(12, "원준")
bst.add(14, "민서")
print(bst.search(5))
print(bst.dump())
print(bst.delete(10))
print(bst.dump())
