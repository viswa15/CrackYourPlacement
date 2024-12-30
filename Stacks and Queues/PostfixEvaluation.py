#User function Template for python3

class Solution:

    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, s):
        #code here
        stk = []
        a = ["+","-","*","/"]
        for char in s:
            if char in a:
                val2 = stk.pop()
                val1 = stk.pop()
                if char == "+":
                    stk.append(val1+val2)
                elif char == "-":
                    stk.append(val1-val2)
                elif char == "*":
                    stk.append(val1*val2)
                elif char == "/":
                    stk.append(val1//val2)
            else:
                stk.append(int(char))
        return stk[-1]