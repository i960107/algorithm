def get_spell_separation_group_number(s: str) -> int:
    groups = 0
    prev_spell = ""

    for c in s:
        if c != prev_spell:
            groups += 1
            prev_spell = c
    return groups


def get_spell_separation_group_number_others(N: int, s: str) -> int:
    answer = 0
    for i in range(1, N):
        # 차이가 나는 지점에서 분리된다
        if s[i - 1] != s[i]:
            answer += 1
    # answer 번 분리되면 총 answer + 1개의 그룹 생성
    return answer + 1


N = int(input())
s = input()
print(get_spell_separation_group_number(s))
print(get_spell_separation_group_number_others(N, s))
