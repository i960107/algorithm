import collections
import itertools
from functools import reduce


def solution_array(clothes: list) -> int:
    array = {}
    for _, type in clothes:
        if type in array:
            # 각 타입별로 몇개의 이름이 있는지만 알면됨. 이름은 알 필요 없음.
            array[type] += 1
        else:
            array[type] = 1
    cnt = 1
    for i in array.values():
        # 타입의 각 아이템을 착용하는것 + 그 타입을 착용하지 않는 것
        cnt *= (i + 1)
        # 아무것도 안 입는 경우
    return cnt - 1


def solution_reduce(clothes: list) -> int:
    # 각 type이 몇번 등장하는지만 세면 됨
    cnt = collections.Counter([type for name, type in clothes])
    # reduce에 초기값 정해주지 않으면? 앞의 두원소로 처음 연산 수행.
    # initial value 없고 iterable 원소 개수 1면 자기자신을 반환
    return reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1


def solution_combinations(clothes: list) -> int:
    '''itertools.product() 를 사용해서'''
    cnt = collections.Counter([type for _, type in clothes])
    l = [[1] * (c + 1) for c in cnt.values()]
    # 두개 이상의 리스트에서 모든 조합을 계산해야 한다면, product사용
    return sum(1 for _ in itertools.product(*l)) - 1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution_array(clothes))
print(solution_reduce(clothes))
print(solution_combinations(clothes))
