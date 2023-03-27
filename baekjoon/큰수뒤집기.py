T = input()

# result = []
# for x in T.split("-"):
#     original = 0
#     reverse = 0
#     arr = list(map(int, x.split()))
#     n = len(arr)
#     for i, num in enumerate(arr):
#         original += (num * (10 ** i))
#         reverse += (num * (10 ** (n - i - 1)))
#     result.append((original, reverse))
#
# print(result)
#
# prefix = [0]
# for index, (original, reverse) in enumerate(result):
#     # 홀수번째 그룹: index 0, 2, 4
#     if index % 2 == 0:
#         prefix.append(original)
#     else:


# S = ""
# X = 0
# # brute force시 시간 초과
# for t in T.split("-"):
#     for char in t:
#         S += char
#         X += int(S)
#     S = S[::-1]
#
# print(X)