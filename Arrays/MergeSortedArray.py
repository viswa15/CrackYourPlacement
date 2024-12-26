class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for _ in range(len(nums2)):
            nums1.pop()
        nums1 += nums2
        nums1.sort()