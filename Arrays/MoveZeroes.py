class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        if 0 not in nums:
            return nums
        while j<len(nums):
            if nums[j] != 0 and nums[i]==0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            elif nums[i] !=0:
                i+=1
            j+=1
        return nums

