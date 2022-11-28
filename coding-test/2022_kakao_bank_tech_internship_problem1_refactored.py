from typing import List, Final

HOURS: Final = 24
KOREAN_TIME_OFFSET: Final = 24


def get_frequency_count(logs: str) -> List[int]:
    '''로그 발생 횟수'''
    occurred = [0] * 24
    for log in logs.split("\n"):
        utc_date, utc_time = log.split()
        korean_time = (int(utc_time[:2]) + KOREAN_TIME_OFFSET) % 24
        occurred[korean_time] += 1

    return occurred


print(solution(
    "2019/05/01 00:59:19\n2019/06/01 01:35:20\n2019/08/01 02:01:22\n2019/08/01 02:01:23\n2019/08/02 03:02:35\n" +
    "2019/10/03 04:05:40\n2019/10/04 06:23:10\n2019/10/01 08:23:20\n2019/10/01 08:42:24\n2019/10/01 08:43:26\n" +
    "2019/11/01 08:43:29\n2019/11/01 10:19:02\n2019/12/01 11:23:10"))
