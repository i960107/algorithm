import bisect as bs


# bisect : divide into two parts

def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError
    if hi is None or hi > len(a):
        #인덱스가 아님... len(a)-1을 했을때와 크게 차이가 없어서 그런가?
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        # 왜 a[mid] == x 를 비교하지 않나?
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


mylist = [1, 2, 3, 7, 9, 11, 33]
# 3의 index를 return : 2
print(bisect(mylist, 3))
# insertion point를 return : 2+1 =3. bisect_right와 같음
print(bs.bisect(mylist, 3))
# 기존 항목의 앞 위치를 반환
print(bs.bisect_left(mylist, 3))
# 기존 항목의 뒤 위치를 반환
print(bs.bisect_right(mylist, 3))
