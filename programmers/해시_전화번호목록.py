import re


def solution_regexp(phone_book):
    for phone in phone_book:
        # regexp 표현시 // 필요없음?
        pattern = re.compile('^' + phone)
        # 복잡도 O(n^2)으로 매우 높음
        for phone2 in phone_book:
            if phone != phone2 and pattern.match(phone2):
                return False
    else:
        return True


def solution_sort(phone_book):
    phone_book.sort()
    # 정렬된 상태이기 때문에 같은 번호가 있다면 바로 뒤에 있을것, 하나 이상이면 바로 return
    # 복잡도 O(NlogN)
    # zip()의 복잡도는 O(N)
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         return False
    # else:
    #     return True
    #두가지 방법 가능. 뭐가 더 효율적인지?
    for i in range(len(phone_book)):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    else:
        return True




print(solution_regexp(['119', '96564223', '11955234']))
print(solution_sort(['119', '96564223', '11955234']))


def solution_list_slicing(phone_book):
    # 꼭 복잡도 O(N^2)이라고 할 수 없음? 최악의 경우 반환값이 True인 경우 O(N^2)이지만 최선의 경우 O(n)
    # 최악의 경우 실행 속도 너무 느리기 때문에 입력값의 특징을 예측할 수 없는 코테에서는 solution_sort()가 적합
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            # 자신보다 뒤에있는 것들을 양방향으로 비교하기 때문에 p1 in p2 or p2 in p1, 앞에 것 체크 안 해도됨
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True
