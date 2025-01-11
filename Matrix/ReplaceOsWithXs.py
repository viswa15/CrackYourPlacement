class Solution:
    def fill(self,  mat):
        # code here
        m,n = len(mat),len(mat[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(i,j,visited):
            visited[i][j] = True

            if i>0 and not visited[i-1][j] and mat[i-1][j] == "O":
                dfs(i-1,j,visited)
            if i<m-1 and not visited[i+1][j] and mat[i+1][j] == "O":
                dfs(i+1,j,visited)
            if j>0 and not visited[i][j-1] and mat[i][j-1] == "O":
                dfs(i,j-1,visited)
            if j<n-1 and not visited[i][j+1] and mat[i][j+1] == "O":
                dfs(i,j+1,visited)


        for j in range(n):
            if mat[0][j] == "O" and not visited[0][j]:
                dfs(0,j,visited)
            if mat[m-1][j] == "O" and not visited[m-1][j]:
                dfs(m-1,j,visited)

        for i in range(m):
            if mat[i][0] == "O" and not visited[i][0]:
                dfs(i,0,visited)
            if mat[i][n-1] == "O" and not visited[i][n-1]:
                dfs(i,n-1,visited)

        for i in range(1,m):
            for j in range(1,n):
                if not visited[i][j] and mat[i][j] =="O":
                    mat[i][j] = "X"

        return mat
