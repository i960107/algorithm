from typing import Optional, List, Any
from functools import reduce


class ListNode:
    def __init__(self, val: Any, next=None):
        self.val = val
        self.next = next


def add_two_numbers(head1: ListNode, head2: ListNode):
    def reverseList(head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(node: ListNode) -> List[int]:
        '''덧셈 연산을 위해 연결리스트를 파이썬의 리스트로'''
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(result: str) -> ListNode:
        prev: Optional[ListNode] = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    a = toList(reverseList(head1))
    b = toList(reverseList(head2))

    # resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))
    resultStr = reduce(lambda x, y: 10 * x + y, a, 0)
    resultStr += reduce(lambda x, y: 10 * x + y, b, 0)

    return toReversedLinkedList(str(resultStr)).val


def add_two_number_full_adder(l1: ListNode, l2: ListNode):
    '''전가산기 구현'''
    # root 임의의 head
    root = curr = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        total = 0
        if l1:
            total += l1.val
            l1 = l1.next

        if l2:
            total += l2.val
            l2 = l2.next

        carry, val = divmod(total + carry, 10)
        curr.next = ListNode(val)
        head = curr.next
    return root.next

    # 입력값 A,B 이전의 자리 올림수(Carry in) => 합, 다음 자리올림수(carry out)


print(add_two_numbers(head1=ListNode(2, ListNode(4, ListNode(3))), head2=ListNode(5, ListNode(6, ListNode(4)))))
