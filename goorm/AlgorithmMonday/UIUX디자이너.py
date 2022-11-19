from collections import Counter

n, m = map(int, input().split())
event_counter = Counter()
for _ in range(m):
    event_counter.update(list(map(int, input().split()))[1:])

max_execution = event_counter.most_common(1)[0][1]
answer = []
for event, count in event_counter.most_common():
    if count == max_execution:
        answer.append(event)
    else:
        break
answer.sort(reverse=True)
print(*answer)
