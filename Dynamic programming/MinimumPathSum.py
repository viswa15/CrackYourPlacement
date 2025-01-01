class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        #tabulation
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]

        # #first row
        # for j in range(1,n):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]

        # #first col
        # for i in range(1,m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]

        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])

        # return dp[m-1][n-1]

        #space optimization
        prev = [0] * n
        cur = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cur[j] = grid[i][j]
                else:
                    right,down = float("inf"),float("inf")
                    if i > 0:
                        down = prev[j]
                    if j > 0:
                        right = cur[j-1]
                    cur[j] = grid[i][j] + min(right,down)
            prev = cur
        return prev[n-1]


