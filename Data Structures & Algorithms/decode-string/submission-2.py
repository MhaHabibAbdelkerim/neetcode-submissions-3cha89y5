class Solution:
    def decodeString(self, s: str) -> str:
        SStack = []
        NumStack = []
        Number = 0
        Current = ""

        for i in range(len(s)):
            if s[i].isdigit():
                Number = Number * 10 + int(s[i])
            elif s[i] == "[":
                SStack.append(Current)
                NumStack.append(Number)
                Current = ""
                Number = 0
            elif s[i] == "]":
                TEMP = Current
                Count = NumStack.pop()
                Current = SStack.pop()
                Current += TEMP * Count
            else:
                Current += s[i]

        return Current