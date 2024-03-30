from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        new_list = ListNode()
        new_list_dummy = new_list
        left_pos = set(i for i, x in enumerate(lists) if x is not None)

        while left_pos:
            nxt_l_pos = -1
            for i in left_pos:
                if nxt_l_pos == -1 or lists[i].val < lists[nxt_l_pos].val:
                    nxt_l_pos = i
            new_list.next = ListNode(lists[nxt_l_pos].val, None)
            new_list = new_list.next
            lists[nxt_l_pos] = lists[nxt_l_pos].nxt
            if lists[nxt_l_pos] is None:
                left_pos.remove(nxt_l_pos)

        return new_list_dummy.next

    # divide and conquer
    # 어떻게 linked list 를 분할 정렬하지?
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        # 매 번 정렬이 유지되어야하는게 아니면 마지막 한번에 정렬하는 것이 나음
        # append O(1), 정렬은 O(NLogN). 파이썬 내부적으로 최적화되어있음
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values.sort()
        node = ListNode()
        dummy = node
        for v in values:
            node.next = ListNode(v, None)
            node = node.next
        return dummy.next
