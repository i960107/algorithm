from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head: ListNode) -> bool:
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False


def hasCycle2(head: ListNode) -> bool:
    s = f = head

    while f and f.next:
        s = s.next
        f = f.next.next
        if f == s:
            return True
    return False


def makeLinkedList(arr: List[int]) -> ListNode:
    head = ListNode(-1, None)
    curr = head
    for n in arr:
        curr.next = ListNode(n, None)
        curr = curr.next
    return head.next
