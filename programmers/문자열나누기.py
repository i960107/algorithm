def solution(s: str) -> int:
    temp = None
    same_characters = 0
    different_characters = 0
    strs = 0
    for chr in s:
        if not temp:
            temp = chr
            same_characters += 1
        elif chr != temp:
            different_characters += 1
        elif chr == temp:
            same_characters += 1
        if different_characters == same_characters:
            strs += 1
            temp, same_characters, different_characters = None, 0, 0

    if temp:
        strs += 1

    return strs


print(solution("banana"))
