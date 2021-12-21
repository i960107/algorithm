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


def solution_cartesian_product(*mylist):
    '''iterable 곱집합 구하기'''
    # 어떻게 unpacking한 상태로 전달하기, list원소 개수가 다를 경우?
    # list이름이 list이면 안됨..
    cartesian = list(itertools.product(*mylist))
    print(f'[{len(cartesian)}]cartesian')


mylist = ['ABCD', 'xy', '1234']
solution_cartesian_product(*mylist)

'''가장 많이 등장하는 알파벳 찾기 - counter(어떤 원소가 시퀀스 타입에 몇 번이나 등장하는지'''


# def solution_most_common_alphabet(my_str):
#     c = collections.Counter(my_str)
#     # sort() 함수는 반환 값 없기 때문에 바로 출력할 수 없음.
#     most_common = c.most_common(1)
#     most_common.sort()
#     # 알파벳만 리스트로 모으기
#     print(f'most_common : {most_common}')
#     print(f'가장 많이 등장하는 알파벳 사전 순 : {"".join([counters[0] for counters in most_common])}')
#     # print(f'가장 많이 등장하는 알파벳 사전 순 : {c}')
def solution_most_common_alphabet(my_str):
    dic = collections.Counter(my_str)
    maximum = max(dic.values())
    result = filter(lambda x: x[1] == maximum, dic.items())
    answer = [key for key, value in result]
    answer.sort()
    print(''.join(answer))


# counter - 해시 가능한 객체를 새기 위한 dict 서브 클래스
# list.count의 time complexity는 O(N) dictionary의 원소를 접근하는데에는 (1)
my_str = "dfdefdgf"
solution_most_common_alphabet(my_str)

# counter dict 타입으로 생성됨
my_str = 'hellomynameiskimsoohuynk'
answer = collections.Counter(my_str)
print(f'h : {answer["h"]}')
print(f'counter : {answer}')

# n개의 가장 흔한 요소와 그 개수를 튜플로, 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환
# 개수가 같은 요소를 처음 발견된 순서를 유지
print(f'most_common : {answer.most_common(1)}')

# a new counter from keyword args
example = collections.Counter(cats=4, dogs=10, rabbits=11, lions=12)
print(f'how many cats are here? : {example["cats"]}')
