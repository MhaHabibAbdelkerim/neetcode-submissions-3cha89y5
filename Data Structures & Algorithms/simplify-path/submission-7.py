class Solution:
    def simplifyPath(self, path: str) -> str:
        Current_path = ""
        stack = []

        for character in path + "/":
            if character == "/":
                if Current_path == "..":
                    if stack: stack.pop()
                elif Current_path != "." and Current_path != "":
                    stack.append(Current_path)
                Current_path = ""
            else:
                Current_path += character

        return "/" + "/".join(stack)