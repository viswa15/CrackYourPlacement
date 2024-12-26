class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] * nums[1] * nums[-1] > nums[-1] * nums[-2] * nums[-3]:
            return nums[0] * nums[1] * nums[-1]
        return nums[-1] * nums[-2] * nums[-3]
        sol = float("-inf")
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j<k:
                sol = max(sol,nums[i]*nums[j]*nums[k])
                j += 1
                k -= 1

        return sol