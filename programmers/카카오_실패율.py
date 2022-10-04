from typing import List
from collections import Counter


def get_stages_order_by_failure_rate_desc(n: int, stages: List[int]) -> List[int]:
    stage_state = Counter(stages)

    acc_players = stage_state[n + 1]

    for stage in range(n, 0, -1):
        acc_players += stage_state[stage]
        stage_state[stage] = (stage_state[stage] / acc_players) if acc_players else 0

    return sorted(range(1, n + 1), key=lambda x: (stage_state[x], -x), reverse=True)


print(get_stages_order_by_failure_rate_desc(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(get_stages_order_by_failure_rate_desc(4, [4, 4, 4, 4, 4]))
