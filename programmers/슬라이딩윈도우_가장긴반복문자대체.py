from collections import Counter


def longest_repeating_character_replacement(s: str, k: int) -> int:
    '''투포인터, 슬라이딩 윈도우, counter를 모두 이용'''
    # 오른쪽 포인터에서 왼쪽 포인터 값을 뺀 다음,
    # 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같을 수 있는
    # 수 중 가장 큰 값
    # max(right) - min(left) - max_char_n == k
    # right를 초기화해주는 이유 len(s) == 1인 경우 right - left = 0을 반환해주어야함
    # for문 안으로 진입하면 right 재할당됨. right global변수로 만들어 두어야
    left = right = 0
    counts = Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        max_char_n = counts.most_common(1)[0][1]
        # 왼쪽 포인터는 0에서 움직이지 않는게 좋지만 k를 넘어선다면 오른쪽으로 이동해야 함
        # k 초과시 왼쪽 포인터 이동
        # k 초과시 right 포인터를 왼쪽으로 이동할 필요는 없나.
        # 인덱스를 가리키는는게 아니라 수만 찾으면 됨
        # 한번 최댓값이 된 상태에서는 오른쪽 포인터가 한 칸 이동하면 왼쪽 포인터도 따라서 이동하게 됨.
        # 여기가 잘 이해가 안됨.
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1

    print("left", left, "right", right)
    return right - left


# k번 대체해서 반복되는 문자열 만들 수 있을때
print(longest_repeating_character_replacement("AAABBC", 2))
# k가 0일때. 가장 긴 반복 문자
print(longest_repeating_character_replacement("AAABBC", 0))
# s가 빈 문자열일때
print(longest_repeating_character_replacement("", 2))
# k가 len(s)보다 클때
print(longest_repeating_character_replacement("AAABBC", 10))


def longest_repeating_character_replacement(s: str, k: int) -> int:
    left = right = 0
    # 0일때는 pass. 1일때 부터 반복
    count = Counter()
    for right in range(1, len(s) + 1):
        count[s[right - 1]] += 1
        max_n_count = count.most_common(1)[0][1]
        if right - left - max_n_count > k:
            count[s[left]] -= 1
            left += 1
    return right - left
