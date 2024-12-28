class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low,high = max(nums),sum(nums)
        res = high

        def is_possible(mid):
            c,p = 0,0
            for i in nums:
                c += i
                if c > mid:
                    c = i
                    p += 1
            return 1 + p <= k

        while low <= high:
            mid = low + ((high-low)//2)
            if is_possible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res