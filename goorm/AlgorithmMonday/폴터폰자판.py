keyboard = {
    "1": ["1", ".", ",", "?", "!"],
    "2": ["2", "A", "B", "C"],
    "3": ["3", "D", "E", "F"],
    "4": ["4", "G", "H", "I"],
    "5": ["5", "J", "K", "L"],
    "6": ["6", "M", "N", "O"],
    "7": ["7", "P", "Q", "R", "S"],
    "8": ["8", "T", "U", "V"],
    "9": ["9", "W", "X", "Y", "Z"]
}


def convert_keyboard_input_to_sentence(n: int, s: str) -> str:
    answer = []
    temp_char, temp_index = s[0], 0
    for i in range(1, n):
        x = s[i]
        if x == temp_char:
            temp_index += 1
        else:
            answer.append(keyboard[temp_char][temp_index % len(keyboard[temp_char])])
            temp_char, temp_index = x, 0

    answer.append(keyboard[temp_char][temp_index % len(keyboard[temp_char])])
    return ''.join(answer)


n = int(input())
s = input()

print(convert_keyboard_input_to_sentence(n, s))
