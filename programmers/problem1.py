from datetime import datetime


def solution(purchase: list) -> list:
    answer = [0] * 5
    for i, p in enumerate(purchase):
        date = datetime.strptime(p.split()[0], "%Y/%m/%d")
        date_before = datetime.strptime(purchase[i - 1].split()[0], "%Y/%m/%d") if i > 0 else datetime.strptime(
            "2019/01/01", "%Y/%m/%d")
        date_diff = (date -date_before).days
        price = int(p.split()[1])
        accumulated_price = price

        # 최근 30일내 구매금액 계산
        for j in range(i - 1, -1,-1):
            if (date - datetime.strptime(purchase[j].split()[0], "%Y/%m/%d")).days <= 30:
                accumulated_price += int(purchase[j].split()[1])
            else:
                break

        if accumulated_price < 10000:
            # 브론즈
            answer[0] += date_diff
        elif accumulated_price < 20000:
            # 실버
            answer[1] += date_diff
        elif accumulated_price < 50000:
            # 골드
            answer[2] += date_diff
        elif accumulated_price < 100000:
            # 플래티넘
            answer[3] += date_diff
        else:
            # 다이아몬드
            answer[4] += date_diff

    return answer


print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))
print(solution(["2019/01/30 5000", "2019/04/05 1000", "2019/06/10 20000", "2019/08/15 5000", "2019/12/01 100000"]))
