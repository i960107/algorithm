from typing import List, Tuple
from collections import Counter


def ArrayChallenge(strArr: str) -> bool:
    converted = convertToListOfTuple(strArr)
    # child: parent

    # if parent is more than one, not a valid binary tree
    children = set([child for child, parent in converted])
    if len(children) != len(converted):
        return False

    # if parent has more than two children, not a valid binary tree

    return True


def convertToListOfTuple(strArr: str) -> List[Tuple[int]]:
    converted = []
    for element in strArr[1: -1].split(", "):
        l = []
        temp = ""
        for index in range(2, len(element) - 1):
            if element[index] in (",", ")"):
                l.append(int(temp))
                temp = ""
                continue
            temp += element[index]
        converted.append(tuple(l))
    return converted


print(ArrayChallenge(input()))
