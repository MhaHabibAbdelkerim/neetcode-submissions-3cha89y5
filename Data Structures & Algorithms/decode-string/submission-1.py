class Solution:
    def decodeString(self, s: str) -> str:
        String_Stack = []
        Count_Stack = []
        Current = ""
        Number = 0

        for character in s:
            if character.isdigit():
                Number = Number * 10 + int(character)
            elif character == "[":
                String_Stack.append(Current)
                Count_Stack.append(Number)
                Current = ""
                Number = 0
            elif character == "]":
                TEMP = Current
                Count = Count_Stack.pop()
                Current = String_Stack.pop()
                Current += TEMP * Count
            else:
                Current += character

        return Current
