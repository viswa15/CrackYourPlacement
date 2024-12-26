class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0,len(nums)-1
        x = target
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            elif nums[l] == nums[m] and nums[m] == nums[h]:
                l += 1
                h -= 1

            elif nums[l] <= nums[m]:
                #checking if x in left sorted part or not
                if nums[l] <= x and x <= nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[h]:
                #checking if x in right sorted part or not
                if x >= nums[m] and x <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        return -1