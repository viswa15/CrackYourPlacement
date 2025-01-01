class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #memorization
        dp = {}

        def dfs(i,m,n):
            if i == len(strs):
                return 0
            if (i,m,n) in dp:
                return dp[(i,m,n)]

            mCnt,nCnt = strs[i].count("0"),strs[i].count("1")
            dp[(i,m,n)] = dfs(i+1,m,n)
            if mCnt<=m and nCnt<=n:
                dp[(i,m,n)] = max(dp[(i,m,n)],1+dfs(i+1,m-mCnt,n-nCnt))
            return dp[(i,m,n)]
        return dfs(0,m,n)

        #dynamic programming
        # dp = {}

        # for i in range(len(strs)):
        #     mCnt,nCnt = strs[i].count("0"),strs[i].count("1")
        #     for M in range(0,m+1):
        #         for N in range(0,n+1):
        #             if mCnt <= M and nCnt <= N:
        #                 dp[(i,M,N)] = max(dp[(i-1,M,N)],1+dp[(i-1,M-mCnt,N-nCnt)])
        #             else:
        #                 dp[(i,M,N)] = dp[(i-1,M,N)]
        # return dp[(len(strs)-1,m,n)]