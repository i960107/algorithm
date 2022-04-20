import bisect
from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    l, u = 0, len(letters) - 1
    while l <= u:
        mid = l + (u - l) // 2
        if letters[mid] < target:
            l = mid + 1
        elif letters[mid] > target:
            u = mid - 1
        else:
            # mid +1 이 index out of range일 경우는 없음?
            return letters[(mid + 1) % len(letters)]
    # 왜 u가 기준이 될까?
    return letters[(u + 1) % len(letters)]


def nextGreatestLetter2(letters: List[str], target: str) -> str:
    index = bisect.bisect_right(letters, target)
    return letters[index % len(letters)]


print(nextGreatestLetter(letters=["a", "b"], target="r"))
print(nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(nextGreatestLetter(letters=["c", "f", "j"], target="d"))
# 중복된 원소 있을 수 있음!
print(nextGreatestLetter(letters=["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], target="e"))

print(nextGreatestLetter2(letters=["a", "b"], target="r"))
print(nextGreatestLetter2(letters=["c", "f", "j"], target="a"))
print(nextGreatestLetter2(letters=["c", "f", "j"], target="c"))
print(nextGreatestLetter2(letters=["c", "f", "j"], target="d"))
# 중복된 원소 있을 수 있음!
print(nextGreatestLetter2(letters=["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], target="e"))
