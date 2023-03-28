from typing import List


def solution(babbling: List[str]) -> int:
    # string을 넣으면 character별로 해시 생김.
    # 같은 발음을 연속해서 하지 못함.
    possible = set(["aya", "ye", "woo", "ma"])

    # babbling의 개수 * 각 babbling의 길이
    count = 0
    for word in babbling:
        now = ''
        prev = ''
        for chr in word:
            now += chr
            if len(now) <= 1:
                continue
            if now in possible and now != prev:
                prev = now
                now = ''
        # 마지막에 stack에 남아있는 값 체크해주는 것 잊지말기!
        if now in possible and now != prev:
            now = ''
        if not now:
            count += 1

    return count


# 짧기 때문에 속도차이 크게 나지 않음
# babbling의 개수 * 각 babbling의 길이 * word의 개수
def solution2(babbling: List[str]) -> int:
    count = 0
    for babble in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            if word * 2 not in babble:
                babble = babble.replace(word, " ")
        if not babble.split():
            count += 1
    return count


print(solution2(["aya", "yee", "u", "maa"]))
print(solution2(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
