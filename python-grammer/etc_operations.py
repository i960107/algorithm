from math import sqrt
import bisect as bs


def for_else(numbers: list) -> None:
    '''flag 대신 for-else 사용하기'''
    # print() 후 return으로 함수 종료시켜도 되지만, 가독성 높게 작성하기위해
    multiplied = 1
    for number in numbers:
        multiplied *= number
        sr = sqrt(multiplied)
        # 4.0 == 4  True int converted to float
        if sr == int(sr):
            print('found')
            return
    # for 문을 break없이 다 수행되었다면
    # else 없이 출력하면 찾은 경우에도 not found 출력됨.
    else:
        print('not found')


# input() 여러개 받기 -> 반복문 사용
# numbers = [int(input()) for _ in range(5)]
# for_else(numbers)


# --------------------------------------------------------------

# 매개변수 default값에 변수 조작한 값 넣어줄 수 없음
# None 으로 받고 함수 안에서 값 넣어주기
def bisect(a, x, lo=0, hi=None):
    '''binary search'''
    # bisect : divide into two parts

    if lo < 0:
        raise ValueError

    if hi:
        if hi > len(a):
            raise ValueError
    else:
        # 인덱스가 아님... len(a)-1 로 쓰지 않음
        # lo 인덱스의 앞쪽을 가르키고 hi는 인덱스의 뒷쪽을 가리키도록
        hi = len(a)

    # lo = hi 이면 통과. lo > hi 이면 false
    # while lo <= hi 로 하면 무한루프 돔
    while lo < hi:
        mid = (lo + hi) // 2
        # 왜 a[mid] == x 를 비교하지 않나?
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


mylist = [1, 2, 3, 7, 9, 11, 33]

# 3의 index를 return : 2. bs.bisect_left()와 같음
print(bisect(mylist, 3))

# insertion point를 return : 2+1 =3. bisect_right와 같음
# return value i is such that all e in a[:i] have e<=x, and all e in a[i] have e>x
# 처음부터 3까지 리스트 list slicing mylist[:bs.bisect(mylist,3)]
# 같은 값이 있으면 뒤에다 넣겠다는 뜻
# bisect는 key가 없으면 key가 들어갈 위치를 반환
print(bs.bisect(mylist, 3))
print(bs.bisect(mylist, 4))

# 기존 항목의 앞 위치를 반환
# the return value i is such that all e in a[:i] have e<x, and all e in a[i:] have e>=x
print(bs.bisect_left(mylist, 3))  # 2
print(bs.bisect_left(mylist, 4))  # 3

# 기존 항목의 뒤 위치를 반환 -> bisect()와 같음
print(bs.bisect_right(mylist, 3))  # 3
print(bs.bisect_right(mylist, 4))  # 3


# --------------------------------------------------------------
class Coord(object):
    '''클래스 인스턴스 출력하기'''

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        # 클래스의 자동 string casting
        # return '({}, {})'.format(self.x, self.y)
        return f'({self.x}, {self.y})'


point = Coord(1, 2)
print(point)

# --------------------------------------------------------------
'''가장 큰수,무한대,inf(infinite)'''
'''최소값을 저장하는 변수에 아주 큰 값을 할당'''
# 모든 수보다 큰 값 -> 어떤 숫자와 비교해도 무조건 크다고 판단됨
min_val = 9999
print(min_val > 1000000000)

min_val = float('inf')
print(min_val)
print(min_val > 1000000000)

max_val = float('-inf')
print(max_val)
print(max_val < -10000000000000000000000000000000000)  # true


# --------------------------------------------------------------
def file_open_while():
    '''myfile.txt 라는 이름의 파일을 읽어오기'''
    f = open('myfile.txt', 'r')
    while True:
        line = f.readline()
        # EOF를 만날때까지
        if not line:
            break
        # 공백 포함한 str
        # python에서는 \n을 한줄로 인식하는 듯?- 다음줄과 사이에 공백 한줄 출력됨
        # 빈줄이라면 \r\n일테므로 한줄 공백 출력됨
        # 마지막라인에는 \n대신 eof있음
        print(line)
        # 단어로 나눠서 list반환
        raw = line.split()
        print(f'raw{raw}')
    f.close()


def file_open_with_as():
    '''with-as 구문을 사용하여 file read'''
    with open('myfile.txt') as file:
        for line in file.readlines():
            # strip() 앞뒤 whitespace제거 strip('0') 앞뒤 0 제거
            # split() str -> list로 \t 기준으로 쪼개기. 언제 tab으로 인식되지? 네칸 띄우기로는 tab으로 인식 안되는데
            print(line.strip().split('\\t'))
    # file을 close하지 않아도 됨 - with-as블록이 종료되면 파일 자동으로 close
    # readlines가 EOF까지만 읽으므로, while문 안에서 EOF를 체크할 필요 없음.


file_open_while()
file_open_with_as()
