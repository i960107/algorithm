from typing import List
from dateutil.relativedelta import relativedelta
from datetime import datetime


def solution(today: str, ters: List[str], privacies: List[int]) -> List[int]:
    # print(list(map(int, today.split("."))))
    today = datetime(*map(int, today.split(".")))
    print(today)

    pass


print(solution("2021.12.12", None, None))
# print(solution())
# print(solution())
