class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        prev_1,prev_2 = 1,1
        for i in range(2,n+1):
            cur = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = cur
        return cur