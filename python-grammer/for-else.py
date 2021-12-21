import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    sqrt = math.sqrt(multiplied)
    # 4.0 == 4  True int converted to float
    print(f'sqrt : {sqrt} int(sqrt) : {int(sqrt)}  결과 : {sqrt == int(sqrt)}')
    if sqrt == int(sqrt):
        print('found')
        break
# for 문을 break없이 다 수행되었다면
# else 없이 출력하면 찾은 경우에도 not found 출력됨.
else:
    print('not found')
