from functools import reduce

'''2차원 list 뒤집기'''


def solution_for(mylist):
    # answer = [[None] * len(mylist)] * len(mylist)
    # 안됨. 2차원 배열안 요소 배열은 모두 같은 객체로 인식되어서
    # 값 삽입시 전체 배열에 영향이 감.
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
    print(f'numbers : {numbers}')
    p = reduce(lambda x, y: x * y, numbers)
    return p


def product2(numbers):
    print(f'numbers : {numbers}')
    p = reduce(lambda x, y: x * y, numbers)
    return p


primes = [2, 3, 5, 7, 11, 13]
# argument와 parameter 둘다 asterisk 필요? 언패킹한 상태로
# 6개의 데이터
print(*primes)
# 1개의 리스트 6개의 원소
print(primes)

# argument로 *를 받기 때문에 데이터 개수 상관없음.
print(f'product  {product(primes)}')
print(f'product * {product(*primes)}')

# argument로 데이터 하나를 받기 때문에 unpacking된 상태로 전달하면 TypeError발생
print(f'product2  {product2(primes)}')
print(f'product2 * {product2(*primes)}')

'''i번째 원소가 i+1번째 원소'''


# index를 사용하지 않고 각 원소에 접근 가능
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1, number2))
    return answer
