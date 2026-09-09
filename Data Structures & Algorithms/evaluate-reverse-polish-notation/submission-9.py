class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = []

        for token in tokens:
            if token == "+":
                Stack.append(Stack.pop() + Stack.pop())
            elif token == "*":
                Stack.append(Stack.pop() * Stack.pop())
            elif token == "-":
                a, b = Stack.pop(), Stack.pop()
                Stack.append(b - a)
            elif token == "/":
                a, b = Stack.pop(), Stack.pop()
                Stack.append(int(b/a))
            else:
                Stack.append(int(token))

        return Stack[0]