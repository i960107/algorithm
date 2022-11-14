def solution(s: str, operation: str, token: str) -> str:
    answer = None
    if operation == "E":
        answer = encrypt(s, token)
    else:
        answer = decrypt(s, token)
    return answer


def encrypt(s: str, token: str) -> str:
    encrypted = []
    for index, c in enumerate(s):
        shift = ord(token[index % len(token)])
        if c.islower():
            encrypted.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
        elif c.isupper():
            encrypted.append(chr((ord(c) - ord("A") + shift) % 26 + ord("A")))
        # elif c.isdigit():
        #     encrypted.append(chr((ord(c) - ord("0") + shift) % 10 + ord("0")))
        else:
            encrypted.append(c)
    return "".join(encrypted)


def decrypt(s: str, token: str) -> str:
    decrypted = []
    for index, c in enumerate(s):
        shift = ord(token[index % len(token)])
        if c.islower():
            decrypted.append(chr((ord(c) - ord("a") - shift) % 26 + ord("a")))
        elif c.isupper():
            decrypted.append(chr((ord(c) - ord("A") - shift) % 26 + ord("A")))
        # elif c.isdigit():
        #     decrypted.append(chr((ord(c) - ord("0") - shift) % 10 + ord("0")))
        else:
            decrypted.append(c)
    return "".join(decrypted)


t = int(input())
for _ in range(t):
    s = input()
    operation, token = input().split()
    print(solution(s, operation, token))
