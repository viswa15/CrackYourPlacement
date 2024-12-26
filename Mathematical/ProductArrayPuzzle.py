class Solution:
    def isPossible(self,k,arr1,arr2):
        n = len(arr1)
        arr1.sort()
        arr2.sort(reverse=True)
        for i in range(n):
            if arr1[i] + arr2[i] < k:
                return False
        return True