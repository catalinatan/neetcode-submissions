class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "{":"}", "[": "]"}
        for char in s: 
            if char in mapping.keys():
                stack.append(mapping[char])
            
            if char in mapping.values():
                if not stack:
                    return False
                else:
                    if char != stack[-1]:
                        return False
                    else:
                        stack.pop()
            # if stack and char in mapping.values() and char == stack[-1]:
            #     stack.pop()
            # elif char in mapping.values() and not stack:
            #     return False
        return False if stack else True