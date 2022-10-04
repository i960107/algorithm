def solution(L: int, P: int, V: int):
    return V // P * L + min(V % P, L)


L, P, V = 5, 8, 20
print(solution(L, P, V))
L, P, V = 5, 8, 17
print(solution(L, P, V))
