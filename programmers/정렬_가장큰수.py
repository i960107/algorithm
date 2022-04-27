from typing import List


def solution(numbers: list) -> str:
    # 문자열로 취급
    numbers = [str(x) for x in numbers]

    # 내가 만든 기준(가장 크게 만들 수 있는 수)으로 정렬하기
    # x*4 같은 문자를 4번 반복하라는 뜻.
    # 왜 4번 반복하지?
    # 괄호로 묶어주지 않으면 int object is not subscriptable(index나 key로 iterable의 원소에 접근하는 ) 에러 발생
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 0 만 2개이상 들어있는 경우 0으로 return 해야 함
    # 정렬된 결과로 가장 첫번째 원소가 0 이라는 것은 나머지 원소가 다 0이라는 뜻
    # 방법(2) int로 캐스팅 해서 0으로 변경후 다시 str로 변경하기. 모든 경우에 대해 type casting이 일어나므로 좋지 않은 방법
    return "".join(numbers) if numbers[0] != '0' else '0'


print(solution([6, 10, 2]))


def solution2(nums: List[int]) -> str:
    '''파이썬 인터뷰 풀이-삽입정렬'''

    # a+b < b+a 이면 swap
    # 문제에 적합한 비교 함수
    def to_swap(n1: int, n2: int) -> bool:
        # swap이 필요한지
        # 그 앞 숫자랑 붙여서 더 큰지 아닌지 확인
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    # 뒤에서부터 앞으로 탐색해가면서 삽입 위치 결정. 연결 리스트처럼 포인터를 맨 앞으로 옮길 필요 없음.
    # 제자리 정렬
    i = 1
    for i in range(1, len(nums)):
        j = i
        # j == 0까지 비교해야 하는 것 아님?
        for j in range(i, 0, -1):
            if to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return "".join(map(str, nums)) if nums[0] != 0 else "0"


print(solution2([10, 2]))
print(solution2([3, 30, 34, 5, 9]))
