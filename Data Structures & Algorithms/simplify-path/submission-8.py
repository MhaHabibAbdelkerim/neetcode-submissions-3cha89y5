class Solution:
    def simplifyPath(self, path: str) -> str:
        Stack = []
        current_path = ""

        for character in path + "/":
            if character == "/":
                if current_path == "..":
                    if Stack: Stack.pop()
                elif current_path != "." and current_path != "":
                    Stack.append(current_path)
                current_path = ""
                
            else:
                current_path += character

        return "/" + "/".join(Stack)
