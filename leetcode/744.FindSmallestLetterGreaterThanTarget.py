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
    # 중복되는 값이 여러개 있다면 맨 오른쪽 인덱스
    # bisect_right는 원소가 있다면 그 다음잉니깐 삽입하는 위치니깐 letters[index] == target인 경우 없겠군
    # bisect_left는 원소가 있다면 그 첫 위치니깐 letters[index] == target인 경우 있음
    index = bisect.bisect_right(letters, target)
    # 꼭 필요할때만 연산하고 아니면 바로 참조해서 속도 빠르게 할 수 있음
    return letters[index % len(letters)]


# 찾는 원소가 중복되어 들어있을때
print(nextGreatestLetter2(["a", "b", "b", "f"], "b"))
# 찾는 원소가 마지막 원소일때
print(nextGreatestLetter2(["a", "b", "b", "f"], "f"))
# 찾는 원소가 없을때
print(nextGreatestLetter2(["a", "b", "b", "f"], "i"))
# 찾는 원소가 없고 답이 맨 처음 원소일때
print(nextGreatestLetter2(["x", "y"], "i"))

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
