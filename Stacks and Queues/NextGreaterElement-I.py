class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #O(m+n)
        d = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stk = []

        for i in nums2:
            cur = i
            while stk and cur > stk[-1]:
                val = stk.pop()
                idx = d[val]
                res[idx] = cur
            if cur in nums1:
                stk.append(cur)
        return res


        # O(m*n)
        # res = []
        # for val in nums1:
        #     idx = -1
        #     x = None
        #     for i in range(len(nums2)):
        #         if nums2[i] == val:
        #             idx = i
        #         if nums2[i] > val and idx != -1 and i > idx:
        #             x = nums2[i]
        #             break
        #     if x:
        #         res.append(x)
        #     else:
        #         res.append(-1)
        # return res

