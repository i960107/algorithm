import sys
from collections import Counter
from typing import List
from itertools import takewhile


def solution():
    input = sys.stdin.readline  # type(input) : builtin function or method

    books = Counter()
    for _ in range(int(input())):
        # 개별 문자가 count됨
        # books.update(input())
        books.update({input().rstrip(): 1})

    # 정렬된 순서로 모든 쌍 출력
    # print(books.most_common())
    # 가장 많이 팔린 책이 여러개일 경우 사전 으로 가장 앞서는 제목. most common시 사전순 정렬된 결과임?
    # dictionary는 순서 없는 자료형으로 key순으로 정렬 불가능
    max_count = books.most_common(1)[0][1]
    # 가장 많이 팔린 책의 key들을 모아 정렬시키고 첫번째 값을 찾기
    print(sorted(title for title, count in books.items() if count == max_count)[0])


def solution2(books: List[str]) -> str:
    '''counter 와 takewhile 사용'''
    counter = list(Counter(books).items())
    counter.sort(key=lambda x: (-x[1], x[0]))
    return counter[0][0]


res = solution2(["uop", "uop", "uop", "top", "top", "top", "top", "kimtop"])

print(res, res == "top")
