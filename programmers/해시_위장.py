import collections
import itertools
from functools import reduce


def solution(clothes: list) -> int:
    d = collections.defaultdict(set)

    for c in clothes:
        # 존재하지 않는 키에 값 삽입하려고 하면 get(키, set())으로 들고 오는 주소가 해시 주소가 아님.
        # get()으로 가져오는 주소는 key가 dictionary에 없을 경우 key와 연결되지 않는 새로운 주소 일 수 있음.
        # 기존 set 주소 혹은 없다면 새로운 set() 생성한 곳에 추가한 다음 key에 넣어주기.
        # d_set = set(d.get(c[1], set()))
        # d_set.add(c[0])
        # d[c[1]] = d_set
        d[c[1]].add(c[0])

    answer = 1
    for kinds in d.keys():
        answer *= (len(d[kinds]) + 1)

    return answer - 1


def solution_array(clothes: list) -> int:
    array = {}

    # underscore : 값을 무시한다는 뜻
    for _, type in clothes:
        # 각 타입별로 몇개의 이름이 있는지만 알면됨. 이름은 알 필요 없음.
        array[type] = array.get(type, 0) + 1
        # if type in array:
        #     array[type] += 1
        # else:
        #     array[type] = 1
    cnt = 1
    for i in array.values():
        # 타입의 각 아이템을 착용하는것 + 그 타입을 착용하지 않는 것
        cnt *= (i + 1)
        # 아무것도 안 입는 경우
    return cnt - 1


def solution_reduce(clothes: list) -> int:
    # 각 type이 몇번 등장하는지만 세면 됨
    # solution_array()와 같은 방법.
    cnt = collections.Counter([type for name, type in clothes])
    # reduce에 초기값 정해주지 않으면? 앞의 두원소로 처음 연산 수행.
    # initial value 없고 iterable 원소 개수 1면 자기자신을 반환
    return reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1


def solution_combinations(clothes: list) -> int:
    '''itertools.product() 를 사용해서. 테스트에서 시간초과되는 방법.'''

    cnt = collections.Counter([type for _, type in clothes])
    #값은 상관없이. 의상의 종류 * 의상의종류별 의상의 수의 2차원 배열 필요.
    l = [[1] * (c + 1) for c in cnt.values()]
    # 두개 이상의 리스트에서 모든 조합을 계산해야 한다면, product사용(단 unpacking한 1차원 배열을 매개변수로 넣어주어야함)
    #itertool.product(*l) -> 모든 조합을 담음 len(list(itertool.product(*l))) 보다는
    # product()의 결과 iterator의 원소의 개수만큼 1을 더해주는게 더 나은 방법

    # 조합의 경우의 수 -1을 해주는 이유? 선택하지 않거나 선택하는 경우의 수가 각 배열의 길이가 됨. 즉 모두 안 입는 경우 포함.
    print(l)
    print(list(itertools.product(*l)))
    return sum(1 for _ in itertools.product(*l)) - 1


clothes1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes1))
print(solution_array(clothes1))
print(solution_reduce(clothes1))
print(solution_combinations(clothes1))

print(solution(clothes2))
