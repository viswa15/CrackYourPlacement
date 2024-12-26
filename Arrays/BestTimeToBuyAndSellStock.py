class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        ans = 0
        for i in range(len(prices)):
            min_val = min(min_val,prices[i])
            ans = max(ans,prices[i]-min_val)
        return ans