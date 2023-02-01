from typing import List

'''문제 1C-배열의 최대값'''


def get_max(data: List[int], n: int) -> int:
    answer = 0
    for i in range(len(data)):
        answer += data[i]
    return answer


if __name__ == '__main__':
    n = int(input())
    data = [int(word) for word in input().split()]
    answer = get_max(data, n)
    print(answer)
