def solution(s: str) -> str:
    alphas = []
    digits = []

    for c in s:
        if c.isalpha():
            alphas.append(c)
        else:
            digits.append(c)
    return "".join(sorted(alphas)) + "".join(digits)


print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))
