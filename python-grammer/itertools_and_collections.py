import itertools

'''iterable 곱집합 구하기'''


def solution_cartesian_product(*my_list):
    # list이름이 list이면 안됨..
    print(f'mylist {my_list}')
    print(*my_list)
    print(*my_list[0])

    # cartesian product - 데카르트 곱. DB의 join과 비슷
    # 두개 이상의 리스트의 모든 조합을 구할때 사용
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
        answer.append(element)
    return answer


def solution_sum(my_list: list) -> list:
    '''방법2 - sum함수'''
    # sum(iterable, start_value)
    # 빈 배열에서 시작해서 숫자 원소 하나씩 가져와서 추가하기
    # 2차원 리스트일 경우 각 요소 배열 다 돌고 난 다음에 다음 요소 배열 돔
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
    return [element (for array in my_list) for element in array]


my_list = [[1, 2], [3, 4], [5, 6]]
print(solution_for(my_list))
print(solution_for(my_list))

# 방법 5 - reduce 함수 이용 1
# answer = list(reduce(lambda x, y: x + y, my_list))
#
# # 방법 6 - reduce 함수 이용 2
# answer = list(reduce(operator.add, my_list))
#
# # 방법 7 - numpy 라이브러리의 flatten 이용 (각 원소의 길이가 동일한 경우에만 사용 가능)
# answer = np.array(my_list).flatten().tolist()
#
# dict = {}
# dict.items()
# k
# ------------------------------------------------------------------
# permutations순열 순서가 있는것 nPr = n!/(n-r)!
# combinations조합 순서가 없는것 nCr = nPr/r! = n!/r!(n-r)!
# 주의 : combinations, permutations, product 모두 generator이기 때문에 list()로 캐스팅하여 저장하지 않으면
# 한번의 루핑이후 사라짐
pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool))))
print(list(map(''.join, itertools.permutations(pool, 2))))


# ??
def permute(arr):
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
'''가장 많이 등장하는 알파벳 찾기 - counter(어떤 원소가 시퀀스 타입에 몇 번이나 등장하는지'''


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

# def solution_most_common_alphabet(my_str):
#     c = collections.Counter(my_str)
#     # sort() 함수는 반환 값 없기 때문에 바로 출력할 수 없음.
#     most_common = c.most_common(1)
#     most_common.sort()
#     # 알파벳만 리스트로 모으기
#     print(f'most_common : {most_common}')
#     print(f'가장 많이 등장하는 알파벳 사전 순 : {"".join([counters[0] for counters in most_common])}')
#     # print(f'가장 많이 등장하는 알파벳 사전 순 : {c}')
