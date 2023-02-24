from typing import List
from sys import stdin

# 이건 다 잡을 수 있는지만 파악할 수 있는 풀이..
read = stdin.readline

M, N, L = map(int, read().split())

haunters = list(map(int, read().split()))
haunters.sort()

animals = []
for _ in range(N):
    animals.append(list(map(int, read().split())))

count = 0
for x, y in animals:
    start, end = x - L + y, x + L - y
    left, right = 0, M - 1
    while left <= right:
        mid = left + (right - left) // 2
        if start <= haunters[mid] <= end:
            count += 1
            break
        elif haunters[mid] < start:
            left = mid + 1
        elif haunters[mid] > end:
            right = mid - 1
print(count)
#
# min_range = 1000000000
# animals_adjusted = [x + y for x, y in animals]
# animals_adjusted.sort()
# # 동물을 다 잡기 위한 사정거리의 최소값
# left, right = 0, 1000000000
# # 최대 30번 수행
# while left <= right:
#     mid = left + (right - left) // 2
#     caught = set()
#     # 최대 100,000번 수행
#     last_haunted_animal_index = -1
#     for haunter in haunters:
#         while last_haunted_animal_index < N - 1:
#             if abs(animals_adjusted[last_haunted_animal_index + 1] - haunter) <= mid:
#                 last_haunted_animal_index += 1
#                 caught.add(last_haunted_animal_index)
#             else:
#                 break
#         if len(caught) == N:
#             break
#     if len(caught) == N:
#         min_range = mid
#         right = mid - 1
#     else:
#         left = mid + 1
#
# # if min_range <= L:
# #     print("Can Catch All Animal")
# # else:
# #     print("Can't Catch All Animal")
#
# # 헌터의 입장에서 동물 찾기 vs 동물 입장에서 헌터 찾기
# animals_caught = set()
# for haunter in haunters:
#     distances = [(abs(haunter - x) + y, index) for index, (x, y) in enumerate(animals)]
#     distances.sort()
#     left, right = 0, N - 1
#     # 주의! 중복된 값이 있을경우 가장 오른쪽 선택할 수 있도록 -> 모든 거리가 3.
#     # 못잡는 동물의 익덴스 중 최소
#     result = 0
#     while left <= right:
#         mid = left + (right - left) // 2
#         if distances[mid][0] <= L:
#             result = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     if result != 0 or distances[result][0] <= L:
#         animals_caught.update(index for distance, index in distances[:result + 1])
# print(len(animals_caught))
