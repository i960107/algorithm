class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class BasicLinkedList:
    def __init__(self):
        self.head = None
        self.nodeCount = 0

    def get_length(self) -> int:
        return self.nodeCount

    def concat(self, l2) -> None:
        if self.get_length() == 0:
            self.head = l2.head
        else:
            tail = self.get_at(self.get_length() - 1)
            tail.next = l2.head

    def insert(self, pos: int, node: Node) -> bool:
        if pos == 0:
            if self.head:
                node.next = self.head.next
            self.head = node
        else:
            try:
                prev = self.get_at(pos - 1)
                node.next = prev.next
                prev.next = node
            except IndexError:
                return False
        self.nodeCount += 1
        return True

    def pop(self, pos: int) -> int:
        if pos < 0 or pos > self.nodeCount - 1:
            raise IndexError

        if pos == 0:
            curr = self.head
            self.head = curr.next
        else:
            try:
                prev = self.get_at(pos - 1)
                curr = prev.next
                prev.next = curr.next
            except ValueError:
                return False
        self.nodeCount -= 1
        return curr.data

    def get_at(self, pos: int) -> Node:
        '''pos 번째 원소 가져오기. 원소의 data 반환 아님'''
        # 배열과 마찬가지로 index는 리스트의 길이 -1 까지 존재
        if pos < 0 or pos > self.nodeCount - 1:
            raise IndexError
        i = 0
        curr = self.head
        while i <= pos:
            i += 1
            curr = curr.next

        return curr

    def traverse(self) -> None:
        i = 0
        curr = self.head
        while i < self.nodeCount:
            print(f'{curr.data}', end='   ')
            curr = curr.next
            i += 1


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def getNodeCount(self):
        return self.nodeCount

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.apeend(curr.data)
        return result

    def insertAfter(self, prev, newNode):
        if prev == None or newNode == None:
            return False

        newNode.next = prev.next
        prev.next = newNode

        if prev.next is None:
            self.tail = newNode

        self.nodeCount += 1

        return True


if __name__ == '__main__':
    linkedList = BasicLinkedList()

    while True:
        pos = int(input('삽입할 위치(-1입력시 종료):'))
        if pos == -1:
            break
        value = int(input('삽입할 값:'))
        if not linkedList.insert(pos, Node(value)):
            print('삽입 실패')
        else:
            linkedList.traverse()
            print(f'nodeCount : {linkedList.nodeCount}')
    while True:
        pos = int(input('참조할 원소의 위치(-1 입력시 종료):'))
        if pos == -1:
            break
        try:
            print(linkedList.get_at(pos).data)
        except IndexError:
            print('index error 발생')

    while True:
        pos = int(input('삭제할 위치(-1입력시 종료):'))
        if pos == -1:
            break
        if not linkedList.pop(pos):
            print('삭제 실패')
        else:
            linkedList.traverse()
            print(f'nodeCount : {linkedList.nodeCount}')

    linkedList2 = BasicLinkedList()
    linkedList.concat(linkedList2)
    print('빈 배열 concat : ', end='')
    linkedList.traverse()

    linkedList2.insert(0, Node(10))
    linkedList.concat(linkedList2)
    print('빈 배열 concat : ', end='')
    linkedList.traverse()
