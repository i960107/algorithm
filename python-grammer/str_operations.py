import collections
import string
from collections import deque
from collections import Counter
from collections import defaultdict
from typing import Deque
from typing import List


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


def is_palindrome_arr(s: str) -> bool:
    '''유효한 팰린드롬: 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다'''
    '''배열을 이용한 팰린드론 판단'''
    filtered = ""
    for char in s.lower():
        # if not (ord(char) in range(ord('a'), ord('z') + 1) or ord(char) in range(ord('0'), ord('9'))):
        if not (char in string.ascii_lowercase or char in string.digits):
            # return True if char is alpha-numeric
            # if not char.isalnum():
            continue
        else:
            filtered += char

    reverse = filtered[::-1]

    # O(n)
    return reverse == filtered


def is_palindrome_deque(s: str) -> bool:
    '''데크를 이용한 팰린드론 판단'''
    strs: Deque = deque()
    s = deque(s)

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        # popleft() :O(1)
        # 리스트로 풀이할때는 O(N)이지만 자료형 deque으로 정의하면 O(N)
        # 리스트 슬라이싱이 내부적으로 더 빠른 방법. 배열 포인터를 사용하기때문
        if strs.popleft() != strs.pop():
            return False

    return True


print(is_palindrome_arr("A man, a plan, a canal: Panama"))


def reverse_string(l: list) -> list:
    # 만약 공간 복잡도 제한이 있는 플랫폼이라면
    # l[:] = l[::-1]
    return l[::-1]


def reverse_string_pointer(l: list) -> list:
    left, right = 0, len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

    return l


d = collections.Counter()
d.most_common(1)

print(reverse_string_pointer(["h", "e", "l", "l", "o"]))


def reorder_log_files(logs: list) -> list:
    letters, digits = [], []
    # 문자로 구성된 로그가 숫자 로그보다 앞에, 숫자로그는 입력순
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 두번째 문자를 기준으로 정렬하되, 같을 경우 식별자 순
    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return letters + digits


print(reorder_log_files(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))

print(sorted(['2 A', '1 B', '4 C', '1 A'], key=lambda x: (x.split()[1], x.split()[0])))


def most_common_word(paragraph: str, banned: list) -> str:
    counter = Counter(part for part in paragraph.lower().replace(",", "").replace(".", "").split())

    for s in banned:
        if counter[s]:
            counter[s] = 0

    return counter.most_common()[0][0]


print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))


def longest_palindrome_substring(s: str) -> str:
    '''가장 긴 팰린드롬 부분 문자열을 출력하라'''

    # 투 포인터가 중앙을 중심으로 확장. 슬라이딩 윈도우처럼 이동
    # 2칸, 3칸으로 구성된 투 포인터가 슬라이딩 윈도우처럼 계속 앞으로 전진해간다.
    # 홀수 3칸과 짝수 2칸의 2개 포인터가 계속 우측으로 이동하다.
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


def group_anagrams(strs: List[str]) -> List[List[str]]:
    '''그룹 애너그램'''
    groups = defaultdict(list)
    for s in strs:
        groups[''.join(sorted(s))].append(s)
    return [value for _, value in groups.items()]


print(group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(strs=[""]))
print(group_anagrams(strs=["a"]))


def longest_palindrome(s: str) -> str:
    # 최적화. 예외처리. 해당하지 않을때 빠르게 return
    if len(s) < 2 or s == s[::-1]:
        return s

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right -= 1
        # left, right 포함하지 않는 범위가 팰린드롬에 해당
        return s[left + 1:right]

    result = ''
    # 가장 마지막 두개 글자가 팰린드롬인 경우 확인
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


# print(longest_palindrome("babad"))
print(longest_palindrome("bb"))
print(longest_palindrome("ab"))
