class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        triplet = []
        nums.sort()
        for i in range(length-2):
            j = i+1
            k = length - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    current_triplet = [nums[i],nums[j],nums[k]]
                    if current_triplet not in triplet:
                        triplet.append(current_triplet)
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return triplet