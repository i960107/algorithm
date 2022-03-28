def solution_num_represent(n: int) -> int:
    cnt = 1
    for i in range(1, n + 1):
        s = [i]
        for j in range(i + 1, n + 1):
            s.append(j)
            if sum(s) == n:
                print(s)
                cnt += 1
                break
            elif sum(s) > n:
                break
    return cnt


print(solution_num_represent(15))
print(solution_num_represent(10000))
