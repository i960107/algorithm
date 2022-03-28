def solution_N_notation_game(n: int, t: int, m: int, p: int) -> str:
    arr = ""

    def convert_notation(num: int, k: int) -> str:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if num == 0:
            return '0'
        reverse = ''
        while num != 0:
            num, remainder = num // k, num % k
            reverse += nums[remainder % k]
        return reverse[::-1]

    i = 0
    while len(arr) <= p + m * (t - 1):
        arr += convert_notation(i, n)
        i += 1

    return ''.join([arr[i-1] for i in range(p, p + m * (t - 1) + 1, m)])


print(solution_N_notation_game(2, 4, 2, 1))
print(solution_N_notation_game(16, 16, 2, 1))
print(solution_N_notation_game(16, 16, 2, 2))
