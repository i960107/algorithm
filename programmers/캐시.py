from typing import List
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    HIT = 1
    MISS = 5

    head = [None, None, None, None]
    tail = [None, None, None, None]
    head[3] = tail
    tail[2] = head

    look_up = dict()
    size = 0

    answer = 0

    def remove(node):
        nonlocal size
        prev_node = node[2]
        next_node = node[3]
        prev_node[3] = next_node
        next_node[2] = prev_node

        del look_up[node[0]]
        size -= 1

    def put(node):
        nonlocal size
        last_node = tail[2]
        last_node[3] = node
        node[2] = last_node
        node[3] = tail
        tail[2] = node
        look_up[node[0]] = node
        size += 1

    for city in cities:
        city = city.lower()
        if city in look_up:
            answer += HIT
            remove(look_up[city])
        else:
            answer += MISS
            if size == cacheSize:
                lru = head[3]
                remove(lru)
        node = [city, None, None, None]
        put(node)

    return answer


# LRU cache 알고리즘 기본
cache_size = 3
reference = [4, 2, 3, 4, 5, 6, 5, 4, 7]
# 페이지 교체가 일어날때 O(N). -> linked list 사용.
cache = []
cached = 0
for ref in reference:
    if ref not in cache:
        if len(cache) < cache_size:
            cache.append(ref)
        else:
            cache.pop()
            cache.append(ref)
    else:
        cache.pop(cache.index(ref))
        cache.append(ref)

'''linked list  + hash table 사용 LRU 캐시 구현'''


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, max_size: int):
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = max_size
        self.curr_size = 0
        # key : Node
        self.node_lookup = {}

    def removeNode(self, node):
        node_nxt = node.nxt
        node_prev = node.prev
        node_prev.nxt = node_nxt
        node_nxt.prev = node_prev
        del self.node_lookup[node]
        self.curr_size -= 1

    def addNodeToLast(self, node):
        last_node = self.tail.prev
        last_node.next = node
        self.tail.prev = node
        node.prev = last_node
        node.next = self.tail
        self.curr_size += 1
        self.node_lookup[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.node_lookup:
            return -1
        node = self.node_lookup[key]
        return node

    def put(self, key: int, val: int):
        if key in self.node_lookup:
            node = self.node_lookup[key]
            self.removeNode(node)
            self.addNodeToLast(node)
        else:
            if self.curr_size == self.max_size:
                lru_node = self.head.next
                self.removeNode(lru_node)
            now = Node(key, val)
            self.addNodeToLast(now)

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2,
#                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
#                 "Rome"]))
