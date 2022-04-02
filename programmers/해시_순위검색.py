from typing import List
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution1(info: List[str], query: List[str]) -> List[int]:
    # 해시 사용 효율성 통과 불가
    answer = []
    # 숫자로 비교하는게 빠르다고 생각해서 변경하는데
    # 인덱스를 사용하면 겹쳐서 subset 비교가 정확히 안됨.set으로 바꾸면 중복값 제거됨. dictionary로 관리? 확장성은?
    # languages = ['cpp', 'java', 'python']
    # jobs = ['backend', 'frontend']
    # careers = ['junior', 'senior']
    # foods = ['chicken', 'pizza']

    counter = defaultdict(int)
    for person in info:
        x = person.split()
        x[-1] = int(x[-1])
        # key를 list로 하면 unhashable type 에러발생
        # hash: object에 저장된 내용을 기준으로 한 개의 정수를 생성하여 반환하는 함수
        # hahsable: numeric, immutable  container(string, tuple.)
        # unhashable - 리스트, 셋, 딕셔너리와 같이 데이터 변경이 가능한 컨테이너는 hashable하지 않음
        counter[tuple(x)] += 1

    # O(N^2)
    # 효율성이 중요한 문제인데... input  최대 100,000 시간초과 문제
    # 점수를 먼저 비교하는건 어때? 점수별로 list해놓으면 검색해야할 대상이 줄어들자나! 검색 대상을 줄이는게 핵심이ㅣㅈ!
    for i in range(len(query)):
        conditions = list(condition for condition in query[i].split() if condition not in ('-', 'and'))
        score = int(conditions.pop())
        count = 0
        for x in counter:
            # 빈 셋일때 모든 셋의 서브셋이됨
            if set(conditions).issubset(set(x[:-1])) and (int(x[-1]) >= score):
                count += 1
        answer.append(count)
    return answer


def solution2(information: List[str], queries: List[str]) -> List[int]:
    # 아주 중요햐!!~~!@아ㅓㄹㄴ아러마너리ㅏㄴ
    answer = []
    # 점수별로 모아볼까 1이상 100,000이라는데.. 이게 가능할까?
    # 뭘 기준으로 모아보지?
    # 지원자들을 그룹별로 적절하게 미리 분류해두기
    # 점수를 기준으로 뱅려해두고 이진 배열을 사용해서 몇 명인지 세기
    # 108개의 key:value set 감당 가능?
    dic = defaultdict(list)
    for info in information:
        condition = info.split()
        score = int(condition.pop())
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                # 모든 조건의 경우의 수에 대해 딕셔너리? -> 공간 복잡도는?
                dic[key].append(score)
    for value in dic.values():
        value.sort()
    print(dic.items())

    for query in queries:
        query = query.replace("and", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer


def solution3(information: List[str], queries: List[str]) -> List[int]:
    answer = []
    # 공간복잡도 조금 희생하더라도 108개 해시로 제한하는게 탐색속도 매우 빠름
    # 최대 108개 아이템은 많은것도 아님
    # 조건 : 해당하는 점수(오름차순 정렬)
    d = defaultdict(list)

    # 1.매조건마다 해당하는 조건(16가지)에 score 넣어주기
    test = 0
    for info in information:
        conditions = info.split()
        score = int(conditions.pop())
        for i in range(5):
            # 총 16가지 * infomatin 개수 6개 -> 만들어진 key는 겹치는거 제외 54개
            for combi in combinations([0, 1, 2, 3], i):
                test +=1
                print(combi)
                temp = conditions.copy()
                for c in combi:
                    temp[c] = '-'
                temp = ''.join(temp)
                d[temp].append(score)
    # 2.이진탐색을 위해 점수 오름차순 정렬하기
    for value in d.values():
        value.sort()

    # 3.쿼리에 해당하는 키를 찾아서 해당 점수 이상의 개수 찾기
    for query in queries:
        # 여러개 구분자 있을때 ' and '을 ' '으로 바꾼 후 split()호출 가능
        conditions = query.split()
        score = int(conditions.pop())
        conditions = ''.join(condition for condition in conditions if condition != 'and')
        count = len(d[conditions]) - bisect_left(d[conditions], score)
        answer.append(count)

    return answer


print(solution3(["java backend junior pizza 150",
                 "python frontend senior chicken 210",
                 "python frontend senior chicken 150",
                 "cpp backend senior pizza 260",
                 "java backend junior chicken 80",
                 "python backend senior chicken 50"],
                ["java and backend and junior and pizza 100",
                 "python and frontend and senior and chicken 200",
                 "cpp and - and senior and pizza 250",
                 "- and backend and senior and - 150",
                 "- and - and - and chicken 100",
                 "- and - and - and - 150"]))
