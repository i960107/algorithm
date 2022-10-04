from collections import deque


def solution1(log: str) -> str:
    '''deque을 이용한 풀이'''

    left = deque()
    right = deque()

    for x in log:
        if x.isalpha():
            left.append(x)
        elif x == "<":
            if left:
                right.appendleft(left.pop())
        elif x == ">":
            if right:
                left.append(right.popleft())
        else:
            if left:
                left.pop()

    return ''.join(left) + ''.join(right)


def solution2(log: str) -> str:
    '''stack을 이용한 풀이'''
    left = []
    right = []

    for x in log:
        if x.isalpha():
            left.append(x)
        elif x == "<":
            if left:
                right.append(left.pop())
        elif x == ">":
            if right:
                left.append(right.pop())
        else:
            if left:
                left.pop()

    return ''.join(left) + ''.join(right[::-1])


res = solution1("<<BP<A>>CD-")
print(res, res == "BAPC")

res = solution2("<<BP<A>>CD-")
print(res, res == "BAPC")
