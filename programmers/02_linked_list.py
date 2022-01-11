class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.node_count = 0

    def get_node_count(self) -> int:
        return self.node_count

    def concat(self, l2) -> None:
        # 예외) 앞 배열이 빈 경우. (뒷 배열이 빈 경우 상관없음)
        if self.get_node_count() == 0:
            self.head = l2.head
        else:
            tail = self.get_at(self.get_node_count())
            tail.next = l2.head

        self.node_count += l2.node_count

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
        self.node_count += 1
        return True

    def pop(self, pos: int) -> int:
        if pos < 0 or pos > self.node_count - 1:
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
        self.node_count -= 1
        return curr.data

    def get_at(self, pos: int) -> Node:
        # pos 번째 원소 가져오기. 원소의 data 반환 아님
        # index 는 1부터 시작- 어떤 이점? 마지막 index가 nodeCount랑 같음
        if pos < 1 or pos > self.get_node_count():
            raise IndexError

        i = 1
        curr = self.head

        while i < pos:
            i += 1
            curr = curr.next

        return curr

    def traverse(self) -> list:
        curr = self.head
        l = []

        #index 비교 필요 없이 curr이 None인지로 배열의 끝 판단
        while curr:
            l.append(curr.data)
            curr = curr.next
        return l


class LinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def getnode_count(self):
        return self.node_count

    def getAt(self, pos):
        if pos < 0 or pos > self.node_count:
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

        self.node_count += 1

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
            print(f'node_count : {linkedList.node_count}')
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
            print(f'node_count : {linkedList.node_count}')

    linkedList2 = BasicLinkedList()
    linkedList.concat(linkedList2)
    print('빈 배열 concat : ', end='')
    linkedList.traverse()

    linkedList2.insert(0, Node(10))
    linkedList.concat(linkedList2)
    print('빈 배열 concat : ', end='')
    linkedList.traverse()
