from collections import Counter, defaultdict


def solution(J: str, S: str) -> int:
    '''counter모듈을 활용한 풀이'''
    counter = Counter(S)
    return sum(counter[jewel] for jewel in J)


def solution2(J: str, S: str) -> int:
    '''해시 테이블을 활용한 풀이'''
    # O(max(N, M)) 복잡도를 가짐
    freqs = defaultdict(int)

    for char in S:
        freqs[char] += 1

    return sum(freqs[jewel] for jewel in J)


def solution3(J: str, S: str) -> int:
    '''파이썬다운 방식'''
    # O(NM) 복잡도를 가짐. 왜 속도 비슷할까? 최대 연산 횟수 50번 vs 2500. 컴퓨터 입장에서는 차이 없음
    return sum((s in J) for s in S)


print(solution("aA", "aAAbbbb"))
# 경우를 나누자면: 1) jewel이 있는 경우, 2)jewel이 없는 경우 3) J또는 S가 빈 배열이 경우
print(solution2("aA", "aAAbbbb"))
print(solution2("B", "aAAbbbb"))
print(solution2("", "aAAbbbb"))
print(solution2("aA", ""))
