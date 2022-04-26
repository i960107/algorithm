from typing import List


class ListNode:
    '''definition of singly-linked list'''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_merge_sort(head: ListNode) -> ListNode:
    '''병합 정렬'''
    # 연결리스트의 정렬 결과도 연결 리스트

    # 연결리스트는 전체 길이를 알 수 없기 때문에 runner기법 활용
    # slow는 한칸씩, fast는 두칸씩 앞으로 이동
    # fast가 맨 끝에 도달했을때 slow는 중앙에 도착해 있을 것.
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    # half의 위치를 기준으로 연결리스트 관계를 끊어버리기
    half.next = None

    # divide head - half, slow - 끝가지
    l1 = linked_list_merge_sort(head)
    l2 = linked_list_merge_sort(slow)

    # conquer - merge
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        # l1의 포인터를 이동하면서 정렬해 리턴한다
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = mergeTwoLists(l1.next, l2)
        # l1이 있다면 l1 l1이 없다면 l2
        return l1 or l2

    return mergeTwoLists(l1, l2)


def linked_list_quick_sort(head: ListNode) -> List[int]:
    '''퀵 정렬'''
    # 연결 리스트는 특성상 피벗을 고정된 위치로 지정할 수 밖에 없고
    # 입력값에 따라 성능의 편차가 심하므로 병합 정렬이 적합
    # 퀵 정렬은 대표적인 불안정 정렬로, 같은 값이 반복될 경우 계속해서 스왑을 시도해서 timeout이 발생
    # 퀵 정렬의 어려움. 피벗을 원하는 형태로 설정하기 어려우며 이미 정렬되어 있을 겨웅 계속해서 불균형 리스트로 나뉜다는 점.
    pass


def linked_list_sort_module(head: ListNode) -> ListNode:
    '''내장함수활용'''
    # 기본 라이브러리의 정렬 함수는 C로 신중하게 구현한 팀소트로 가장 빠르다

    # 연결리스트 -> 파이썬 리스트
    lst: List[int] = []
    p = head
    while p:
        lst.append(p.val)
        p = p.next

    # 정렬
    lst.sort()

    # 파이썬 리스트 -> 연결 리스트
    # 링크를 살려두고 활용. 값만 교체 해주기
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head