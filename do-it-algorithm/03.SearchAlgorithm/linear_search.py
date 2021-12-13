import copy
from typing import Any, Sequence


# Sequence : 열거형 타입 임의의 자료형. list나 tuple, 문자열이 될 수 있음
# () 혹은 감싸는 기호 없이 열거하면 tuple 타입이 됨.
# 예시
# days = "monday", "tuesday", 'wednesday', 'thursday', 'friday'
# print(type(days)) // 결과 <class 'tuple'>


# 선형 검색 : 원소의 값이 정렬되지 않은 데이터 집합에서 검색시 사용할 수 있는 유일한 방법.
# a가 Sequence타입이기 때문에? 정수 배열, 실수 배열, 문자열 배열 모두 검색 가능
def seq_search_while(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)'''
    i = 0

    while True:
        if i == len(a):
            raise ValueError
        if key == a[i]:
            return i
        i += 1


def seq_search_while_sentinel(a: Sequence, key: Any) -> int:
    '''배열의 끝인지를 n번만큼 판단하지 않고 마지막에 한번 판단하기 위해 보초 사용'''

    # shallowcopy는 같은 주소를 바라보게 함. 원래 배열의 값이 바뀌면 복사한 배열의 값도 바뀜
    # deepcopy는 배열 안 객체까지 새로 생성하기 때문에 원래 배열의 수정이 영향을 미치지 않음.1
    b = copy.deepcopy(a)
    b.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(a) else i


def seq_search_for(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 값이 같은 원소를 선형 검색(for문)'''

    for i in range(len(a)):
        # 왜 실행횟수가 n/2인가 ? n아닌가? p.126
        if a[i] == key:
            return i

    return -1


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요. :'))
    x = [None] * num

    for i in range(num):
        x[i] = (input(f'x[{i}] : '))

    key = (input('검색할 값을 입력하세요. :'))

    try:
        idx = seq_search_while(x, key)
    except ValueError:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
