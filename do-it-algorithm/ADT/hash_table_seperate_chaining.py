class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, capacity):
        self.table = [None] * capacity
        self.capacity = capacity
        self.numberOfItems = 0

    def get(self, key: str):
        index = hash(key)
        if self.table[index] is None:
            return None
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def remove(self, key: str) -> bool:
        index = hash(key)
        if self.table[index] is None:
            return False
        curr = self.table[index]
        prev = None
        while curr:
            if curr.key != key:
                prev = curr
                curr = curr.next
            if prev is not None:
                prev.next = curr.next
            else:
                self.table[index] = curr.next

    def put(self, key: str, value: str) -> bool:
        index = hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value, None)
            return True
        else:
            # 같은 key 값이 존재하는 경우 실패.
            head = self.table[index]
            curr = head
            while curr:
                if curr.key == key:
                    return False
                curr = curr.next
            self.table[index] = Node(key, value, head)

    def __hash__(self, key: str) -> int:
        hash_digest = 0
        for c in key:
            hash_digest += ord(c)

        return hash_digest % self.capacity
