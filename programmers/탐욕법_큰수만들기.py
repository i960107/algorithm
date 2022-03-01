def solution(number: str, k: int) -> str:
    if sorted(number) == number:
        return "".join(number[:-k])

    # 모아진 숫자. 문자열은 immutable하기 때문에 list에 모으는게 나음.
    collected = []

    # k개 만큼 다 뺏을때 그 위치부터 마지막 글자까지 지칭하기 위해 인덱스 필요
    for i, num in enumerate(number):
        # 정수로 굳이 바꾸지 않아도 됨. 문자열 대소관계와 정수 대소관계 같음.
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        # collected가 빈 배열이거나 collected에 있는 모든 수보다 num이 작거나 뺄 수 있는 수가 없을때 while 문 빠져나옴
        # 만약 더 이상 뺄 수 없다면 number의 나머지 부분 다 더해주기. 계속 반복문 실행되는 것보다 최적화된 방법
        if k == 0:
            collected.append(number[i:])
            break
        else:
            collected.append(num)

    # 만약 빼낼 글자가 남아있는 경우 더 빼내주기. (예를 들어 number가 내림차순 정렬되어있을때 반복문 끝날때까지 하나도 빠지지 않음)
    # [:-k] -> 뒤에서부터 k개의 글자를 떼어낸다는 의미.
    # [-0] -> 배열의 가장 앞글자를 말함 따라서 collected[:-0] = None
    collected = collected[:-k] if k > 0 else collected

    return "".join(collected)

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

