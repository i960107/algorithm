from functools import reduce

n = int(input())
bridges = list(map(int, input().split()))
print(reduce(lambda x, y: x * y, bridges, 1))
