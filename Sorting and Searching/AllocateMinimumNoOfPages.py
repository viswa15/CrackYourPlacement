class Solution:

    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if len(arr) < k:
            return -1



        low,high = max(arr),sum(arr)
        res = high

        def is_possible(mid):
            pages,c = 0,1

            for i in range(len(arr)):
                if arr[i] + pages > mid:
                    c += 1
                    pages = arr[i]

                    if c > k:
                        return False
                else:
                    pages += arr[i]
            return True


        while low <= high:
            mid = (low+high) // 2

            if is_possible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res