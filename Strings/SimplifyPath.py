class Solution:
    def simplifyPath(self, path: str) -> str:
        # symbols = [".","..","/"]
        res = ""
        stk = []
        i = 0
        while i < len(path):
            print(stk)
            if path[i] == "/":
                while i < len(path) and path[i] == "/":
                    i += 1
                stk.append("/")
            elif path[i] == ".":
                c = ""
                while i<len(path) and (path[i] == "." or path[i] != "/"):
                    c += path[i]
                    i += 1
                if len(c) < 3 and c[-1]==".":
                    for _ in range(2*(len(c))-1):
                        if stk:
                            stk.pop()
                else:
                    stk.append(c)
            else:
                c = ""
                while i<len(path) and  (path[i] != "/"):
                    c += path[i]
                    i += 1
                stk.append(c)
        print(stk)

        if not stk or stk==["/"]:
            return "/"

        if stk[-1] == "/":
            if stk[0] != "/":
                res += "/"
            for i in range(len(stk)-1):
                res += stk[i]
        else:
            if stk[0] != "/":
                res += "/"
            for i in range(len(stk)):
                res += stk[i]
        return res



