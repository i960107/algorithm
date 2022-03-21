def solution(new_id: str) -> str:
    # 문자열 자체를 조작하는게 아니라 조작된 결과를 반환함!
    new_id = new_id.lower()
    # 알파벳 소문자, 숫자,빼기, 밑줄,마침표를 제외!!한 모든 문자를 제거. for문 밖에 없나?
    filtered_id = ""
    for char in new_id:
        # if char in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
        # 문자을 아스키 코드 값으로 변경 intX ordO
        if (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 97 and ord(char) <= 122) or (
                ord(char) in (45, 46, 95)):
            filtered_id += char
    new_id = filtered_id
    # ..이 여러개인 경우 한번만 치환한 결과가 ..일수도 있음!
    # new_id 길이 1000이하로 선형탐색해도 됨.
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    new_id = new_id.strip(".")
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        # python에서 trim -> strip. split은 쪼개기
        new_id = new_id.rstrip(".")
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id


# def solution_others(new_id:str)->str:
#     new_id = new_id.lower()
#     answer = ''
#     for char in new_id:
#         if char.isalnum() or char in '-_.':
#             answer += char
#
#     return answer

print(solution("...!@BaT#*..y.abcde..fghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
