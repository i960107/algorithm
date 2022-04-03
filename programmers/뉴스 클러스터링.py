from collections import Counter


def solution(str1: str, str2: str) -> int:
    '''[1차]뉴스 클러스터링'''
    # 중복을 허용하면서 합집합, 교집합

    # def make_group(s: str) -> dict:
    #     d = {}
    #     for i in range(0, len(s) - 1):
    #         curr = s[i:i + 2]
    #         if curr.isalpha:
    #             curr = curr.lower()
    #             d[curr] = d.get(curr, 0) + 1
    #
    #     return d
    #
    # d1 = make_group(str1)
    # d2 = make_group(str2)

    # 문자열 : [str1에서의 횟수, str2에서의 횟수]
    d = dict()
    for i in range(len(str1) - 1):
        curr = str1[i:i + 2]
        if curr.isalpha():
            curr = curr.lower()
            curr_cnt = d.get(curr, [0, 0])
            curr_cnt[0] += 1
            d[curr] = curr_cnt

    for i in range(len(str2) - 1):
        curr = str2[i:i + 2]
        if curr.isalpha():
            curr = curr.lower()
            curr_cnt = d.get(curr, [0, 0])
            curr_cnt[1] += 1
            d[curr] = curr_cnt

    # 하나로 합치기 가능? 경제성 있나?
    # for i in range(max(len(str1), len(str2)) - 1):
    #     part1 = str1[i:i + 2] if i < len(str1) - 1 else ""
    #     part2 = str2[i:i + 2] if i < len(str2) - 1 else ""
    #
    #     if part1.isalpha():

    union = 0
    intersection = 0

    for key, (cnt1, cnt2) in d.items():
        union += max(cnt1, cnt2)
        intersection += min(cnt1, cnt2)

    # 두집합 모두 공집합일 경우 union = 0
    jaccard = intersection / union if union != 0 else 1
    return int(jaccard * 65536)


def solution2(str1: str, str2: str) -> int:
    # dict 참조는 O(1)이니깐 따로 만들었어도 됐네! 그럼 간단했겠네..
    d1 = Counter(str1[i:i + 1].lower() for i in range(len(str1) - 1) if str1[i:i + 1].isalpha())
    d2 = Counter(str1[i:i + 1].lower() for i in range(len(str1) - 1) if str1[i:i + 1].isalpha())

    # 교집합은 key로 다른 dict 참조하면 구할 수 있음 합집합은 어떻게?
    # for key, value in d1:
    #     if
    return 0


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
