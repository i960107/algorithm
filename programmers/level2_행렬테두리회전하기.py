from typing import List


def solution(rows: int, columns: int, queries: List[List]) -> List[int]:
    answer = []
    # stack = []
    # rows * columns 배열을 만들어두는건 공간 복잡도 너무 높지 않나?
    # dict형에 바뀐 자리만 넣어둘까?
    # key: 행+열 문자열, value: 값. 값이 있다면 그자리 값이 바뀐 것
    d = {}
    for x1, y1, x2, y2 in queries:
        # 바꿀 숫자들은 계산 stack에 넣은 후 pop?
        # 첫번째 결과가 두번째에 영향을 미칠 수 있고 계산불가, 돌면서 값 기억해두는게 좋음
        # 바꿀 숫자들을 계산해서 바로바로 넣어주기?
        # 돌면서 전 숫자 기억해두었다가 현재 위치랑 연결 ->d에 넣어주기
        min = -1
        r, c = x1, y1
        cnt = (x2 - x1) * 2 + (y2 - y1) * 2 + 1
        prev = None
        while True:
            if cnt == 0:
                break
            box_id = (r - 1) * columns + c

            if d.get(box_id, None) is not None:
                curr = d[box_id]
            else:
                curr = box_id

            if prev:
                d[box_id] = prev
            prev = curr
            cnt -= 1
            min = curr if min == -1 or min > curr else min
            # 1단계 왼->오 진행
            if r == x1 and c < y2:
                c += 1
            # 2단계 위->아래 진행
            elif r < x2 and c == y2:
                r += 1
            # 3단계 오->왼 진행
            elif r == x2 and c > y1:
                c -= 1
            # 4단계 아래->위 진행
            elif r > x1 and c == y1:
                r -= 1
            # 반복문 종료

        answer.append(min)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
