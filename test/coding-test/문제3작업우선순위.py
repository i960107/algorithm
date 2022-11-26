import heapq
from typing import List


class Job:
    def __init__(self, requested_at: int, duration: int, job_type: int, priority: int):
        self.requested_at = requested_at
        self.duration = duration
        self.job_type = job_type
        self.priority = priority


class JobPriorityQueue:
    max_priority: int = 101

    def __init__(self):
        self.max_heap: List[Job] = []
        self.job_on_processing: Job = None

    def add_job(self, job: Job):
        if self.job_on_processing.job_type == job.job_type:
            job.priority = 101
        heapq.heappush(self.max_heap, job)

    def pop_job(self) -> Job:
        pass


def solution(jobs: List[List[int]]) -> List[int]:
    pass


print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
