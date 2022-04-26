from typing import Optional


class ListNode:
    '''definition of singly-linked list'''

    def __init__(self, val: Optional[int] = 0, next=None):
        self.val = val
        self.next = next


def insertion_sort_list(head: ListNode) -> ListNode:
    # head는 정렬해야할 대상
    # curr은 정렬 끝난 대상

    # parent는 정렬 끝난 연결리스트의 head를 가리키고
    # curr은 head가 추가될 위치는 가리킴. curr에 삽입되어야함?. curr 다음에 삽입되어야함.
    curr = parent = ListNode(None)
    while head:
        while curr.next and curr.next.val < head.val:
            curr = curr.next

        curr.next, head.next, head = head, curr.next, head.next
        curr = parent
    return curr.next


head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
node = insertion_sort_list(head)
while node:
    print(node.val, end=" ")
    node = node.next
