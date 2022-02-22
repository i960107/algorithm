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


def solution_sort(phone_book: list) -> bool:
    # 정렬된 상태이기 때문에 같은 번호가 있다면 바로 뒤에 있을것, 하나 이상이면 바로 return
    # 복잡도 O(NlogN)
    phone_book.sort()
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         return False
    # else:
    #     return True

    # 두가지 방법 가능. 뭐가 더 효율적인지? zip해서 iterable객체 만들고 그 후에 iteration하는것 vs 인덱스로 배열에 접근*원소의 개수 -> zip을 사용하지 않는게 더 최적화된 방법.
    # list slicing 복잡도 O(N) N: 슬라이싱 대상 원소의 개수 =len(phone_book)-1
    # zip복잡도 O(n) zip대상 원소의 개수. 가장 짧은 리스트의 길이*리스트의 개수. 2*len(phone_book)-1
    # for else구문
    for i in range(len(phone_book)):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    else:
        return True


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

solution_regexp(["119", "97674233", "1195524421"])
solution_list_slicing(["119", "97674233", "1195524421"])
solution_sort(["119", "97674233", "1195524421"])

solution_regexp(["123", "456", "789"])
solution_list_slicing(["123", "456", "789"])
solution_sort(["123", "456", "789"])

solution_regexp(["12", "123", "1235", "567", "88"])
solution_list_slicing(["12", "123", "1235", "567", "88"])
solution_sort(["12", "123", "1235", "567", "88"])
