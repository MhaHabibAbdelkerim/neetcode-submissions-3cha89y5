class Solution:
    def decodeString(self, s: str) -> str:
        String_Stack = []
        Number_Stack = []
        Current_S = ""
        Number = 0

        for i in range(len(s)):
            if s[i].isdigit():
                Number = Number * 10 + int(s[i])
            elif s[i] == "[":
                String_Stack.append(Current_S)
                Number_Stack.append(Number)
                Current_S = ""
                Number = 0
            elif s[i] == "]":
                TEMP = Current_S
                Count = Number_Stack.pop()
                Current_S = String_Stack.pop()
                Current_S += TEMP * Count
            else:
                Current_S += s[i]

        return Current_S
                