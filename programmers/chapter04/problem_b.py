from sys import stdin

'''Probing'''


class LuckyDraw:
    def __init__(self, N: int):
        self.N = N
        self.used = [False] * N

    def get_ticket_number(self, user_id: int) -> int:
        ticket = user_id % self.N
        while self.used[ticket]:
            ticket = (ticket + 1) % self.N

        self.used[ticket] = True
        return ticket


N, M = map(int, input().split())
read = stdin.readline

ld = LuckyDraw(N)
for _ in range(M):
    user_id = int(read())
    print(ld.get_ticket_number(user_id))
