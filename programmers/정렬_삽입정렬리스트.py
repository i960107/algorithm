from typing import Optional


class ListNode:
    '''definition of singly-linked list'''

    def __init__(self, val: Optional[int] = 0, next=None):
        self.val = val
        self.next = next


def insertion_sort_list(head: ListNode) -> ListNode:
    # O(N^2) 느림
    # 제대로 된 삽입 정렬 아님. 정답 셋의 가장 큰값부터 왼쪽 방향으로 내려가며 스왑되는 위치를 찾는게 삽입정렬.
    # 연결리스트에서는 거슬러 올라가는게 불가능.

    # head는 정렬해야할 대상
    # curr은 정렬 끝난 대상

    # parent는 정렬 끝난 연결리스트의 head를 가리키고
    # curr은 head가 추가될 위치는 가리킴. curr에 삽입되어야함?. curr 다음에 삽입되어야함.

    curr = parent = ListNode(None)
    while head:
        while curr.next and curr.next.val < head.val:
            curr = curr.next

        # curr.next = None이거나 curr.next.val >= head.val인 경우
        # 정렬된 리스트에 삽입 and 정렬대상 리스트에서 삭제
        curr.next, head.next, head = head, curr.next, head.next
        # 처음부터 다시 탐색
        curr = parent
    # cur은 parent 즉, None을 가리키는 상태이므로 첫번재 유효한 노드 Return해야
    return curr.next


def insertion_sort_list_improved(head: ListNode) -> ListNode:
    # Node가 None이면 curr.val 비교시 에러발생하므로  0으로 수정
    curr = parent = ListNode(0)
    while head:
        while curr.next and curr.next.val < head.val:
            curr = curr.next

        # curr.next = None이거나 curr.next.val >= head.val인 경우
        # 정렬된 리스트에 삽입 and 정렬대상 리스트에서 삭제
        curr.next, head.next, head = head, curr.next, head.next
        # 처음부터 다시 탐색x.만약 다음 head가 여전히 curr보다 크다면 바로 다음에 삽입해주면 됨.
        if head and head.val < curr.val:
            curr = parent
    # cur은 parent 즉, None을 가리키는 상태이므로 첫번재 유효한 노드 Return해야
    return curr.next


head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
node = insertion_sort_list(head)
while node:
    print(node.val, end=" ")
    node = node.next
