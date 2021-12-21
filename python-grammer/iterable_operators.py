import itertools
from functools import reduce
import operator
import copy
from functools import reduce


def solution_sort_list_comprehension(l: list) -> list:
    '''원본을 유지한채, 정렬된 리스트 구하기 방법 (1)-list comprehension and sort '''
    # 방법1 - list comprehension & sort O(N)
    # python은 정렬 알고리즘으로 팀소트 사용

    list2 = [i for i in l]

    # sort(revers= True)보다 reverse()가 O(N)으로 복잡도 더 낮음 ? 내부적으로 같을수도
    # return list2.reverse() -> reverse() 원본을 변화시키는 것으로 반환값 없음.
    list2.reverse()

    return list2


def solution_sort_list_deepcopy(l: list) -> list:
    '''원본을 유지한채, 정렬된 리스트 구하기 방법 (2)-deepcopy and sort'''
    # 방법2 - deepcopy & sort O(N)

    list2 = copy.deepcopy(l)
    list2.reverse()

    return list2


def solution_sort_list_sorted_method(l: list) -> list:
    '''원본을 유지한채, 정렬된 리스트 구하기 방법 (3)-sorted()'''
    # deepcopy 함수 없이 새로운 정렬된 리스트 만들기 O(NlogN)

    # 정렬이 필요할 경우 방법 1,2,3 모두 O(NlogN) 복잡도를 가짐.
    # 내부적으로는 deepcopy와 sort 실행할 것.
    return sorted(l, reverse=True)


l = [3, 2, 1]
print(l, solution_sort_list_comprehension(l))
print(l, solution_sort_list_deepcopy(l))
print(l, solution_sort_list_sorted_method(l))


# -------------------------------------------------------------------------

def solution_for(mylist):
    '''2차원 list 뒤집기 - for문 사용'''
    # answer = [[None] * len(mylist)] * len(mylist)
    # 안됨. 2차원 배열안 요소 배열은 모두 같은 객체로 인식되어서
    # 값 변경시 전체 배열에 영향이 감.
    answer = [[None] * len(mylist) for _ in range(len(mylist))]
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            # i는 느리게 변하는 값->행 번호로 할 것인가 열번호로 할 것인가.
            # 행번호로 하면 한 행씩 읽어와서 -> 각행의 열에 추가
            # 열번호로 하면 각 행의 열 읽어와서 -> 한 행에 추가
            # 알고리즘 복잡도 크게 차이 없음.
            answer[j][i] = mylist[i][j]

    return answer


def solution_zip(mylist):
    '''2차원 list 뒤집기 - zip 사용'''
    # * : for unpacking the data in container ->3개의 별개의 리스트로 쪼개기
    # 행과 열이 바뀐다는건 각 요소 리스트에서 i번째 원소를 들고와서 i번째 리스트를 만들게 되는 결과
    return list(map(list, zip(*mylist)))


print(solution_for([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution_zip([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

'''zip함수에 대해 '''
# 정의- returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables
# 예1 - 여러개의 iterable 동시에 순회
list1 = [1, 2, 3]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
    # 4번째 반복문에서 원소는 무엇? 모든 리스트에 원소 존재할때까지만 tuple 만들기때문에 zip()에서 반환되는 튜플 사이즈 3
    print(number1)
    print(number2)
    print(number3)
    # 모든 리스트의 i번째 원소의 합 출력
    print(f'합 :  {number1 + number2 + number3}')

# 예2 - key리스트와 value리스트로 딕셔너리 생성하기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer)

'''*(asterisk)에 대해'''


def product(*numbers):
    # reduce() : sequence에 대해 집계함수 적용.
    # x: accumulator y:current value
    # lambda식에서 multiline (,) 하면 이상한 결과 나옴 => 외부 함수로 빼주기
    p = reduce(lambda x, y: x * y, numbers)
    return p


def product2(numbers):
    p = reduce(lambda x, y: x * y, numbers)
    return p


primes = [2, 3, 5, 7, 11, 13]
# argument와 parameter 둘다 asterisk 필요? 의미가 다름.
# *primes : unpacking , *numbers : 가변인자
# print(*primes)  # 6개의 데이터 - unpacking된 데이터 type은? 요소 타입 데이터 요소 개수만큼
# print(primes)  # 1개의 리스트 6개의 원소

# *-가변 인자.  argument로 *를 받기 때문에 데이터 개수 상관없음.
print(f'product : {product(primes)}')
print(f'product : {product(*primes)}')

# argument로 데이터 하나를 받기 때문에 unpacking된 상태로 전달하면 TypeError발생
print(f'product2  {product2(primes)}')


# print(f'product2 * {product2(*primes)}')


# -------------------------------------------------------------------------

# index를 사용하지 않고 각 원소에 접근 가능
def solution_abs_difference(mylist):
    '''i번째 원소가 i+1번째 원소'''
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        # 원소 하나라도 None일때 어떤 값 반환?
        # 그런 경우 존재하지 않음 모든 원소가 존재할때까지만 zip object만듬
        num = abs(number1 - number2)
        answer.append(num)
    return answer


print(solution_abs_difference([84, 48, 13, 4, 71, 11]))
