class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == '(' or i=="[" or i=="{":
                stk.append(i)
            elif (i==")" or i=="}" or i=="]") and not stk:
                return False
            elif (i==")" and stk[-1]=="(") or (i=="}" and stk[-1]=="{") or (i=="]" and stk[-1]=="["):
                stk.pop()
            else:
                stk.append(i)
        if stk:
            return False
        return True