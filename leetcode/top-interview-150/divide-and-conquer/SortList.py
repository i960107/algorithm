from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 분할 정복 가능한가? 인덱스가 없는데 어떻게 반을 나눠...
    # linked list의 정렬
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(head: Optional[ListNode], total: int):
            # print("head", head.val, "size", total)
            if not head or not head.next:
                return head
            left = head
            left_size = 1

            curr = head
            for _ in range(total // 2 - 1):
                curr = curr.next
                left_size += 1
            right = curr.next
            right_size = total - left_size

            curr.next = None

            # print("left", makeList(left), "right", makeList(right))
            sorted_left = sort(left, left_size)
            sorted_right = sort(right, right_size)
            # 병합 정렬?
            print(makeList(sorted_left), makeList(sorted_right))

            if not sorted_left:
                return sorted_right
            if not sorted_right:
                return sorted_left

            if sorted_left.val > sorted_right.val:
                sortedHead = sorted_right
                sorted_right = sorted_right.next
            else:
                sortedHead = sorted_left
                sorted_left = sorted_left.next

            prev = sortedHead

            while sorted_left and sorted_right:
                if sorted_left.val > sorted_right.val:
                    prev.next = sorted_right
                    prev = sorted_right
                    sorted_right = sorted_right.next
                else:
                    prev.next = sorted_left
                    prev = sorted_left
                    sorted_left = sorted_left.next

            if sorted_left:
                prev.next = sorted_left

            if sorted_right:
                prev.next = sorted_right
            print("sorted", makeList(sortedHead))
            return sortedHead

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        return sort(head, count)


def makeLinkedList(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0], None)
    prev = head
    for i in range(1, len(arr)):
        curr = ListNode(arr[i], None)
        prev.next = curr
        prev = curr
    return head


def makeList(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


s = Solution()
print(s.sortList(makeLinkedList([-1, 5, 3, 4, 0])))
print(s.sortList(makeLinkedList([])))
