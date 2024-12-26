class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d,n = {},len(nums)
        # for i in nums:
        #     d[i] = 1 + d.get(i,0)
        # for i in d:
        #     if d[i] > n//2:
        #         return i
        res,c = None,0
        for i in nums:
            if c==0:
                res=i
            c+= (1 if res==i else -1)
        return res