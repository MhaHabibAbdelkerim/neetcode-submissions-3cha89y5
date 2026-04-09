class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        S = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in S:
                if stack and stack[-1] == S[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False