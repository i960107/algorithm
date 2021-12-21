import copy

'''원본을 유지한채, 정렬된 리스트 구하기'''

list1 = [3, 2, 1]

# 방법1 - list comprehension & sort
# O(N)
# sort(revers= True)보다 reverse()가 O(N)으로 복잡도 더 낮음
list2 = [i for i in list1]
list2.reverse()

# 방법2 - deepcopy & sort
# O(N)
list2 = copy.deepcopy(list1)
list2.reverse()

# 방법3 - sorted() 반복문이나 deepcopy 함수 없이 새로운 정렬된 리스트 만들기
# O(NlogN)
# 단지 reverse의 경우, copy() 후 reverse함수를 이용하는게 나을수 있음.
# sort()가 필요할 경우 방법 1,2,3 모두 O(NlogN) 복잡도를 가지지만, 방법3)은 list를 카피하지 않아 더욱 최적화된 방법임.
list2 = sorted(list1, reverse=True)
