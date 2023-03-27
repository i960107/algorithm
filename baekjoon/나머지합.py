# 부분 배열의 개수 -> O(N^2)
# brute force시 시간초과날것!
# 1차원이든 2차원이든 연속된 범위의 합 -> 누적합
N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]
remainders = [0] * M
for num in arr:
    prefix.append((num + prefix[-1]))
    remainders[prefix[-1] % M] += 1


# 시간 초과..
# count =0
# for j in range(1, N +1):
#     for i in range(j + 1, N+1):
#         range_sum = prefix[i] - prefix[j-1]
#         if range_sum % M == 0:
#             count += 1

# 누적합이 3의 배수인 것들 어떻게 조합해서 더하든 3의배수가 됨
# 누적합의  % m 결과가 같은 것들 중 2개를 조합해서 빼면 나머지가 0이됨
# (3 * m + k) - (3 * n +k) = 3 ( m- n)

# 0 ~ N까지의 누적합이 M의 배수인 경우
count = remainders[0]
# 누적합 % M의 결과가 같은 것들 중 2개씩 조합하는 경우
for x in remainders:
    # x == 0일때 결과도 0이 됨!
    count += ((x * (x - 1)) // 2)
print(count)



# solution 2
# 나누기 M의 나머지가 i인 누적합의 개수
arr_m = [0] * M

# 누적합
s = 0
num = 0
for i in range(N):
    s += arr[i]
    res = s % M
    if res == 0:
        num += 1
    arr_m[res] += 1

for i in range(M):
    if arr_m[i] == 0:
        continue
    num += (arr_m[i] * (arr_m[i] - 1)) // 2

# -1 // 3 = -1 , -1 % 3 == 2
print(num)
