from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    '''정렬하여 병합'''
    # intervals.sort(key = lambda x : x[0])
    # O(NLogN)
    intervals.sort()
    result = []

    # O(N)
    for i in range(len(intervals)):
        if result and result[-1][1] >= intervals[i][0]:
            # 당연히 intervals[i][1]이 더 큰 것 아닌가?
            # result[-1][1] = max(result[-1][1],intervals[i][1])
            result[-1][1] = intervals[i][1]
        else:
            result.append(intervals[i])
    return result


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
