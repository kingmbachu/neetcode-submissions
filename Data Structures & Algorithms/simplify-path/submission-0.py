class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        parts = path.split("/")

        for directory in parts:
            if directory == "..":
                if stack:
                    stack.pop()

            elif directory != "" and directory != ".":
                stack.append(directory)
        
        return "/" + "/".join(stack)