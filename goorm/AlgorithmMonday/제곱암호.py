def solution(n: int, s: str) -> str:
    def _decrypt(char: str, num: int) -> str:
        count = num ** 2
        return chr((ord(char) - ord('a') + count) % 26 + ord('a'))

    decrypted = []
    for char_index in range(0, n, 2):
        char = s[char_index]
        num = int(s[char_index + 1])
        decrypted.append(_decrypt(char, num))
    return ''.join(decrypted)


n = int(input())
s = input()
print(solution(n, s))
