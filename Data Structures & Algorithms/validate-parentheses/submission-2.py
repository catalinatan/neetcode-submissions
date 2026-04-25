class Solution:
    def isValid(self, s: str) -> bool:
        par_pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s: 
            if char in par_pairs: 
                if stack and stack[-1] == par_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False