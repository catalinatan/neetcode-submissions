class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for char in tokens:
            if char in operators:
                last_val = int(stack.pop())
                sec_last_val = int(stack.pop())

                if char == "+":
                    stack.append(sec_last_val + last_val)

                if char == "-":
                    stack.append(sec_last_val - last_val)

                if char == "*":
                    stack.append(sec_last_val * last_val)

                if char == "/":
                    stack.append(sec_last_val / last_val)
            else:
                stack.append(int(char))

        return int(stack[-1])