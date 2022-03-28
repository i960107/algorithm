from collections import defaultdict
from typing import List
from math import ceil


def solution_parking_fee(fees: List[int], records: List[str]) -> List[int]:
    ins = {}
    parked = defaultdict(int)
    answer = []

    def get_time_between(in_time: str, out_time: str) -> int:
        in_hour, in_min = map(int, ins[car].split(":"))
        out_hour, out_min = map(int, out_time.split(":"))
        # 주차된 시간
        parked_time = (out_hour - in_hour - 1) * 60 + (60 - in_min) + out_min
        return parked_time

    for record in records:
        time, car, behavior = record.split()
        # 입차시
        if behavior == "IN":
            ins[car] = time
        # 출차시
        else:
            # 주차된 시간
            parked[car] += get_time_between(ins[car], time)
            ins.pop(car)
            # # 주차 요금을 세련되게 계산하는 방법? if 문 없이?
            # if parked >= 180:
            #     answer.append()
            # else:
            #     parked - 180

    for car in ins:
        # 입차되었지만 출자안된경우 24시 출차로 간주
        parked[car] += get_time_between(ins[car], "23:59")

    for car in sorted(parked):
        fee = 0
        if parked[car] <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + ceil((parked[car] - fees[0]) / fees[2]) * fees[3]
        answer.append(fee)

        # 차량번호가 작은 차부터
    return answer


print(solution_parking_fee([180, 5000, 10, 600],
                           ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                            "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution_parking_fee([120, 0, 60, 591],
                           ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution_parking_fee([1, 461, 1, 10], ["00:00 1234 IN"]))
