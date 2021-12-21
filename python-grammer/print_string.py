import string

'''알파벳 출력하기 - string 모듈'''
num = int(input().strip())
print(string.ascii_lowercase if 0 else string.ascii_uppercase)
#
string.ascii_letters
string.digits
# list comprehsension 으로 들고 오는 방법?
# list unpacking 괄호, 콤마 없이 출력?
[chr(x) for x in range(65, 100)]
