def solution_divide_modulus(num1: int, num2: int) -> tuple:
    '''몫과 나머지 구하기'''
    quotient = num1 // num2
    modulus = num1 % num2
    return quotient, modulus


def solution_divide_modulus_divmod(num1: int, num2: int) -> tuple:
    '''몫과 나머지 구하기 - divmod(활용)'''
    # divmode는 tuple을 반환, * unpacking 하는 문법
    # 작은 숫자를 다룰때는 //, %을 하는게 좋음. 큰 숫자에서는 divmode가 더 효율적
    return divmod(num1, num2)


# input()으로 받은 값은 str으로 인식됨. map으로 각각을 int형으로 변환해준 뒤 unpacking
# input()값 여러개 받고 싶을때? 한 줄 안에 공백으로 나눠서 입력하게 하든가, 여러번 물어보기(반복문 사용)
a, b = map(int, input().strip().split(' '))
print(solution_divide_modulus(a, b))
print(solution_divide_modulus_divmod(a, b))


# decimal : 10진수 혹은 소수(float)을 의미
def solution_nbase_to_decimal_conversion(num: int, base: int) -> int:
    '''n진법으로 표기된 string을 10진법 숫자로 변환하기'''
    # 리스트 뒤집기 l.reverse() 혹은 l[::-1]
    l = list(map(int, str(num)))
    answer = 0
    # 리스트를 뒤집는 것보보다 pow를 조정해주는게 더 최적화된 방법
    for i in range(len(l)):
        # base **(len(l)-1-i)도 가능
        answer += l[i] * pow(base, (len(l) - 1 - i))
    return answer


def solution_nbase_to_decimal_conversion_base(num: int, base: int) -> int:
    '''n진법으로 표기된 string을 10진법 숫자로 변환하기 - int()이용'''
    # int() 에 argument 2개일때는 str 여야함
    # num 이 base 진법으로 표현된 올바른 값이 아니라면 Value Error 발생
    return int(str(num), base)


num, base = map(int, input().strip().split(' '))
print(solution_nbase_to_decimal_conversion(num, base))
print(solution_nbase_to_decimal_conversion_base(num, base))

