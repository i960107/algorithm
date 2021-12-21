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

'''for문을 사용하지 않고 리스트를 이어붙이기'''

my_list = [[1, 2], [3, 4], [5, 6]]
# 방법 1 - sum 함수
# sum(iterable, start_value)
# 빈 배열에서 시작해서 숫자 원소 하나씩 가져와서 추가하기
answer = sum(my_list, [])

# 방법 2 - itertools.chain
answer = list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools.chain과 unpacking
answer = list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
# 배열 원소 하나씩 가져온 후 각 배열 원소 안 데이터 하나씩 가져와서 리스트 생성
answer = [element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
answer = list(reduce(lambda x, y: x + y, my_list))

# 방법 6 - reduce 함수 이용 2
answer = list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용 (각 원소의 길이가 동일한 경우에만 사용 가능)
answer = np.array(my_list).flatten().tolist()

dict = {}
dict.items()
k

# permutations순열 순서가 있는것 nPr = n!/(n-r)!
# combinations조합 순서가 없는것 nCr = nPr/r! = n!/r!(n-r)!

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
