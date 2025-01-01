class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * (n)
        cur = [1] * n

        for i in range(m):
            for j in range(1,n):
                if i==0:
                    cur[j] = 1
                else:
                    cur[j] = cur[j-1] + prev[j]
            prev = cur
        return prev[n-1]