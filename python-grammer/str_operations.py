import string


def solution_for(s: str, n: int) -> None:
    ''' 문자열 정렬하기'''
    answer_left_align = ''
    for i in range(n):
        if i < len(s):
            answer_left_align += s[i]
        else:
            answer_left_align += '0'
    print(answer_left_align)

    # center 인덱스 기준 어떻게??
    # answer_center_align = ''
    # for i in range(n):
    #     if i < n - len(s):
    #         answer_center_align += s
    #         break
    #     else:
    #         answer_center_align += '0'
    # print(answer_center_align)

    answer_right_align = ''
    for i in range(n):
        # n-1-len(s)가 기준이 아님. index기준으로 : 마지막인덱스- 문자열길이 +1(처음 끝 둘다 포함)
        if i >= n - len(s):
            answer_right_align += s
            break
        else:
            answer_right_align += '0'
    print(answer_right_align)


def solution_string_method(s: str, n: int) -> None:
    ''' 문자열 정렬하기- string method사용'''
    print(s.ljust(n, '0'))
    print(s.center(n, '0'))
    print(s.rjust(n, '0'))


solution_for('안녕하세요', 10)
solution_string_method('안녕하세요', 10)


def solution_print_string(num: int) -> None:
    '''알파벳 출력하기'''
    for x in range(97, 123):
        if num == 0:
            print(chr(x), end='')
        elif num == 1:
            print(chr(x - 32), end='')
    print()
    # list unpacking 괄호, 콤마 없이 출력?
    # l = [chr(x - 32 * num) for x in range(97, 123)]
    # print(''.join(l))


def solution_print_string_string_method(num: int) -> None:
    '''알파벳 출력하기 - string 모듈'''
    # string.ascii_letters
    # string.digits
    print(string.ascii_lowercase if num == 0 else string.ascii_uppercase)


solution_print_string(0)
solution_print_string_string_method(0)
