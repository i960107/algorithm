from typing import List
from itertools import product


def solution(users: List[List[int]], emoticons: List[int]) -> List[int]:
    discounts = [10, 20, 30, 40]

    # 할인율 조합별 이모티콘 플러스 가입자수
    max_emo_plus_users = 0
    max_emo_sales = 0

    for discount_per_emoticons in product(discounts, repeat=len(emoticons)):
        emo_plus_users = 0
        emo_sales = 0
        for user in users:
            payments = 0

            for i, disc in enumerate(discount_per_emoticons):
                if disc >= user[0]:
                    payments += (emoticons[i] * (100 - disc) / 100)

            if payments >= user[1]:
                emo_plus_users += 1

            else:
                emo_sales += payments

        if max_emo_plus_users < emo_plus_users:
            max_emo_plus_users, max_emo_sales = emo_plus_users, emo_sales

        elif max_emo_plus_users == emo_plus_users:
            if max_emo_sales < emo_sales:
                max_emo_plus_users, max_emo_sales = emo_plus_users, emo_sales

    return [max_emo_plus_users, int(max_emo_sales)]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
