class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        res = 0
        d = {0:1}
        for i in nums:
            cur += i
            diff = cur-k

            res += d.get(diff,0)
            d[cur] = 1 + d.get(cur,0)
        return res