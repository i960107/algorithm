import itertools
import collections


def solution_sequence_join(mylist):
    '''sequence멤버를 하나로 이어붙이기'''
    return ''.join(mylist)


print(solution_sequence_join(['hello', 'my', 'name', 'is', 'soohyun']))


def solution_sequence_asterisk(n):
    '''문자열 반복'''
    print(*[123, 456] * n)  # 123 456 123 456
    print([123, 456] * n)  # [123,456,123,456]
    for i in range(n):
        print('*' * (i + 1))


n = int(input().strip())
solution_sequence_asterisk(n)

