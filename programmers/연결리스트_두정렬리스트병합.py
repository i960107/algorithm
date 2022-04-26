class ListNode:
    '''definition of singly-linked list'''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = mergeTwoLists(l1.next, l2)

    return l1 or l2


def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    '''재귀 구조로 연결'''
    # 괄호를 생략해도 됨. 연산 우선순위 > not and or
    if not l1 or (l2 and l1.val > l2.val):
        # 변수 swap : 파이썬이 지원하는 다중 할당(2개 이상의 변수에 동시에 할당)
        l1, l2 = l2, l1
    # l1, l2 둘다 None일 수 있음!
    if l1:
        l1.next = mergeTwoLists2(l1.next, l2)
    # l1이 None이 되면서 재귀 호출 종료. 값 return
    return l1 or l2


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
result = mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next
