from typing import List


def solution(babbling: List[str]) -> int:
    # 2,3,2,3,
    possible = ("aya", "ye", "woo", "ma")
    count = 0
    for babble in babbling:
        left, right = 0, 2
        now_count = 0
        while right <= len(babble):
            print(left, right, babble[left:right])

            temp = babble[left:right]
            if temp in possible:
                now_count += 1
            else:
                now_count = 0
                break

            if right - left == 2:
                right += 1
            elif right - left == 3:
                left += 1
        count += now_count
    return count


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
