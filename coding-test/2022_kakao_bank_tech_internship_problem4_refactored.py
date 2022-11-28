from typing import List, Final
from collections import deque
import heapq


class Job:
    def __init__(self, requested_at: int, duration: int, job_type: int, priority: int):
        self.requested_at = requested_at
        self.duration = duration
        self.job_type = job_type
        self.priority = priority


def get_job_sequence(jobs: List[List[int]]) -> int:
    request_list = []

    for job in jobs:
        request_list = Job(job[0], job[1], job[2], job[3])

    pass


print(get_job_sequence(
    [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
print(get_job_sequence([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
print(get_job_sequence([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
print(get_job_sequence([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]))
