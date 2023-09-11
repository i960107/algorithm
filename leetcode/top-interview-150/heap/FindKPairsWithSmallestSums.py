import heapq
from typing import List


class Solution:
    # 오른차순 정렬된 배열, 중복값 있음
    # 둘다 빈 배열일 수 없다
    # 음수 포함
    # 각 배열에서 원소 하나씩 추출한 쌍 n * m개 중 가장 합이 작은 것 k개
    # 투포인터O(K), heapO((N + M)Log(N + M))
    # 투포인터 안되는 이유 갔다가 되돌아야함.
    # AllPossiblePairs가 return 되는 경우 N * M <= K인 경우도 주어짐
    def kSmallestPairs_fail(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        count = 0
        p1 = p2 = 0
        result = []
        while count < k:
            result.append([nums1[p1], nums2[p2]])
            if nums1[p1 + 1] <= nums2[p2 + 1]:
                p1 += 1
            else:
                p2 += 1
            count += 1
        return result

    # 전체를 저장하는 배열이 필요 -> memory limit excceed 발생
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                result.append([nums1[i], nums2[j]])
        result.sort(key=lambda x: x[0] + x[1])
        return result[:k]

    # 왜 heap일까 어떻게 heap을 사용할 수 있지?
    # sum이 같다면 [1,2] [2,1] 어떤 순서로 반환되어도 좋음
    # 그 뒤에 나올 수 있는 가장 작은 수와 비교하는 것은 의미없음 그 뒤 숫자들도 비교해야 하므로
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        for i in range(len(nums1)):
            max_sum = nums1[i + 1] + nums2[0] if i + 1 < len(nums1) else float('INF')
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] > max_sum or len(result) >= k:
                    break
                result.append([nums1[i], nums2[j]])
            if len(result) >= k:
                break

        return result

    def kSmallestPairs3(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        resV = []
        pq = []

        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])

        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]

            resV.append([s - nums2[pos], nums2[pos]])

            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])
            k -= 1
        return resV


s = Solution()
print(s.kSmallestPairs2(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
print(s.kSmallestPairs2(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
print(s.kSmallestPairs2(nums1=[1, 2], nums2=[3], k=3))
print(s.kSmallestPairs2(nums1=[1, 2], nums2=[3], k=1))
print(s.kSmallestPairs2(nums1=[1, 1, 1], nums2=[1, 1, 1], k=9))
