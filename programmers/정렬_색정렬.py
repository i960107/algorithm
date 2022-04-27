from typing import List


def sort_colors(colors: List[int]):
    '''네덜란드 국기 문제- 퀵 정렬의 개선 아이디어'''
    # partitioning 을 세부분으로 하기. 작은 부분, 같은 부분, 큰 부분
    # red = 0 white = 1 blue = 2
    # red, white, blue 순으로 정렬해야함 -> white를 기준으로 세부분으로 나누기
    # 각 index는 각 색깔이 시작하는 위치를 가리킴? 아님
    red, white, blue = 0, 0, len(colors)  # 배열 인덱스 바깥에 있다

    # white = blue시 비교 완료
    while white < blue:
        if colors[white] < 1:
            colors[red], colors[white] = colors[white], colors[red]
            white += 1
            red += 1
        elif colors[white] > 1:
            blue -= 1
            colors[white], colors[blue] = colors[blue], colors[white]
        else:
            white += 1
    print(colors, red, blue)

    # 종료시 red는 1보다 작은 마지막 인덱스 +1(1일수도,2일수도),blue는 1보다 큰 인덱스의 처음을 가리킴


print(sort_colors([2, 0, 2, 2, 1, 0]))
print(sort_colors([2, 0, 2, 2, 0]))
