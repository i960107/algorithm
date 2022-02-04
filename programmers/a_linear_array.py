L = [1, 2, 3]

# 추가
L.append(5)
L.insert(3, 4)
L2 = [6, 7, 8, 9]
L += L2
print(L)

# 삭제
print(L.pop(-1))
del L[-1]
print(L.remove(2))
print(L)

# 탐색
L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(f'index of first 3 {L.index(3)}')
print(f'3 in list counts {L.count(3)}')

# 기타
L.reverse()
L2 = L.copy()
print(L)
print(f'copy of L {L2}')
print(f'is copy of L L? {L2 is L}')


# 정렬된 리스트에 원소 삽입
def insert(L, x):
    isInserted = False

    for i, num in enumerate(L):
        if x <= num:
            L.insert(i, x)
            isInserted = True
            break

        if not isInserted:
            L.append(x)
        return L


# 중간에 원소 삽입
print(insert([1, 3, 4], 2))
# 모든 원소보다 작을때
print(insert([2, 3], 1))
# 모든 원소보다 클때
print(insert([1, 2, 3], 4))
# 빈 배열일때
print(insert([], 1))


# 리스트에서 원소 찾아내기
def find_index(L, x):
    ans = []
    for i, num in enumerate(L):
        if x == num:
            ans.append(i)

    if len(ans) == 0:
        ans = [-1]

    return ans


print()
print('리스트에서 원소 찾아내기')
# 같은 값의 원소가 하나일때
print(find_index([1, 2, 3], 1))
# 같은 값의 원소가 없을때
print(find_index([1, 2, 3], 4))
# 같은 값의 원소가 여러개일때
print(find_index([1, 2, 3, 1, 2, 3], 2))
# 빈 배열일때
print(find_index([], 3))


# 리스트에서 원소 찾아내기 - list comprehension 을 사용한 풀이
def find_index_others_list_comprehension(L, x):
    if x in L:
        return [i for i, num in enumerate(L) if num == x]
    else:
        return [-1]


# 리스트에서 원소 찾아내기 - list slicing 을 사용한 풀이
def find_index_others_list_slicing(L, x):
    n = []
    index = 0
    for i in range(len(L)):
        try:
            number = index
            index = L.index(x)
            n.append(index + number + i)
            L = L[index + 1:]
        except ValueError:
            break

    return n if len(n) != 0 else [-1]


# 정렬
def case_insensitive_sort_string_array(L):
    return sorted(L, key=lambda str: str.casefold)


# 이진 탐색
def binary_search(L, x):
    lower = 0
    upper = len(L) - 1
    middle = (lower + upper) // 2

    answer = -1
    while lower <= upper:
        if x == L[middle]:
            answer = middle
            break
        elif x < L[middle]:
            upper = middle - 1
        else:
            lower = middle + 1
        middle = (lower + upper) // 2

    return answer


print()
print('이진탐색')
print(binary_search([1, 2, 3, 4, 5], 1))
print(binary_search([1, 2, 3, 4, 5], 5))
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5], 6))
print(binary_search([], 6))
