def valid_anagram(s: str, t: str) -> bool:
    # 해시 테이블 사용? 해시 테이블에 삽입. O(N)이 실제로 여러번 수행됨. 개수 비교 O(N) 뭐가 더 빠를까
    # 정렬 사용? O(NlogN).
    # 입력값이 1,000,000처럼 크다고 해도  O(N) 연산을 여러번 수행하는게 여전히 나음.
    # 그럼 해시 테이블에 삽입하는게 더 낫지 않나? 맞음.
    return sorted(s) == sorted(t)


print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
