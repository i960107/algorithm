from collections import Counter


def solution(call: str) -> str:
    answer = ""
    counter = Counter(call.lower())
    max_count = counter.most_common(1)[0][0]
    max_count_nums = counter.most_common(1)[0][0]
    # 가장 많은 원소의 개수
    print(f'가장 많은 원소 {counter.most_common(1)[0][0]} ({counter.most_common(1)[0][1]})')
    print(counter.most_common(1)[0][1] >= len(call) // 2)
    # 과반수 이상이면? 6개일 경우 3개이상 7개일경우도 3개이상?
    if counter.most_common(1)[0][1] > len(call) // 2:
        print("여기")
    return answer


print(solution("abcabcdefabc"))
print(solution("abxdeydeabz"))
print(solution("abcabca"))
print(solution("ABCabcA"))
