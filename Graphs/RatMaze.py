class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        res = []
        n = len(mat)


        def dfs(i,j,path):
            if i < 0 or j < 0 or i >= n or j >= n or mat[i][j] == 0:
                return

            if i == n-1 and j == n-1:
                res.append("".join(path))
                return

            mat[i][j] = 0

            if i>0:
                dfs(i-1,j,path+["U"])
            if i<n-1:
                dfs(i+1,j,path+["D"])
            if j>0:
                dfs(i,j-1,path+["L"])
            if j<n-1:
                dfs(i,j+1,path+["R"])

            mat[i][j] = 1


        if mat[0][0] == 1:
            dfs(0,0,[])
        return sorted(res)