class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current_directory = ""

        for character in path + "/":
            if character == "/":
                if current_directory == "..":
                    if stack: stack.pop()
                elif current_directory != "" and current_directory != ".":
                    stack.append(current_directory)
                current_directory = ""
            else:
                current_directory += character
        return "/" + "/".join(stack)