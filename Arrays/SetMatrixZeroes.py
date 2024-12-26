class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = nums[0]
        i = 1
        n = len(list(set(nums)))
        while len(nums) != n:
            if nums[i] == k:
                nums.pop(i)
            elif nums[i] != k:
                k = nums[i]
                i += 1
        print(nums)
        return n