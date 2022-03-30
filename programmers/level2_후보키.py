from collections import Counter
from itertools import combinations
from functools import reduce


# def solution_candidate_key(relation: list) -> int:
#     unique = 0
#     non_unique = {}
#
#     for i in range(len(relation[0])):
#         counter = Counter(relation[j][i] for j in range(len(relation)))
#         # 중복된 원소가 있을때
#         if len(counter) != len(relation):
#             # 고유키가 아닌 키들과 복합키가 기본키가 될 수 있는지 살피기
#             non_unique[i] = [key for key in counter if counter[key] > 1]
#         # 중복된 원소가 없을때
#         else:
#             unique += 1
#
#     # 중복된 컬럼들끼리 복합키가 후보키 될 수 있을지 검사
#     # non_unique 배열은 오름차순 정렬된 상태. 자기 보다 뒤 키만 확인하면 됨.
#     # 확인하고 기본키 가능하면 두개 배열에서 제거하기
#     # 중복값 검사!!
#     # 세개 합쳐서 복합키 될 수도 있음. 어떻게 검사하지?
#     for i in non_unique:
#         for j in non_unique:
#             counter = Counter(relation[k][i] + relation[k][j] for k in range(len(relation))
#                               if relation[k][i] in non_unique[i])
#             if all(v <= 1 for v in counter.values()):

#                 unique += 1
#     return unique

def solution_candidate_key(relation: list) -> int:
    unique = 0
    fields = {i for i in range(len(relation[0]))}
    duplicated_rows = dict()

    for i in range(len(relation[0])):
        counter = {}
        for j in range(len(relation)):
            counter[relation[j][i]] = counter.get(relation[j][i], []) + [j]

        # 중복된 원소가 없을때
        if len(counter) == len(relation):
            fields.remove(i)
            unique += 1
        else:
            # 중복된 row 넣기
            # 배열을 set으로 만들면 unhashable type 'list' 에러 발생
            duplicated_rows[i] = set(row for key in counter if len(counter[key]) > 1 for row in counter[key])

    print((duplicated_rows.items()))

    # 3개 이상 필드의 복합키도 존재 가능!!
    for i in range(2, len(duplicated_rows) + 1):
        for combi in combinations(duplicated_rows, i):
            elements = set()
            # rows = reduce(lambda x, y: x.update(duplicated_rows[y]), combi, set())
            rows = set()
            for field in combi:
                rows.update(duplicated_rows[field])

            for row in rows:
                e = ''.join([relation[row][field] for field in combi])
                if e in elements:
                    break
                else:
                    elements.add(e)

            if len(elements) == len(rows):
                for field in combi:
                    duplicated_rows.pop(field)
                unique += 1

    return unique


def solution(relation: list) -> int:
    unique = 0
    duplicated_fields = set(i for i in range(len(relation[0])))

    # 1개 기본키 고르고, 나머지 필드에 대해서 중복되는 행 거르기
    for i in range(len(relation[0])):
        counter = Counter(relation[j][i] for j in range(len(relation)))

        if len(counter) == len(relation):
            unique += 1
            duplicated_fields.discard(i)

    count = 2
    while True:
        if count > len(duplicated_fields):
            break
        for combi in combinations(duplicated_fields, count):
            elements = set()

            for row in range(len(relation)):
                e = ''.join(relation[row][field] for field in combi)
                if e in elements:
                    break
                else:
                    elements.add(e)

            # 제외를 하면 안돼! 다 검사하고 난 후 복합키가 되지 않은 것에 대해서 다른 필드 붙여서 검사해보기
            # 복합키가 기본키가 될 수 있을때
            if len(elements) == len(relation):
                unique += 1
            count += 1
    return unique


def solution_others(relation: list) -> int:
    row = len(relation)
    col = len(relation[0])

    # 가능한 모든 복합키 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    unique = []
    for fields in combi:
        tmp = [tuple([item[field] for field in fields]) for item in relation]
        
        if len(set(tmp)) == row:
            put = True

            for x in unique:
                if set(x).issubset(fields):
                    put = False
                    break
            if put: unique.append(fields)

    return len(unique)


print(solution_others(
    [["100", "ryan", "music", "2"],
     ["200", "apeach", "math", "2"],
     ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"],
     ["500", "muzi", "music", "3"],
     ["600", "apeach", "music", "2"]]))
