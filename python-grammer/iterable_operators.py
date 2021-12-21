import itertools
from functools import reduce
import operator
import numpy as np

'''for문을 사용하지 않고 리스트를 이어붙이기'''

my_list = [[1, 2], [3, 4], [5, 6]]
# 방법 1 - sum 함수
#sum(iterable, start_value)
#빈 배열에서 시작해서 숫자 원소 하나씩 가져와서 추가하기
answer = sum(my_list, [])

# 방법 2 - itertools.chain
answer = list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools.chain과 unpacking
answer = list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
#배열 원소 하나씩 가져온 후 각 배열 원소 안 데이터 하나씩 가져와서 리스트 생성
answer = [element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
answer = list(reduce(lambda x, y: x + y, my_list))

# 방법 6 - reduce 함수 이용 2
answer = list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용 (각 원소의 길이가 동일한 경우에만 사용 가능)
answer = np.array(my_list).flatten().tolist()
