class TwoStacks:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Function to push an integer into stack 1
    def push1(self, x):
        self.stk1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.stk2.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if len(self.stk1) > 0:
            return self.stk1.pop()
        return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if len(self.stk2) > 0:
            return self.stk2.pop()
        return -1