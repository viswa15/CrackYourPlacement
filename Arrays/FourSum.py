class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,quads = [],[]
        nums.sort()

        def kSum(k,start,target):
            if k != 2:
                for i in range(start,len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quads.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    quads.pop()
                return

            #basecase twosum II
            l,r = start,len(nums)-1
            while l<r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(quads + [nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4,0,target)
        return res