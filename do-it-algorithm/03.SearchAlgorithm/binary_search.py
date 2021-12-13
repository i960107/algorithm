from typing import Any, Sequence


def bin_search(a: Sequence, key: Any):
    '''이진 검색 알고리즘'''

    lower = 0
    upper = len(a) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            upper = middle - 1
        else:
            lower = middle + 1
    raise ValueError


if __name__ == '__main__':
    num = int(input(f'원소 수를 입력하세요 :'))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요.')
    x[0] = (int(input(f'x[0] : ')))

    for i in range(1, num):
        while True:
            x[i] = (int(input(f'x[{i}] : ')))
            # 중복된 값 인정?//정확하지 않음 값 나옴. 일치하는 원소중 가장 먼저 만난 원소의 인덱스를 반환
            if x[i] >= x[i - 1]:
                break

    # 입력값을 int형으로 변환해주지 않으면 string으로 인식
    key = int(input('검색할 값을 입력하세요'))

    try:
        idx = bin_search(x, key)
    except ValueError:
        print('검색값을 갖는 원소가 없습니다')
    else:
        print(f'검색값은 x[{idx}]에 있습니다')
