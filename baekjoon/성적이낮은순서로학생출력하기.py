from typing import List, Tuple


def solution(scores: List[Tuple[str, int]]) -> List[str]:
    return [name for name, score in sorted(scores, key=lambda x: x[1])]


res = solution([("홍길동", 95), ("이순신", 77)])
print(res, res == ["이순신", "홍길동"])
