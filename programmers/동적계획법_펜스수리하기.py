from typing import Final, List
from math import sqrt


class FenceReparing:
    EMPTY: Final = -1

    def __init__(self, fence: str):
        self.n = len(fence)
        self.fence = fence
        self.memo = [self.EMPTY] * self.n

    def is_broken(self, index: int) -> bool:
        return self.fence[index] == "X"

    # 첫번째 펜스부터 last_index + 1번째 펜스까지 고장난 펜스를 고치는 최소 비용을 반환
    def get_minimum_cost(self, last_index: int) -> float:

        if last_index < 0:
            return 0

        # memo[0] 값은 업데이트 되지 않음
        elif last_index == 0:
            return 1

        elif self.memo[last_index] != self.EMPTY:
            return self.memo[last_index]

        # last_index의 펜스가 고장나지 않았다면 이전 고장난 펜스까지 고치는 최소 비용을 반환
        if not self.is_broken(last_index):
            return self.get_minimum_cost(last_index - 1)

        # last_index의 펜스가 고장났다면
        else:

            # 첫번째 펜스부터 last_index의 펜스까지 한번에 고치는 비용
            min_cost = sqrt(last_index + 1)
            for prev_index in range(last_index + 1):

                # 정상 펜스인 경우 현재 블럭까지
                if not self.is_broken(prev_index):
                    continue

                # prev_index 이전까지의 최소 수리 비용 + prev_index ~ last_index펜스를 한번에 수리하는 비용
                # 만약 previous_index == last_index 라면 last index 펜스만 따로 수리하는 경우가 됨. 즉 sqrt(last_index - prev_index + 1) = 1
                cur_cost = self.get_minimum_cost(prev_index - 1) \
                           + sqrt(last_index - prev_index + 1)

                min_cost = min(min_cost, cur_cost)

            return min_cost


fence = input()
fr = FenceReparing(fence)
res = fr.get_minimum_cost(fr.n - 1)
print('%.3f' % res)
