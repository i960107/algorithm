import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    '''개별 체이닝 방식을 이용한 해시 테이블 구현'''

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int):
        index = self.__hashCode__(key)

        if not self.table[index].key:
            self.table[index] = ListNode(key, value)
            return

        pointer = self.table[index]

        while pointer:
            if pointer.key == key:
                pointer.value = value
                break

            if not pointer.next:
                pointer.next = ListNode(key, value)
                break

            pointer = pointer.next

    def __hashCode__(self, key):
        print("myHashCode", self.__hashCode__(key))
        print("hash", key.__hash__())
        return key % self.size

    def get(self, key: int) -> int:
        index = self.__hashCode__(key)

        p = self.table[index]

        while p:
            if p.key == key:
                return p.value
            p = p.next

        return - 1

    def remove(self, key: int):
        index = self.__hashCode__(key)

        # 첫번째 노드가 삭제할 노드인 경우!
        prev = None
        curr = self.table[index]

        while curr:
            if curr.key == key:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
