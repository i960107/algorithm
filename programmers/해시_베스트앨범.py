from collections import defaultdict


def solution(genres: list, plays: list) -> list:
    # O(n)
    album = [[i, 0] for i in range(len(genres))]

    # 장르 내 순위도 기록하고 있어야함.
    # O(n)
    d_genres = defaultdict(int)
    for i, genre in enumerate(genres):
        d_genres[genre] += plays[i]

    # O(NlogN)
    album = sorted(album, key=lambda x: (d_genres[genres[x[0]]], plays[x[0]], -x[0]), reverse=True)

    # O(n)
    for i, (music, priority) in enumerate(album):

        if i == 0 or genres[music] != genres[album[i - 1][0]]:
            # i==0 조건 만족하면 or 뒤 조건 검사하지 않기 때문에 index error 나지 않음
            album[i][1] = 0
        elif i == len(album) - 1 or genres[music] == genres[album[i - 1][0]]:
            album[i][1] = album[i - 1][1] + 1

    # O(n)
    return [music for music, priority in album if priority <= 1]


def solution_others(genres: list, plays: list) -> list:
    #복잡도 비슷. 효율성 테스트시 시간 더 걸리기도 덜 걸리기도 어떤 차이가 있을가?
    answer = []

    # {genre:[(음악ID, play횟수)]}
    # list안 튜플. 같은 장르안 음악끼리는 순서 필요 없음. 변경될 일 없음.
    dic1 = defaultdict(list)
    dic2 = defaultdict(int)

    for i, (g, p) in enumerate(zip(genres, plays)):
        dic1[g].append((i, p))
        dic2[g] += p

    # 가장 많이 play된 장르순 정렬
    # O(NlogN) 장르개수* 장르별 음악 개수
    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        # 장르별 가장 많이 play 노래 정렬된 list에서 2개까지만 list slicing
        for (i, p) in sorted(dic1[k], key=lambda x: (x[1], -x[0]), reverse=True)[: 2]:
            answer.append(i)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution_others(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
