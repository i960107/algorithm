def solution(lottos, win_nums):
    d = {}

    # O(1): lottos배열 길이 6으로 일정.
    # dic에서 찾는 시간 얼마나 걸리지? 새로운 원소 추가될때마다 stack처럼 연속적으로 쌓는다면 최대 사이즈 6이므로 상수시간에 발생
    for num in lottos:
        d[num] = d.get(num, 0) + 1

    won = 0

    # O(1): win_num 길이 6으로 일정. d에서 찾는 행위를 win_num의 개수만큼 반복
    for num in win_nums:
        won += d.get(num, 0)

    # O(1)
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    return [rank[won + d.get(0, 0)], rank[won]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))


# 정렬을 했을때
# rank라는 dic으로 우선순위를 결정하는것 vs if 문으로 결정하는것
# 최소 순위를 결정하고 거기에 0의 갯수를 더하면 순위 결정되는가?
# lottos, win_nums가 빈 배열인 경우는 없음. lottos가 다 0이거나 0이 하나도 없는 경우를 따져봐야함
# keyError가 발생한 이유
# 다른 사람의 풀이에 비해서 내 풀이가 나은 점. 부족한 점. rank를 dictionary가 아닌 배열을 쓴것은 매모리 및 연산 속도 상 좋음.
def solution_others(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1

    return rank[cnt_0 + ans], rank[ans]
