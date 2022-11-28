from typing import List, Final

hours: Final = 24
korean_time_offset: Final = 9


def solution(logged_at_datetime: str) -> List[int]:
    logged_at_time = [y for x in logged_at_datetime.split("\n") for i, y in enumerate(x.split(" ")) if i % 2 == 1]

    total_logs_at_time = [0] * hours

    for log in logged_at_time:
        standard_time = int(log[:2])
        korean_time = (standard_time + korean_time_offset) % 24
        total_logs_at_time[korean_time] += 1
    return total_logs_at_time


print(solution(
    "2019/05/01 00:59:19\n2019/06/01 01:35:20\n2019/08/01 02:01:22\n2019/08/01 02:01:23\n2019/08/02 03:02:35\n" +
    "2019/10/03 04:05:40\n2019/10/04 06:23:10\n2019/10/01 08:23:20\n2019/10/01 08:42:24\n2019/10/01 08:43:26\n" +
    "2019/11/01 08:43:29\n2019/11/01 10:19:02\n2019/12/01 11:23:10"))
