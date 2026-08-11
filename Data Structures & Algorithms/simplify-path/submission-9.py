class Solution:
    def simplifyPath(self, path: str) -> str:
        Stack = []
        Current_Path = ""

        for character in path + "/":
            if character == "/":
                if Current_Path == "..":
                    if Stack: Stack.pop()
                elif Current_Path != "" and Current_Path != ".":
                    Stack.append(Current_Path)
                Current_Path = ""
            else:
                Current_Path += character

        return "/" + "/".join(Stack)