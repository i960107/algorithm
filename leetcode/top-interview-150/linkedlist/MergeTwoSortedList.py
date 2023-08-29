from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2) -> bool:
    head = ListNode(float('inf'), None)
    prev = head
    while l1 and l2:
        if l1.val >= l2.val:
            prev.next = l2
            l2 = l2.next
        else:
            prev.next = l1
            l1 = l1.next
        prev = prev.next
    if l1:
        prev.next = l1
    if l2:
        prev.next = l2
    return head.next


def makeLinkedList(arr: List[int]) -> ListNode:
    head = ListNode(-1, None)
    curr = head
    for n in arr:
        curr.next = ListNode(n, None)
        curr = curr.next
    return head.next


def makeArr(head: ListNode):
    curr = head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


print(makeArr(mergeTwoLists(makeLinkedList([1, 2, 4]), makeLinkedList([1, 3, 4]))))
print(makeArr(mergeTwoLists(makeLinkedList([]), makeLinkedList([]))))
print(makeArr(mergeTwoLists(makeLinkedList([]), makeLinkedList([0]))))
print(makeArr(mergeTwoLists(makeLinkedList([0]), makeLinkedList([0]))))
