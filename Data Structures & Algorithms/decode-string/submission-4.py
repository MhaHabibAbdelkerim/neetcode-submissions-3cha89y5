class Solution:
    def decodeString(self, s: str) -> str:
        Number = 0
        Current = ""
        String_Stack = []
        Number_Stack = []

        for i in range(len(s)):
            if s[i].isdigit():
                Number = Number * 10 + int(s[i])
            elif s[i] == "[":
                String_Stack.append(Current)
                Number_Stack.append(Number)
                Number = 0
                Current = ""
            elif s[i] == "]":
                TEMP = Current
                COUNT = Number_Stack.pop()
                Current = String_Stack.pop()
                Current += TEMP * COUNT
            else:
                Current += s[i]

        return Current
