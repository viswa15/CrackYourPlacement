from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #brute force
        # res = [0] * len(nums)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] > nums[j]:
        #             res[i] += 1
        # return res
        sorted_arr = SortedList()
        res = []

        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            idx = sorted_arr.bisect_left(n)
            res.append(idx)
            sorted_arr.add(n)
        return res[::-1]