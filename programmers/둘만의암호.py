def solution(s: str, skip: str, index: int) -> str:
    skip = set(skip)
    cache = dict()
    answer = []
    for char in s:
        # # 문자를 아스키코드로
        # print(ord(char))
        # # 아스키코드를 문자로?
        # print(chr(ord(char)))
        if char in cache:
            decoded = cache.get(char)
        else:
            k = 0
            decoded = ord(char)
            while k < index:
                decoded += 1
                if decoded == ord("z") + 1:
                    decoded = ord("a")
                if chr(decoded) not in skip:
                    k += 1
            decoded = chr(decoded)
            print(char, decoded)
        cache[char] = decoded
        answer.append(decoded)
    return ''.join(answer)


print(solution("aukks", "wbqd", 5))
