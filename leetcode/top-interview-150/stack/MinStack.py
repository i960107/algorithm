class MinStack:
    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self, val: int):
        self.stack.append(val)
        minValue = self.minValues[-1] if self.minValues and self.minValues[-1] < val else val
        self.minValues.append(minValue)

    def pop(self):
        self.minValues.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]


# 하나의 stack만 사용.
class MinStack2:
    EMPTY = 2 ** 31

    def __init__(self):
        self.stack = []
        self.min = self.EMPTY

    def push(self, val: int):
        if not self.stack:
            self.stack.append(val)
            self.min = val
        elif self.min <= val:
            self.stack.append(val)
        else:
            # 항상 val보다 항상 작고 이전 min값을 기억한다.
            # 이후에는 self.min보다 작은 값이 stack에 저장됨 ->불가능.
            # 최소값이라고 판단할 수 있음
            # 이후에 중복된 값이 들어오더라도 val 상태로 저장되어 val
            self.stack.append(2 * val - self.min)
            self.min = val

    def pop(self):
        x = self.stack.pop()
        if x < self.min:
            self.min = 2 * self.min - x

    def top(self) -> int:
        if self.stack[-1] < self.min:
            return self.min
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min


ops = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
nums = [[], [-2], [0], [-3], [], [], [], []]

obj = None

result = []
for op, num in zip(ops, nums):
    if op == "MinStack":
        obj = MinStack2()
        result.append("None")
    elif op == "push":
        result.append(obj.push(num[0]))
    elif op == "pop":
        result.append(obj.pop())
    elif op == "getMin":
        result.append(obj.getMin())
    else:
        result.append(obj.top())
print(result)
