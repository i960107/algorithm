def solution(dartResult: str) -> int:
    scores = []
    options = [None] * 3
    i = 0
    while i < len(dartResult):
        # 숫자로 된 string 자를때 자리수 확인 필수!!
        if dartResult[i + 1] in ('S', 'D', 'T'):
            score, bonus = int(dartResult[i]), dartResult[i + 1]
            i += 2
        else:
            score, bonus = int(dartResult[i:i + 2]), dartResult[i + 2]
            i += 3

        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        else:
            bonus = 3

        option = None
        if i < len(dartResult) and dartResult[i] in ('*', '#'):
            option = dartResult[i]
            i += 1

        scores.append(pow(score, bonus))
        options[len(scores) - 1] = option

    for i in range(3):
        if options[i] == '*':
            scores[i] *= 2
            scores[i - 1] *= 2 if i else 1
        elif options[i] == '#':
            scores[i] *= -1

    print(f'input {dartResult} scores {scores} options {options}')
    return sum(scores)


def solution_others(dartResult: str) -> int:
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'#': -1, '*': 2}
    scores = []
    dartResult = dartResult.replace('10', 'p')  # perfect

    i = 0
    while i < len(dartResult):
        # 점수
        score = int(dartResult[i]) if dartResult[i] != 'p' else 10

        # 보너스
        score = pow(score, bonus.get(dartResult[i + 1]))
        i += 2
        scores.append(score)

        # 옵션
        if i < len(dartResult) and dartResult[i] in option:
            op = option.get(dartResult[i])
            scores[-1] *= op
            if len(scores) > 1 and dartResult[i] == '*':
                scores[-2] *= op
            i += 1

    return sum(scores)


print(solution_others("1S2D*3T"))
print(solution_others("1D2S#10S"))
print(solution_others("1D2S0T"))
print(solution_others("1S*2T*3S"))
print(solution_others("1D#2S*3S"))
print(solution_others("1T2D3D#"))
print(solution_others("1D2S3T*"))

