class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            elif len(stack) >= 2: 
                right = stack.pop()
                left = stack.pop() 
                
                if char == "+":
                    stack.append(left + right)
                
                if char == "-":
                    stack.append(left - right)
                
                if char == "*":
                    stack.append(left * right)
                
                if char == "/":
                    stack.append(int(left / right))

        return stack[-1]



