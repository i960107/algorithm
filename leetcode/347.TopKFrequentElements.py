from typing import List, Tuple
from collections import Counter
import heapq


def topK_frequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    return [num for num, cnt in counter.most_common(k)]


def topK_frequent2(nums: List[int], k: int) -> Tuple[int]:
    '''pythonic way'''
    return list(zip(*Counter(nums).most_common(k)))[0]


def topK_frequent3(nums: List[int], k: int) -> List[int]:
    '''counter + heapq'''
    freqs = Counter(nums)
    freqs_heap = []

    for num, cnt in freqs.items():
        heapq.heappush(freqs_heap, (-cnt, num))

    topk = []
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk


print(topK_frequent([1, 1, 1, 2, 2, 3], 2))
print(topK_frequent([1], 1))
print(topK_frequent2([1, 1, 1, 2, 2, 3], 2))
print(topK_frequent2([1], 1))
print(topK_frequent3([1, 1, 1, 2, 2, 3], 2))
print(topK_frequent3([1], 1))


