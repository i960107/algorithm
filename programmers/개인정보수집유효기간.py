from typing import List
from datetime import datetime


def solution(today: str, terms: List[str], privacies: List[str]) -> List[int]:
    min_dates = dict()
    y, m, d = map(int, today.split("."))

    # 이왜진...
    # 0년 1월 1일 로부터 몇 일 후인지( currentTimeMillis 개념과 비슷)
    today = y * 12 * 28 + (m - 1) * 28 + (d - 1)
    for term in terms:
        type, duration = term.split()
        min_date = today - int(duration) * 28
        min_dates[type] = min_date

    answer = []
    for index, privacy in enumerate(privacies, 1):
        y, m, d = map(int, privacy.split()[0].split("."))
        registration_date = y * 12 * 28 + (m - 1) * 28 + (d - 1)
        type = privacy.split()[1]
        # if min_dates[type] <= registration_date:
        if min_dates[type] >= registration_date:
            answer.append(index)
    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"],
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
