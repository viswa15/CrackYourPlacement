class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sol = float("inf")
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            i,j = 0,len(nums)-1
            c = 0
            while j-i != 1:
                c += abs(nums[i]-nums[j])
                i += 1
                j -= 1
            return min(sol,c+nums[j]-nums[i])
        else:
            i,j = 0,n-1
            c = 0
            while i < j:
                c += abs(nums[j]-nums[i])
                i += 1
                j -= 1
            return min(sol,c)

