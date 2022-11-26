from typing import List, Final
from datetime import time


def get_occurred_counter(logs: str) -> List[int]:
    KOREAN_TIME_OFFSET: Final = 9
    occurred = [0] * 24
    for log in logs.split("\n"):
        utc_date, utc_time = log.split()
        korean_time = (int(utc_time[:2]) + KOREAN_TIME_OFFSET) % 24
        occurred[korean_time] += 1

    return occurred


print(get_occurred_counter("2019/05/01 00:59:19\n2019/06/01 01:35:20\n2019/12/01 11:23:10"))
