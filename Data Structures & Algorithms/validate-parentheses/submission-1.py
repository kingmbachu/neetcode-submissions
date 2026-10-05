class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if stack[-1] != closing_to_open[bracket]:
                    return False
                stack.pop()
        return len(stack) == 0