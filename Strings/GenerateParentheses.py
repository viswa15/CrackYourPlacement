class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def recursion(openN,closeN):
            #base case
            if openN == closeN == n:
                res.append("".join(s))
                return



            if openN<n :
                s.append("(")
                recursion(openN+1,closeN)
                s.pop()

            if closeN<openN:
                s.append(")")
                recursion(openN,closeN+1)
                s.pop()


        recursion(0,0)
        return res