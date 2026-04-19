class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_match_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if stack and close_match_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0