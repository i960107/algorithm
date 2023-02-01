from typing import List
'''문제 1B-원소의 합 구하기'''


def get_sum(data:List[int], n:int) -> int:
    answer = 0
    for i in range(len(data)):
        answer += data[i]
    return answer


if __name__ == '__main__':
    n = int(input())
    data = [int(word) for word in input().split()]
    answer = get_sum(data,n)
    print(answer)
