from typing import List, Final, Deque, Union, Tuple, Set
from collections import deque
import heapq


class Job:
    def __init__(self, requested_at: int, duration: int, job_type: int, priority: int):
        self.priority = priority
        self.requested_at = requested_at
        self.duration = duration
        self.job_type = job_type

    def __lt__(self, other) -> bool:
        if self.priority > other.priority:
            return True
        elif self.priority == other.priority:
            return self.job_type < other.job_type
        else:
            return False


class JobRequests:
    def __init__(self):
        self.jobs: Deque[Job] = deque()

    def has_new_request(self, now: int) -> bool:
        return self.jobs and self.jobs[0].requested_at == now

    def add_request(self, job: Job):
        self.jobs.append(job)

    def popleft_request(self) -> Job:
        return self.jobs.popleft()

    def has_request_left(self):
        return len(self.jobs) != 0


class JobOnProcessing:
    def __init__(self, job: Job, start_at: int):
        self.job = job
        self.start_at = start_at
        self.end_at = start_at + job.duration

    def get_job_type(self) -> int:
        return self.job.job_type


class JobProcessor:
    def __init__(self):
        self.jobs: List[JobOnProcessing] = []
        self.queue: JobQueue = JobQueue()

    def is_occupied(self, now: int) -> bool:
        if now < 0:
            return False
        return self.jobs and self.jobs[-1].end_at > now

    def get_current_job(self, now) -> Union[JobOnProcessing, None]:
        if not self.is_occupied(now):
            return None
        return self.jobs[-1]

    def get_current_job_type(self, now: int) -> Union[int, None]:
        if now < 0 or not self.jobs:
            return None
        return self.jobs[-1].get_job_type()

    def switch(self, now):
        if self.is_occupied(now):
            return
        new_job = self.queue.pop_left()
        if not new_job:
            return
        if self.jobs and new_job.job_type == self.get_current_job_type(now):
            self.jobs[-1].job.priority += new_job.job_type
            self.jobs[-1].end_at += new_job.duration
            return
        self.jobs.append(JobOnProcessing(new_job, now))

    def has_job_on_queue(self) -> bool:
        return self.queue.has_job_on_queue()

    def add_to_job_queue(self, job: Job, now: int):
        self.queue.add(job, self.get_current_job_type(now))


class JobQueue:
    MAX_PRIORITY: Final = 100 + 1
    MAX_PRIORITY_SUM: Final = 100 * 100 + 1

    def __init__(self):
        self.queue: List[Job] = []
        self.waiting_job_types: Set[int] = set()

    def has_job_on_queue(self) -> bool:
        return len(self.queue) > 0

    def add(self, job: Job, job_on_processing_type: int):
        if not job:
            return
        if job_on_processing_type == job.job_type:
            job.priority = self.MAX_PRIORITY_SUM

        if job.job_type in self.waiting_job_types:
            for x in self.queue:
                if x.job_type == job.job_type:
                    x.priority += job.priority
                    x.duration += job.duration
                    break
        else:
            self.queue.append(job)
        self.waiting_job_types.add(job.job_type)
        heapq.heapify(self.queue)

    def pop_left(self) -> Union[Job, None]:
        if not self.queue:
            return None
        job = heapq.heappop(self.queue)
        self.waiting_job_types.remove(job.job_type)
        return job


def get_job_sequence(jobs: List[List[int]]) -> List[int]:
    # 들어온 순서대로
    jobRequests = JobRequests()

    for job in jobs:
        jobRequests.add_request(Job(job[0], job[1], job[2], job[3]))

    # 우선순위에 따라 정렬된
    job_processor = JobProcessor()

    now = -1

    while jobRequests.has_request_left() or job_processor.has_job_on_queue():
        now += 1

        if jobRequests.has_new_request(now):
            job_processor.add_to_job_queue(jobRequests.popleft_request(), now)
        job_processor.switch(now)

    return [job.get_job_type() for i, job in enumerate(job_processor.jobs)]


print(get_job_sequence(
    [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
print(get_job_sequence([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
print(get_job_sequence([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
print(get_job_sequence([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]))
