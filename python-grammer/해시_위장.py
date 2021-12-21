import collections


# def solution(clothes):
#     d = {}
#     for name, type in clothes:
#         print(name, type)
#         type_d = d.get(type, 0)
#         if type
#             print(f'type_d:{type_d}')
#         type_d[name] = type_d.get(name, 0) + 1
#
#     print(d)


# solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])


def solution_others(clothes):
    array = {}
    for name, type in clothes:
        if type in array:
            array[type] += 1
        else:
            array[type] = 1
    cnt = 1
    for i in array.values():
        cnt *= (i + 1)
    return cnt - 1
