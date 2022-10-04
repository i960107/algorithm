from typing import List


def solution(input: str) -> List[int]:
    def compute(left: List[int], right: List[int], op: str):
        results = []
        for l in left:
            for r in right:
                # eval함수 활용
                results.append(eval(str(l) + op + str(r)))
        return results

    # 더 이상 쪼갤 수 없다면
    # 연산자가 포함되지 않을때까지 쪼갬
    if input.isdigit():
        return [int(input)]

    results = []
    # 어떻게 나누지?
    # mid로 나눌 수는 없어 숫자가 여러자리 일 수도 있잖아
    # solution 함수의 리턴값이 [] 인데?
    # 선형탐색하면서 연산자가 등장할때 좌/우 분할을 하고 각각 계산 결과를 리턴
    # 연산자가 3개일때 어떻게 5가지 경우 연산자가 2개일때 2가지 경우
    # 연산자가 한개 포함되어있을때 결과  하나
    # 연산자가 두개일때 두가지 경우로 나눌 수 있음
    for index, value in enumerate(input):
        if value in '+-*':
            left = solution(input[:index])
            right = solution(input[index + 1:])

            results.extend(compute(left, right, value))

    return results


print(solution("2-1-1")
print(solution("2*3-4*5"))
