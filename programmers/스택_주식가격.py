# 효율성 테스트 통과는 되지만 복잡도 O(n^2) -> 5배 이상 오래 걸림..
# 같은 원소에 대해서 검사 여러번 이뤄짐.
def solution(prices: list) -> list:
    answer = [len(prices) - 1 - i for i in range(len(prices))]
    # 원소 하나씩 돌면서 자기보다 작은 원소 만날때까지 반복
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break

    return answer


# 복잡도 O(n)
def solution_others(prices: list) -> list:
    answer = [0] * len(prices)
    stack = []

    # stack에 인덱스와 값을 같이 쌓거나, 인덱스만 쌓아서 인덱스로 참조하거나
    for i, price in enumerate(prices):
        # 마지막 원소 pop()하면 if stack -> Falsy됨
        # python falsy : None, [],(),{},"" 즉 빈 iterable,0
        # stack에 쌓으면 한번에 자기 보다 작은 원소 모두 검사 가능
        # stack[-1] -> stack.peek()과 같
        # 원소 하나씩 돌면서 앞의 원소들과 비교하기.
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        # prices배열 그대로 가지고 있으니 stack에는 index만 저장하면 됨.
        stack.append(i)

    # stack에 마지막까지 남아있다는 건 배열이 끝날때까지 자기보다 작은 가격을 만나지 않았다는 것
    # 따라서 마지막 인덱스와의 차이를 계산하기
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer


def solution_practice(prices: list) -> list:
    answer = [0] * len(prices)

    stack = []
    for i, ip in enumerate(prices):
        while stack and stack[-1][1] > ip:
            j, jp = stack.pop()
            answer[j] = i - j
        stack.append((i, ip))

    while stack:
        i, ip = stack.pop()
        answer[i] = len(prices) - 1 - i

    return answer


list = [1, 2, 3, 2, 3]
print(solution(list))
print(solution_others(list))
print(solution_practice(list))

list = [4, 3, 2, 4, 3, 1, 2]
print(solution(list))
print(solution_others(list))
print(solution_practice(list))
