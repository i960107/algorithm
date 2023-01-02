n, name = input().split()
answer = 0
for _ in range(int(n)):
    other = input()
    if other.__contains__(target=name):
        answer += 1
print(answer)
