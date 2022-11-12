from collections import defaultdict


# 아직 사용되지 않은 색상의 수, 한번만 사용된 색상의 수, 이웃한 색상의 유무
def get_all_possible_ways(N: int) -> int:
    dp = defaultdict(int)
    dp[str([0, 0, 0])] = 1

    def _get_all_possible_ways(unused: int, one: int, neighbor: int) -> int:
        key = str([unused, one, neighbor])

        if key in dp:
            return dp[key]
        cnt = 0
        # 아직 한번도 사용되지 않은 색상을 사용해서 해당 영역을 칠하는 경우의 수
        if unused > 0:
            cnt += _get_all_possible_ways(unused - 1, one, 1)
        if one > 0:
            cnt += _get_all_possible_ways()

    pass


N = int(input())
print(get_all_possible_ways(N))
