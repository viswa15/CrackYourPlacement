class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Helper function to merge and count reverse pairs
        def merge_and_count(nums, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_and_count(nums, left, mid) + merge_and_count(nums, mid + 1, right)

            # Merge step: count the reverse pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))

            # Merge two halves of the array
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            temp.extend(nums[i:mid+1])
            temp.extend(nums[j:right+1])

            for i in range(len(temp)):
                nums[left + i] = temp[i]

            return count

        # Call the helper function with the full range of the array
        return merge_and_count(nums, 0, len(nums) - 1)