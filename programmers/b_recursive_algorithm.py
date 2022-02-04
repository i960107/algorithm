def sum_recursive(n):
    return n + sum_recursive(n - 1) if n != 1 else 1


def sum_iterative(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def fibonacci_recursive(x):
    return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2) if x >= 2 else x


def fibonacci_recursive_improved(x, r):
    if x < 2:
        r[x] = x
        return x
    elif r[x] > 0:
        return r[x]
    else:
        r[x] = fibonacci_recursive_improved(x - 1, r) + fibonacci_recursive_improved(x - 2, r)
        return r[x]


def fibonacci_iterative(x):
    fibo = [0, 1]
    i = 2
    while i <= x:
        fibo.append(fibo[i - 1] + fibo[i - 2])
        i += 1
    return fibo[x]


print(f'fibonacci_iterative : {fibonacci_iterative(4)}')
print(f'fibonacci_recursive : {fibonacci_recursive(4)}')
fibo = [0] * (4 + 1)
print(f'fibonacci_recursive_imporved : {fibonacci_recursive_improved(4, fibo)}')


def binary_search_recursive(L, x, l, u):
    if l > u:
        return -1
    else:
        middle = (l + u) // 2
        if L[middle] == x:
            return l + u // 2
        elif L[middle] > x:
            u = middle - 1
            return binary_search_recursive(L, x, l, u)
        elif L[middle] < x:
            l = middle + 1
            return binary_search_recursive(L, x, l, u)


L = [2, 3, 5, 6, 9, 11, 15]
x = 6
l = 0
u = 6
print(f'binary_search : {binary_search_recursive(L, x, l, u)}')
L = [2, 5, 7, 9, 11]
x = 4
l = 0
u = 4
print(f'binary_search : {binary_search_recursive(L, x, l, u)}')
