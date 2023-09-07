class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    LOAD_FACTOR = 0.75

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
        index = self.getHashing(key)
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
        self.numberOfItems -= 1

    def put(self, key: str, value: str) -> bool:
        index = self.getHashing(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value, None)
            self.numberOfItems += 1
        else:
            # 같은 key 값이 존재하는 경우 실패.
            head = self.table[index]
            curr = head
            duplicated = False
            while curr:
                if curr.key == key:
                    curr.value = value
                    duplicated = True
                    break
                curr = curr.next
            if not duplicated:
                self.table[index] = Node(key, value, head)
            self.numberOfItems += 1
            if self.isResizeRequired():
                self.resize()

    def resize(self):
        newTable = [None] * (self.capacity * 2)
        for i in range(self.capacity):
            newTable[i] = self.table[i]
        self.capacity *= 2
        self.table = newTable

    def isResizeRequired(self) -> bool:
        return self.numberOfItems / self.capacity >= self.LOAD_FACTOR

    def getHashing(self, key: str) -> int:
        return key.__hash__() % self.capacity
