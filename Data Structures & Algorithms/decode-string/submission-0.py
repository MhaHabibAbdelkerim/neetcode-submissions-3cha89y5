class Solution:
    def decodeString(self, s: str) -> str:
        String_Stack = []
        Count_Stack = []
        Current = ""
        Number = ""

        for character in s:
            if character.isdigit():
                Number += character
            elif character == "[":
                String_Stack.append(Current)
                Count_Stack.append(int(Number))
                Current = ""
                Number = ""
            elif character == "]":
                Temp = Current
                Current = String_Stack.pop()
                Count = Count_Stack.pop()
                Current += Temp * Count

            else: Current += character

        return Current