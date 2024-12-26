class Solution:
    def numIslands(self, grid):
        # code here
        res = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def is_safe(i,j,r,c,visited,grid):

            return (i>=0 and i<r and j>=0 and j<c and not visited[i][j] and grid[i][j]==1)

        def dfs(i,j,visited,M):
            r,c = len(M),len(M[0])
            visited[i][j] = True

            row = [-1,-1,-1,0,1,1,1,0]
            col = [-1,0,1,1,1,0,-1,-1]

            for k in range(len(row)):
                newR = i + row[k]
                newC = j + col[k]
                if is_safe(newR,newC,r,c,visited,M):
                    dfs(newR,newC,visited,grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    res += 1
                    dfs(i,j,visited,grid)
        return res
