from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, key: int, item: Any = None):
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def size(self) -> int:
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self) -> int:
        # 최대 level +1
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    def inorder_traverse(self) -> list:
        traversal = []
        if self.left:
            # list합치기
            # append() : 반환된 리스트 자체를 리스트에 원소로 추가하기 때문에 중첩된 리스트 생성됨
            # += :  반환된 리스트를 concat하기 때문에 여기서는 +=를 써줘야함.
            traversal += (self.left.inorder_traverse())
        traversal.append(self.key)
        if self.right:
            traversal += (self.right.inorder_traverse())
        return traversal

    def lookup(self, key: int, parent=None) -> tuple[Node | None, Node | None]:
        # 재귀적으로 사용하기 위해서 매개변수에 parent필요. root는 parent 없으므로 default값 정해주기

        # 왼쪽 서브 트리를 탐색해야할때
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        # 오른쪽 서브 트리를 탐색해야할때
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        # 지금 노드가 검색하는 값일때
        else:
            return self, parent

    def insert(self, key: int, item: Any = None):
        if key < self.key:
            if self.left:
                return self.left.insert(key, item)
            else:
                self.left = Node(key, item)
        elif key > self.key:
            if self.right:
                return self.right.insert(key, item)
            else:
                self.right = Node(key, item)
        else:
            # 중복 값 넣을 수 없음
            raise KeyError


class BinarySearchTree:
    def __init__(self, root: Node = None):
        # root 없이 빈 트리 생성할 수 있도록 root 기본값 정해주기
        self.root = root

    def size(self) -> int:
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self) -> int:
        if self.root:
            return self.root.depth()
        else:
            return 0

    def insert(self, key: int, item: Any = None):
        # 이진 검색 트리는 삽입되는 위치 key에 따라 정해짐
        if self.root:
            self.root.insert(key, item)
        else:
            self.root = Node(key, item)

    def remove(self, key: int) -> bool:
        pass

    def lookup(self, key: int) -> tuple[Node | None, Node | None]:
        # 찾은 노드와, 부모노드를 반환 -> remove()에 사용됨
        # 값 여러개 반환시 tuple로 반환됨. type 힌트 주의

        if self.root:
            return None, None
        else:
            return self.root.lookup(key, None)

    def inorder_traverse(self) -> list:
        # 이진 검색트리의 중위 순회 결과는 오름차순 정렬되어있음
        if self.root:
            return self.root.inorder_traverse()
        else:
            return []

    def max(self) -> int | None:
        # 재귀적으로도 구현 가능
        # 이렇게 정의하면 문제점은?
        # 가장 작은 key 값 혹은 빈트리일지 None 반환. type hint : from__future__ import annotations로 |로 가능.
        if self.root:
            curr = self.root
            while curr.right:
                curr = curr.right
            return curr
        else:
            return None

    def min(self) -> int | None:
        if self.root:
            curr = self.root
            while curr.left:
                curr = curr.left
            return curr
        else:
            return None


bst = BinarySearchTree()
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(4)
bst.insert(9)
bst.insert(7)
print(bst.inorder_traverse())

# ------------------------------------------
'''doit 자료구조와 함께 배우는 알고리즘 입문 이진 검색 트리 구현'''


class DoNode:
    def __init__(self, key: Any, value: Any, left: DoNode = None, right: DoNode = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class DoBinarySearchTree:
    def __init__(self):
        # 빈 이진트리로 생성
        self.root = None

    def search(self, key: Any) -> Any:
        '''키 값으로 노드를 검색 후 노드의 value를 반환'''
        pass

    def add(self, key: Any, value: Any) -> bool:
        '''키가 key이고 값이 value인 노드를 삽입'''
        pass

    def remove(self, key: Any) -> bool:
        '''키가 key인 노드를 삭제'''
        pass

    def dump(self) -> None:
        '''모든 노드를 키의 오름차순으로 출력'''
        pass

    def min_key(self):
        '''최소 키를 반환'''
        pass

    def max_key(self):
        '''최대 키를 반환'''
        pass
