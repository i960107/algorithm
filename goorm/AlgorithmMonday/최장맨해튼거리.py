from itertools import combinations

numbers = list(map(int, input().split()))
# 최종적으로 6개의 경우만 비교하면 됨.
max_distance = 0

for fi, fj, si, sj in combinations(range(4), 4):
    print(fi, fj, si, sj)
    distance = abs(numbers[fi] - numbers[si]) + abs(numbers[si] - numbers[sj])
    max_distance = max(max_distance, distance)

print(max_distance)
