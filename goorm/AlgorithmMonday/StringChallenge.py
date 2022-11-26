from typing import List, Union


def StringChallenge(strParam: str) -> str:
    converted = convert_string_to_int_and_operation(strParam)

    interim_result = converted[0]

    for op_index in range(1, len(converted), 2):
        op = converted[op_index]
        num = converted[op_index + 1]
        interim_result = evaluate(interim_result, num, op)

    return convert_int_to_string(interim_result)



def convert_int_to_string(num: int) -> str:
    d = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }

    converted = ""
    if num < 0:
        converted = "negative"

    target = str(abs(num))

    for x in target:
        converted += d[x]

    return converted


def evaluate(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    return a - b


def convert_string_to_int_and_operation(strParam: str) -> List[Union[str, int]]:
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
        "plus": "+",
        "minus": "-",
    }

    i = 0
    temp = ""

    converted = []
    while i < len(strParam):
        if not temp:
            temp += ''.join((strParam[i:i + 3]))
            i += 3

        else:
            temp += ''.join((strParam[i:i + 1]))
            i += 1

        if temp not in d:
            continue

        if d[temp] in ("+", "-"):
            converted.append(d[temp])
        else:
            if converted and converted[-1] not in ("+", "-"):
                converted[-1] = converted[-1] * 10 + d[temp]
            else:
                converted.append(d[temp])

        temp = ""
    return converted


print(StringChallenge(input()))
