class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # num_dict = {}
        # for i in nums:
        #     if i not in num_dict:
        #         num_dict[i] = 1
        #     else:
        #         num_dict[i] += 1

        # res = []
        # for i in num_dict:
        #     if num_dict[i]==2:
        #         res.append(i)
        # return res
        res = []
        for i in nums:
            i = abs(i)
            if nums[i-1] < 0:
                res.append(i)
            nums[i-1] = -nums[i-1]
        return res