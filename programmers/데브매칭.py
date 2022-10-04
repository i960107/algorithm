# from sys import stdin
#
# read = stdin.readline
#
# n, name = read().split()
#
# cnt = 0
# test = []
# for _ in range(int(n)):
#     # if name in read():
#     cur = read()
#     if cur.find(name):
#         test.append(cur)
#         cnt += 1
# print(cnt)
# print(test)

# nums = list(map(int, input().split()))
#
# max_md = 0
#
# # dk = ((-1, -1, 1, 1), (-1, 1, -1, 1), (-1, 1, 1, -1))
# indices = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
#
# for point in indices:
#     md = abs(nums[point[1][0]] - nums[point[0][0]])
#     md += abs(nums[point[1][1]] - nums[point[0][1]])
#     max_md = max(md, max_md)
#
# print(max_md)

n = int(input())
nums = list(map(int, input().split()))


def is_prime(num: int):
    if num <= 1:
        return False

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False

    return True


summation = 0
test =[]
for i in range(n):
    if is_prime(i + 1):
        summation += nums[i]
        test.append(nums[i])
print(test)
print(summation)
