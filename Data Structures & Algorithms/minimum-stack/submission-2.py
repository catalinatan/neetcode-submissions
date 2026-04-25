class MinStack:

    def __init__(self):
        self.minstack = []
        self.min_val_stack = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        if len(self.minstack) == 1:
            self.min_val_stack.append(val)
        elif len(self.minstack) > 1:
            min_val = min(self.min_val_stack[-1], val)
            self.min_val_stack.append(min_val)
        else:
            pass

    def pop(self) -> None:
        self.minstack.pop()
        self.min_val_stack.pop()

    def top(self) -> int:
        top_val = self.minstack[-1] # Remember stack is LIFO
        return top_val 
        
    def getMin(self) -> int:
        # binary search requires sorting since its not ascending/descending
        # might be tricky to implement 
        return self.min_val_stack[-1]

