class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # AttributeError발생-> None의 next을 참조하려고 하기 때문
        # self.head.next = self.tail
        # self.head = Node(None)이 아님 주의. Node(None) dummy head
        self.node_count = 0

    def get_length(self) -> int:
        return self.node_count

    # return self 가능
    def concat(self, l2) -> None:
        if self.node_count == 0:
            self.head = l2.head
            self.tail = l2.tail
        else:
            # node_count !=0이기 때문에 self.tail != None
            self.tail.next = l2.head
            if l2.tail:
                self.tail = l2.tail

        self.node_count += l2.node_count

    def insert_at(self, pos: int, node: Node) -> bool:
        # get_at() 및 pop_at() 과 유효한 index 범위 다름 주의!
        if pos < 1 or pos > self.get_length() + 1:
            return False

        #Node는 생성시 next = None으로 초기화되기 때문에
        #node.next = None인 상태
        if pos == 1:
            # 빈 배열이었을경우 node.next = None
            # self.head != None이었을경우 node.next = self.head
            # tail 조정 조건문 끝난 후 처리
            node.next = self.head
            self.head = node
        else:
            prev = self.get_at(pos - 1)
            node.next = prev.next
            prev.next = node

        # 빈배열에 삽입하는 경우 혹은 빈배열이 아닐때 tail에 삽입하는 경우
        # 조건문 밖에서 두가지 경우 다 커버해야 하는 것 명심!
        if pos == self.get_length() + 1:
            self.tail = node
        self.node_count += 1
        return True

    def pop_at(self, pos: int) -> int:
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
        # index 는 1부터 시작- 어떤 이점? 이후에 0번째 인덱스에 dummy head 추가하기 위함
        if pos < 1 or pos > self.get_length():
            raise IndexError

        # tail 반환 O(1) 복잡도
        if pos == self.get_length():
            return self.tail

        i = 1
        curr = self.head

        while i < pos:
            i += 1
            curr = curr.next

        return curr

    def traverse(self) -> list:
        curr = self.head
        l = []

        # index 비교 필요 없이 curr이 None인지로 배열의 끝 판단
        while curr:
            l.append(curr.data)
            curr = curr.next
        return l


if __name__ == '__main__':
    linkedList = LinkedList()

    '''삽입 테스트'''
    while True:
        pos = int(input('삽입할 위치(-1입력시 종료):'))
        if pos == -1:
            break
        value = int(input('삽입할 값:'))
        if not linkedList.insert_at(pos, Node(value)):
            print('삽입 실패')
        else:
            linkedList.traverse()
            print(f'node_count : {linkedList.node_count}')
    '''참조 테스트'''
    while True:
        pos = int(input('참조할 원소의 위치(-1 입력시 종료):'))
        if pos == -1:
            break
        try:
            print(linkedList.get_at(pos).data)
        except IndexError:
            print('index error 발생')

    '''삭제 테스트'''
    while True:
        pos = int(input('삭제할 위치(-1입력시 종료):'))
        if pos == -1:
            break
        if not linkedList.pop_at(pos):
            print('삭제 실패')
        else:
            linkedList.traverse()
            print(f'node_count : {linkedList.node_count}')

    linkedList2 = LinkedList()
    linkedList.concat(linkedList2)
    print('빈 배열 concat : ', end='')
    print(linkedList.traverse())

    linkedList2.concat(linkedList)
    print('빈 배열 + 배열 concat', end='')
    print(linkedList2.traverse())

    linkedList2.insert_at(0, Node(10))
    linkedList.concat(linkedList2)
    print('빈 배열 concat : ', end='')
    print(linkedList.traverse())
