import math

A, B, V = map(int, input().split())
print(math.ceil((V - A) / (A - B) + 1))
print((V - B - 1) / (A - B) + 1)
