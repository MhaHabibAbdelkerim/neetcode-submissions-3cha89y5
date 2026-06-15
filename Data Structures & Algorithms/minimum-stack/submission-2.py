class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        return self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        self.Min = []
        for i in range(len(self.MinStack)):
            self.Min.append(self.MinStack[i])
        s = sorted(self.Min)
        return s[0]
    