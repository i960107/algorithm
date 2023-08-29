from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 즉 0 ~ 9 * 10^99 나타낼 수 있다.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2

        head = ListNode(-1, None)
        prev = head
        # 새로운 노드를 만들지 말고 둘 중의 긴 노드를 기준으로?
        up = False
        while p1 or p2 or up:
            sum = (p1.val if p1 else 0) + (p2.val if p2 else 0) + up
            if sum >= 10:
                up = True
                sum -= 10
            else:
                up = False

            new_node = ListNode(sum, None)
            prev.next = new_node
            prev = new_node

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return head.next

    # l1, l2자체가 포인터
    # l2 l2의 합을 l1에 더해감. l1, l2 둘 중 하나 끝날때까지
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        prev = None

        carry_over = 0
        while l1 and l2:
            raw_val = carry_over + l1.val + l2.val

            l1.val = raw_val % 10
            carry_over = raw_val // 10

            prev = l1
            l1 = l1.next
            l2 = l2.next

        if l2:
            prev.next = l2
            l1 = l2

        while l1:
            raw_val = carry_over + l1.val
            l1.val = raw_val % 10
            carry_over = raw_val // 10
            prev = l1
            l1 = l1.next

        if carry_over > 0:
            prev.next = ListNode(carry_over)

        return head


def makeLinkedList(arr: List[int]) -> ListNode:
    head = ListNode(-1, None)
    curr = head
    for n in arr:
        curr.next = ListNode(n, None)
        curr = curr.next
    return head.next


def makeNum(head: ListNode):
    curr = head
    num = 0
    while curr:
        num *= 10
        num += curr.val
        curr = curr.next
    return num


s = Solution()

l1 = makeLinkedList([2, 4, 3])
l2 = makeLinkedList([5, 6, 4])

s.addTwoNumbers(l1, l2)

print(makeNum(s.addTwoNumbers(makeLinkedList([9, 9, 9, 9, 9, 9, 9]), makeLinkedList([9, 9, 9, 9]))))
print(makeNum(s.addTwoNumbers(makeLinkedList([0]), makeLinkedList([0]))))
print(makeNum(s.addTwoNumbers(makeLinkedList([2, 4, 3]), makeLinkedList([5, 6, 4]))))
