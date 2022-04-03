from collections import defaultdict
from typing import List


def solution(id_list: list, report: list, k: int) -> list:
    answer = [0] * len(id_list)

    # defaultdict() 매개변수 default값 반환하는 함수. lambda :set()과 같음
    # 양방향으로 1)신고당한 사람을 key로 2)신고한사람을 key로 dict만들기

    # 1) 신고당한사람 : 신고한 사람들
    d_reported = defaultdict(set)
    # d_reported = {}
    for r in report:
        reporter = r.split(" ")[0]
        reported = r.split(" ")[1]
        # # 아무것도 안넣은 상태에서는 None임. get으로 가져오면 안됨.인덱스로 가져오기.
        # print(d_reported.get(reported))

        # set 자료형은 참조형
        # int 자료형은 기본형이기 때문에 +1 한 후 값에 대입해주어야 함.
        # d_reported[reported].add(reporter) #defaultdict후 인덱스로 검색 안 후 첫번째 값 삽입시 값 들어감
        # d_reported.get(reported, set()).add(reporter) # {}로 딕셔너리 선언후 get으로 검색 및 Default 값 정해준후 값 삽입시 값 삽입 안됨.
        # default dict으로 선언한 경우 get 아니고 인덱스로 값 검색!
        d_reported[reported].add(reporter)

        # print(list(d_report)) 키만 출력
        # print(list(d_reported.items()))  # (키,값) 형태로 배열 출력

    # 1) 신고한사람 : 정지 당한 사람을 신고한 횟수
    d_report = defaultdict(int)
    for reported, reporters in d_reported.items():
        if len(reporters) >= k:
            for reporter in reporters:
                d_report[reporter] = d_report[reporter] + 1

    # # 여기 복잡도를 어떻게 줄이지? 정지먹은 사람을 신고한 횟수를 count해야 하는데.
    # for reported, reporters in d_reported.items():
    #     # 정지 대상
    #     if len(reporters) >= k:
    for i, name in enumerate(id_list):
        answer[i] = d_report.get(name, 0)

    return answer


print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2))

print(solution(
    ["con", "ryna"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3)
)


def solution_others(id_list: list, report: list, k: int) -> list:
    answer = [0] * len(id_list)
    # 모든 유저에 대해서 0값을 default로 가지는 dict 생성
    reports = {x: 0 for x in id_list}

    # report 배열이 신고한 사람 신고당한 사람 1:1 문자열을 담고 있기 때문에
    # report 배열 자체를 set으로 만들어서 중복을 제거해줄 수 있음.
    # O(N)
    # list ot set : O(N)
    for r in set(report):
        reports[r.split()[1]] += 1

    # 신고당한 사람만을 대상으로 신고당한 횟수를 체크하고, 정지 대상이면 유저 리스트에서 index를 찾아서 answer +=1
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


def solution_practice(id_list: List[str], report: List[str], k: int) -> List[int]:
    answer = [0] * len(id_list)
    d_users = {user: idx for idx, user in enumerate(id_list)}
    d_reported = defaultdict(set)

    for r in report:
        reporter, reported = r.split()
        reporter, reported = d_users[reporter], d_users[reported]
        d_reported[reported].add(reporter)

    # d_reported.items() -> O(N)
    # 사람 자체가 아니라 count만 하면 공간 복잡도 낮음
    for reported, reporters in d_reported.items():
        if len(reporters) >= k:
            for user in reporters:
                answer[user] += 1
    return answer


print(solution_practice(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2))

print(solution_practice(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3)
)
