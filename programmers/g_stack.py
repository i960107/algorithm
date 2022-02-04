import f_doubly_linked_list


class ArrayStack:
    '''배열로 구현한 스택'''

    def __init__(self):
        self.data = []

    def size(self) -> int:
        return len(self.data)

    def is_empty(self) -> bool:
        return self.size() == 0

    def pop(self):
        # return self.data[-1] 아님. 단순 원소 값 반환
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]


class LinkedListStack:
    '''양방향 연결리스트로 구현한 스택'''

    def __init__(self):
        # stack 최대 원소 개수 정해져있지 않음. 따라서 isFull()은 없음.
        self.data = f_doubly_linked_list.DoublyLinkedList()

    def size(self):
        return self.data.get_length()

    def is_empty(self):
        return self.data.get_length() == 0

    def pop(self):
        return self.data.pop_at(self.size())

    def push(self, item):
        new_node = f_doubly_linked_list.Node(item)
        self.data.insert_at(self.size() + 1, new_node)

    def peek(self):
        # 스택의 데이터에서 가장 마지막 노드 들고와서 그 노드의 데이터 반환
        return self.data.get_at(self.size()).data


def splitTokens(exprStr):
    pass


def check_bracket(expr: str) -> bool:
    '''수식의 괄호 검사'''
    d = {
        # value로 key 들고 올 수 없기 때문에 처음부터 반대로 지정해주기
        # 닫는 괄호의 짝을 찾아야 함 -> 닫는 괄호가 key가 됨
        ")": "(",
        "}": "}",
        "]": "[",
    }

    s = ArrayStack()

    for x in expr:
        # if x in d.values():
        # 위 방식은 d를 선형탐색해야 하기때문에 문자열로 지정해주는게 더 최적화된 방법
        if x in '({[':
            s.push(x)
        elif x in d.keys():
            # if x in d: 같은 의미임
            # stack이 비었는데 닫는 괄호 있을때
            if s.is_empty():
                return False
            elif not s.pop() == d.get(x):
                return False

    #한 줄로 줄일 수 있음
    # if not s.is_empty():
    #     return False
    #
    # return True
    return s.is_empty()


print(check_bracket('[(1+2)*3]'))
print(check_bracket('{(1+2}*3)'))


def infixToPostfix(tokenList):
    '''중위표현식을 후위표현식으로 변환'''
    pass


def postfixEval(tokenList):
    '''후위표현수식 계산'''
    pass
