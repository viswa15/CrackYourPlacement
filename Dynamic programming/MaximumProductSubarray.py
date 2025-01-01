class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bruteforce
        # m_s = float("-inf")
        # for i in range(len(nums)):
        #     r = nums[i]
        #     m_s = max(r,m_s)
        #     for j in range(i+1,len(nums)):
        #         r*=nums[j]
        #         m_s = max(r,m_s)
        # return m_s

        res = max(nums)
        curMax,curMin = 1,1
        for n in nums:
            tmp = n * curMax
            curMax = max(n,tmp,curMin*n)
            curMin = min(n,tmp,curMin*n)
            res = max(curMax,res)
        return res