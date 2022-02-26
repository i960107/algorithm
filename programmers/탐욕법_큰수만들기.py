def solution(num: str, k: int) -> str:
    answer = ""

    start = 0  # 지울 문자를 검색할 대상 문자의 시작 인덱스
    end = len(num) - k  # 지울 문자를 검색할 대상 문자의 마지막 인덱스 + 1
    cnt = len(num) - k  # 검색할 대상 문자의 수
    while k > 0:
        print(f'start {start}  end {end} cnt {cnt} answer {answer}')
        max_num = num[start]
        for x in num[start:end]:
            if x > max_num:
                max_num = x
        answer += max_num
        k -= (cnt - 1)
        start = end
        end = len(num) - k
        cnt = end - start

    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("775841", 4))
