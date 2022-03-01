def solution(numbers: list) -> str:
    # 문자열로 취급
    numbers = [str(x) for x in numbers]
    # 내가 만든 기준(가장 크게 만들 수 있는 수)으로 정렬하기
    # x*4 같은 문자를 4번 반복하라는 뜻.
    # 괄호로 묶어주지 않으면 int object is not subscriptable(index나 key로 iterable의 원소에 접근하는 ) 에러 발생
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 0 만 2개이상 들어있는 경우 0으로 return 해야 함
    # 정렬된 결과로 가장 첫번째 원소가 0 이라는 것은 나머지 원소가 다 0이라는 뜻
    # 방법(2) int로 캐스팅 해서 0으로 변경후 다시 str로 변경하기. 모든 경우에 대해 type casting이 일어나므로 좋지 않은 방법
    return "".join(numbers) if numbers[0] != '0' else '0'


print(solution([6, 10, 2]))
