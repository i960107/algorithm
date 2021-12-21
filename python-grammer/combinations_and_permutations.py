import itertools

# permutations순열 순서가 있는것 nPr = n!/(n-r)!
# combinations조합 순서가 없는것 nCr = nPr/r! = n!/r!(n-r)!

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool))))
print(list(map(''.join, itertools.permutations(pool, 2))))


# ??
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


print(permute(pool))
