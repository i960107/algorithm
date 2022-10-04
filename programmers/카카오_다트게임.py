def solution(dart_result: str) -> int:
    round = []

    i = 0
    while len(round) < 3:

        score = 0

        if dart_result[i + 1] != "0":
            score = int(dart_result[i])
            i += 1
        else:
            score = int(dart_result[i:i + 2])
            i += 2

        bonus = [None, "S", "D", "T"]
        score = score ** bonus.index(dart_result[i])
        i += 1

        round.append(score)

        if i < len(dart_result) and dart_result[i] == "*":
            round[-1] *= 2
            if len(round) > 1:
                round[-2] *= 2
            i += 1

        elif i < len(dart_result) and dart_result[i] == "#":
            round[-1] *= -1
            i += 1

    return sum(round)


# print(solution("1S2D*3T"))
# print(solution("1D2S#10S"))
# print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
# print(solution("1D#2S*3S"))
