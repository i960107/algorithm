from typing import Tuple


def longest_repeating_character_replacement(s: str, k: int) -> int:
    def get_end_of_repeating_character_with_and_without_replacement(left: int) -> Tuple[int, int]:
        char = s[left]
        replaced = 0
        next_left = left
        for right in range(left, len(s)):
            if char == s[right]:
                continue

            if replaced == 0:
                next_left = right

            if replaced < k:
                replaced += 1
                continue

            return next_left, right
        return len(s), len(s)

    left = right = next_left = 0
    max_repeat_count = 0

    while right < len(s):
        left = next_left
        next_left, right = get_end_of_repeating_character_with_and_without_replacement(left)

        repeat_count = right - left
        max_repeat_count = max(max_repeat_count, repeat_count)

    return max_repeat_count


# print(longest_repeating_character_replacement("AAABBC", 2))
# print(longest_repeating_character_replacement("", 2))
# print(longest_repeating_character_replacement("AA", 2))
# print(longest_repeating_character_replacement("AABBCBB", 2))
# print(longest_repeating_character_replacement("AABB", 2))
print(longest_repeating_character_replacement("ABBB", 2))
