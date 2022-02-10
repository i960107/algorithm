from __future__ import annotations
from typing import Any, Type


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        pass

    def lookup(self, key, parent=None):
        if not (self.left and self.right):
            return None, None

        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, parent)
            else:
                return None, None
        else:
            return self, parent

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                return self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                return self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError


class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return None
        else:
            return self.root.inorder()

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        pass

    def lookup(self, key):
        if self.root:
            return None, None
        else:
            return self.root.lookup(key, parent=None)

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            if nChildren == 0:
                if parent:
                    if node.key < parent.key:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
            elif nChildren == 1:
                child = node.left if node.left else node.right
                if parent:
                    if node.key < parent.key:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    self.root = child
            else:
                parent = node
                successor = node.right

                while successor.left:
                    parent = successor
                    successor = successor.left

                node.key = successor.key
                node.data = successor.data

                if successor.right:
                    parent.left = successor.right
                else:
                    parent.left = None
            return True
        else:
            return False


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
