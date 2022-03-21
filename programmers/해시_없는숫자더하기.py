def solution(numbers: list) -> int:
    # list로 in 검사하면 O(n^2)복잡도 가짐

    # list to dictionary
    dic = {i: 0 for i in range(10)}
    # dic = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for num in numbers:
        dic[num] = dic.get(num) + 1

    return sum(num for num, cnt in dic.items() if cnt == 0)


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))
