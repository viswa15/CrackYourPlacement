class Solution:
    def quick_select(self,arr,k):
        n = len(arr)
        pivot = random.choice(arr)
        left =  [x for x in arr if x > pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]

        if len(left) >= k:
            return self.quick_select(left,k)
        elif len(left) + len(mid) < k:
            return self.quick_select(right,k-len(left)-len(mid))
        return pivot

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # return nums[k-1]
        return self.quick_select(nums,k)
