import sys

read = sys.stdin.readline

maze = [
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "1", "1", "1", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "1", "2", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "1", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
]

# for _ in range(10):
#     maze.append(list(read().split()))
# print(maze)

dx = (1, 0)
dy = (0, 1)
x, y = 1, 1
maze[y][x] = "9"
ate = False

while x != 9 and y != 9 and not ate:

    moved = False

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx > 9 or ny > 9:
            continue

        elif maze[ny][nx] == "1":
            continue

        else:
            moved = True

            x, y = nx, ny

            if maze[y][x] == "2":
                ate = True

            maze[y][x] = "9"
            break

    if not moved:
        break


for y in range(10):
    print(" ".join(maze[y]))
