from collections import Counter
import operator
from functools import reduce
import itertools

'''iterable 곱집합 구하기'''


def solution_cartesian_product(*my_list):
    # list이름이 list이면 안됨..
    print(f'mylist {my_list}')
    print(*my_list)
    print(*my_list[0])

    # cartesian product - 데카르트 곱. DB의 join과 비슷
    # 두개 이상의 리스트의 모든 조합을 구할때 사용
    # 시간 복잡도 매우 높음
    cartesian = list(itertools.product(*my_list))
    print(f'[{len(cartesian)}]cartesian')


my_list = ['ABCD', 'xy', '1234']
solution_cartesian_product(*my_list)
# ------------------------------------------------------------------
'''2차원을 1차원 리스트로 만들기 '''


def solution_for(my_list: list) -> list:
    '''방법1 - for 문 사용'''
    answer = []
    for element in my_list:
        answer += (element)
    return answer


def solution_sum(my_list: list) -> list:
    '''방법2 - sum함수'''
    # sum(iterable, start_value)
    # 빈 배열에서 시작해서 숫자 원소 하나씩 가져와서 추가하기
    # sum 함수 : += 로 누적해서 더해감. 리스트 +=는 리스트 합치는 연산임
    return sum(my_list, [])


def solution_chain_from_iterable(my_list: list) -> list:
    '''방법3 - itertools.chain'''
    return list(itertools.chain.from_iterable(my_list))


def solution_chain_and_unpacking(my_list: list) -> list:
    '''방법4 - itertools.chain과 unpacking'''
    return list(itertools.chain(*my_list))


def solution_list_comprehension(my_list: list) -> list:
    '''방법5 - list comprehension 이용'''
    # 배열 원소 하나씩 가져온 후 각 배열 원소 안 데이터 하나씩 가져와서 리스트 생성
    # array = [array for array in my_list]
    # element = [element for element in array]
    return [element for array in my_list for element in array]


def solution_reduce(my_list: list) -> list:
    '''방법6 - reduce 함수 이용 1'''
    return list(reduce(lambda x, y: x + y, my_list))


def solution_reduce_and_operator(my_list: list) -> list:
    '''방법7 - reduce 함수 이용 2'''
    return list(reduce(operator.add, my_list))


# def solution_reduce(my_list: list) -> list:
#     '''방법8 - numpy 라이브러리의 flatten 이용 (각 원소의 길이가 동일한 경우에만 사용 가능)'''
#     return numpy.array(my_list).flatten().tolist()


my_list = [[1, 2], [3, 4], [5, 6]]
print(solution_for(my_list))
print(solution_sum(my_list))
print(solution_chain_and_unpacking(my_list))
print(solution_chain_from_iterable(my_list))
print(solution_list_comprehension(my_list))
print(solution_reduce(my_list))
print(solution_reduce_and_operator(my_list))

# ------------------------------------------------------------------
# permutation 순열 순서가 있는것 nPr = n!/(n-r)!
# combination 조합 순서가 없는것 nCr = nPr/r! = n!/r!(n-r)!
# 주의 : combinations, permutations, product 모두 generator 이기 때문에
# list()로 캐스팅하여 저장하지 않으면 한번의 루핑이후 사라짐

pool = ['A', 'B', 'C']

# 튜플 iterator반환
print(list(itertools.permutations(pool)))
print(list(map(''.join, itertools.permutations(pool))))
print(list(map(''.join, itertools.permutations(pool, 2))))


def permute(arr: list) -> list:
    '''permutaion 함수 구현하기'''
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


print(permute(pool))


# ------------------------------------------------------------------
def solution_most_common_alphabet(my_str: str) -> str:
    '''가장 많이 등장하는 알파벳 찾기 - counter(어떤 원소가 시퀀스 타입에 몇 번이나 등장하는지'''
    dic = Counter(my_str)
    maximum = max(dic.values())

    # filter 함수
    result = filter(lambda x: x[1] == maximum, dic.items())

    answer = [key for key, value in result]
    answer.sort()

    return ''.join(answer)


my_str = "dfdefdgf"
answer = solution_most_common_alphabet(my_str)
print(answer)

'''counter에 대해서'''
# counter - 해시 가능한 객체를 세기 위한 dict 서브 클래스. 즉, 데이터를 count와 매핑하기 위한 클래스
# 해시 : 임의의 길이를 갖는 임의의 데이터를 고정된 길이의 데이터로 매핑
# list.count의 time complexity는 O(N^2) dictionary O(N)

# Counter().most_common() n개의 가장 item(element, count)를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환
# 개수가 같은 요소를 처음 발견된 순서를 유지. 즉 같은 갯수의 요소가 2개이상이고 most_common()을 구한다면 가장 먼저 발견된 요소를 반환
c = Counter(my_str)
print(f'most_common : {c.most_common(1)}')  # 이걸로는 최대 갯수가지는 원소 전체 구할 수 없음
print(f'most_common : {c.most_common()}')  # Counter() 전체 출력

# a new counter from keyword args
example = Counter(cats=4, dogs=10, rabbits=11, lions=12)
print(f'how many cats are here? : {example["cats"]}')
