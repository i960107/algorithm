# num1과 num2의 최소 공배수를 반환
def get_lcm(num1: int, num2: int) -> int:
    gcd = get_gcd(num1, num2)
    return num1 * num2 // gcd


# a와 b의 최대 공약수를 반환
def get_gcd(a: int, b: int) -> int:
    # b가 a의 약수가 아니라면
    while a % b:
        # 나머지를 계산한다 이후  b와 b%c에 대해 이 과정을 반복한다
        a, b = b, a % b
    # b가 a의 약수라면 b가 a의 최대공약수이다
    return b


T = int(input())

for t in range(T):
    print("Case #%d:" % (t + 1))

    num1, num2 = map(int, input().split())
    gcd = get_gcd(num1, num2)
    lcm = get_lcm(num1, num2)

    print(gcd, lcm)
