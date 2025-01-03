class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        nums.sort()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        vals = list(d.values())
        vals.sort(reverse=True)
        print(vals)
        while k:
            for i in d:
                if d[i] == vals[0]:
                    k-=1
                    res.append(i)
                    d.pop(i)
                    vals.pop(0)
                    break
        return res
