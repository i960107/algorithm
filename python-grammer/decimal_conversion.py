# n진법으로 표기된 string을 10진법 숫자로 변환하기
def solution(num, base):
    # num이 string 타입임.
    answer = 0
    # num[::-1] 리스트 뒤집기
    for idx, number in enumerate(num[::-1]):
        # **은 거듭제곰
        answer += int(number) * base ** idx
    return answer


def solution_python(num, base):
    #int()에 매개변수 두개일 경우 첫번째 인자는 string타입이여야함.
    return int(num, base)
