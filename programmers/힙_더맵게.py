# 우선순위 큐 사용
import heapq


# def solution(scoville: list, k: int) -> int:
#     # 다섞어서 음식 하나만 남았는데도 k보다 작을 경우
#     cnt = -1
#     scoville.sort()
#     for i in range(scoville):
#         min, min2 = scoville[i], scoville[i + 1]
#         if min >= k:
#             break
#         else:
#             mixed = scoville[i] + (scoville[i + 1] * 2)
#             # 섞으면 길이가 하나씩 줄어듬
#             # 섞은게 무조건 가장 작은 원소 아닐듯.
#             # 또 정렬해? 처음에 정렬된 리스트 주어지면 섞은 후 자기 자리만 찾아가면 되므로 정렬에는 O(n) 복잡도
#             # O(n^2) 지나치게 높음.
#             if mixed >= k
#             scoville[i + 1] = mixed
#         # 최소 원소를 빠르게 꺼낼 수 있으면 좋겠는
#         # 최소 힙 사용하면 O(logn)
#         # 힙 트리 -최대,최소 원소를 빠르게 찾을 수 있음 O(1) -상수시간
#         # heapfy-주어진 리스트로 heap트리 구성 O(nlogn), insert, remove 함수 구현해서 사용?
#
#     return cnt

def solution(scoville: list, k: int) -> int:
    cnt = 0
    # 리스트 L로부터 min heap 구성
    # O(NlogN)
    heapq.heapify(scoville)

    # O(N)
    while len(scoville) >= 2 and scoville[0] < k:
        cnt +=1
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one + two * 2)

    return cnt if scoville[0] >=k else -1


print(solution([1, 2, 3, 9, 10, 12], 7))
