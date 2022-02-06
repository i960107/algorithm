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

    # 한 줄로 줄일 수 있음
    # if not s.is_empty():
    #     return False
    #
    # return True
    return s.is_empty()


print(check_bracket('[(1+2)*3]'))
print(check_bracket('{(1+2}*3)'))

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    # stack에 들어갈 문자들은 다 우선순위 가져야 비교 가능. 닫는 괄호는 들어가지 않음
    '(': 1
}


def infixStrToPostfix(exp: str) -> str:
    '''중위표현식 문자열을 후위 표현식으로 바꾸기'''
    opStack = ArrayStack()
    answer = ''
    for x in exp:
        if x in prec:  # 여는 괄호 및 연산자
            if x in '+-*/' and not opStack.is_empty():
                # 우선순위 맞춰서 넣어주기
                precX = prec.get(x)
                # 우선순위 같은 연산자 stack에 있을때 꺼내기
                while not opStack.is_empty() and prec.get(opStack.peek()) >= precX:
                    answer += opStack.pop()
            opStack.push(x)
        elif x == ')':  # 닫는 괄호
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        else:  # 영문자
            answer += x
    while not opStack.is_empty():
        answer += opStack.pop()
    return answer


print(infixStrToPostfix('A+B-C'))
print(infixStrToPostfix('(A+B)*C'))
print(infixStrToPostfix('A+B*C'))


def splitTokens(exprStr: str) -> list:
    '''문자열로 된 중위표현식을 쪼개고 숫자는 실제 정수데이터로 바꾸어서 list로 만들기'''
    # 연산자는 그대로 문자열. 정수는 2자리수 이상일수도
    tokenList = []
    valProcessing = False
    val = 0
    for x in exprStr:
        if x in '+-/*()':
            if valProcessing:
                tokenList.append(val)
                val = 0
                valProcessing = False
            tokenList.append(x)
        else:
            # 어떻게 정수가 끝난는지 판별할 것인가?
            val = val * 10 + int(x)
            valProcessing = True
    if valProcessing:
        tokenList.append(val)
    return tokenList


def infixListToPostfix(tokenList: list) -> list:
    '''중위 포현식을 담은 리스트를 후위표현식으로 바꾸기'''
    opStack = ArrayStack()
    answer = []
    for x in tokenList:
        if x in prec:  # 여는 괄호 및 연산자
            if x in '+-*/' and not opStack.is_empty():
                # 우선순위 맞춰서 넣어주기
                precX = prec.get(x)
                # 우선순위 같은 연산자 stack에 있을때 꺼내기
                while not opStack.is_empty() and prec.get(opStack.peek()) >= precX:
                    answer += opStack.pop()
            opStack.push(x)
        elif x == ')':  # 닫는 괄호
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        else:  # 숫자
            # answer += x int object is not iterable 에러 발생
            answer.append(x)
    while not opStack.is_empty():
        answer += opStack.pop()
    return answer


def postfixEval(tokenList: list) -> int:
    '''후위표현수식 계산'''
    numStack = ArrayStack()
    operators = ['+', '-', "*", "/"]

    for x in tokenList:
        # if x in '+-/*':
        # in <string> requires string as left operand, not int
        # int 와 str을 비교하려고 해서 생기는 문제
        # 왜 if token in operators 는 괜찮지?
        if x in operators:
            num2 = numStack.pop()
            num1 = numStack.pop()
            if x == '+':
                numStack.push(num1 + num2)
            elif x == '-':
                numStack.push(num1 - num2)
            elif x == '*':
                numStack.push(num1 * num2)
            else:
                # int / int -> float형 됨.
                numStack.push(num1 / num2)
        else:
            numStack.push(x)

    return numStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixListToPostfix(tokens)
    val = postfixEval(postfix)
    print(f'{expr} -> {tokens} -> {postfix}  결과 : {val} ')
    return val


solution("5/3")
solution("(1+2)*(3+4)")
solution("7*(9-(3+2))")
solution("7*(9-(30+2))")
