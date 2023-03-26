from typing import List
from datetime import datetime


def solution(today: str, terms: List[str], privacies: List[str]) -> List[int]:
    date_format = "%Y.%m.%d"
    min_dates = dict()
    today = datetime.strptime(today, date_format)
    for term in terms:
        type, duration = term.split()
        duration = int(duration)
        min_year = today.year + ((today.month - duration) // 12)
        min_month = (today.month - duration) % 12
        min_dates[type] = datetime(min_year, min_month, today.day)
    for type, min_date in min_dates.items():
        print(type, min_date)

    answer = []
    for index, privacy in enumerate(privacies, 1):
        registration_date = datetime.strptime(privacy.split()[0], date_format)
        type = privacy.split()[1]
        if min_dates[type] >= registration_date:
            answer.append(index)
    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"],
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
