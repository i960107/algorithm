from typing import List, Final
from collections import deque
import heapq


class Job:
    def __init__(self, requested_at: int, duration: int, job_type: int, priority: int):
        self.requested_at = requested_at
        self.duration = duration
        self.job_type = job_type
        self.priority = priority


class Job_Group:
    def __init__(self, job_type: int, total_duration: int, total_priority: int):
        self.job_type = job_type
        self.total_duration = total_duration
        self.total_priority = total_priority

    def __lt__(self, other):
        if self.total_priority > other.total_priority:
            return True
        elif self.total_priority == other.total_priority:
            return self.job_type < other.job_type
        else:
            return False


class Job_Group_Processing:
    def __init__(self, JobGroup: Job_Group, start_at: int, end_at: int):
        self.JobGroup = JobGroup
        self.start_at = start_at
        self.end_at = end_at


def solution(jobs: List[List[int]]) -> List[int]:
    request_list: deque = deque()
    for job in jobs:
        request_list.append(Job(job[0], job[1], job[2], job[3]))

    job_order = []

    queue: list = []
    waiting_job_type_set: set = set()
    current: Job_Group_Processing = None
    now = -1

    def update(request: Job):
        nonlocal queue
        priority_increasement = request.priority if not current or request.job_type != current.JobGroup.job_type else 0
        for job_group in queue:
            if job_group.job_type == request.job_type:
                job_group.total_priority += priority_increasement
                job_group.total_duration += request.duration

    def add(request: Job):
        priority = request.priority if not current or request.job_type != current.JobGroup.job_type else max_priority
        queue.append(Job_Group(request.job_type, request.duration, priority))

    def update_or_add_request(request: Job):
        if request.job_type in waiting_job_type_set:
            update(request)
        else:
            add(request)
        waiting_job_type_set.add(request.job_type)

    def has_new_request():
        if request_list and request_list[0].requested_at == now:
            return True
        return False

    def is_occupied() -> bool:
        return current and current.end_at > now

    while request_list or queue:
        now += 1

        if has_new_request():
            request = request_list.popleft()
            update_or_add_request(request)

        if is_occupied():
            continue

        if not queue:
            continue

        heapq.heapify(queue)
        current_job = heapq.heappop(queue)
        current = Job_Group_Processing(current_job, now, now + current_job.total_duration)
        waiting_job_type_set.remove(current.JobGroup.job_type)
        if not job_order or job_order[-1] != current.JobGroup.job_type:
            job_order.append(current.JobGroup.job_type)

    return job_order


print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
print(solution([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]))
