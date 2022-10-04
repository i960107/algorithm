from itertools import combinations
x= [-12,-10,-11,10,-3,-14,4,-10,9,8,14]
y= [3,6,-7,-8,4,6,14,5,14,-5,10]
print(len(x))
print(len(y))
print(sorted(x))
print(sorted(y))

a = [-29,2,27,17,-13,24,-26,-17,-27,-21,-13,13,21,20]
b = [-4,-29,-13,-8,-7,-27,8,-14,-20,-21,14,23,-23,25]
print(len(a))
print(len(b))
print(sorted(a))
print(sorted(b))


N =4
test = [[0]*N for _ in range(N)]
sources = [[2,3,2],[5,1,10],[6,1,9],[7,3,10]]

for x,y,power in sources:
    for i in range(len(test)):
        for j in range(len((test))):
            curr = power - (abs(x-i)+abs(y-j))

result  =0
l = [2,11,8,2,8,11,2,4,12]
for a,b,c in combinations(l,3):
    curr = abs(a-b) +abs(b-c)+abs(c-a)
    l2 = l[:]
    l2.remove(a)
    l2.remove(b)
    l2.remove(c)
    for e,f,g in combinations(l2,3):
        curr += abs(e-f) +abs(f-g)+abs(g-e)
        result = max(result,curr)
        l3= l2[:]
        l3.remove(e)
        l3.remove(f)
        l3.remove(g)
        q,w,r = l3[0],l3[1],l3[2]
        print(q,w,r)
        curr += abs(q-w) +abs(w-r)+abs(r-q)
        result = max(result,curr)

print(result)




