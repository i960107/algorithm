def solution(number: str, k: int) -> str:
    answer = ""

    # 모아진 숫자. 문자열은 immutable하기 때문에 list에 모으는게 나음.
    collected = []

    #k개 만큼 다 뺏을때 그 위치부터 마지막 글자까지 지칭하기 위해 인덱스 필요
    for i,num in enumerate(number):
        while


    retrun answer

    # while k > 0 and curr <= len(num) - 1:
    #     while True:
    #         print(f'단계{n}answer{answer} curr{num[curr]} k {k}')
    #         n += 1
    #         if answer and answer[-1] < num[curr]:
    #             k -= 1
    #             answer = answer[:-1]
    #         elif answer and answer[-1] >= num[curr]:
    #             answer += num[curr]
    #             break
    #         else:
    #             answer += num[curr]
    #             break
    #     curr += 1
    #
    # return answer


def solution_other(num: str, k: int) -> str:
    answer = ""
    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("417752841", 4))
