class Solution:

    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        while arr and arr[0] <= 0:
            arr.pop(0)
        if not arr:
            return 1

        arr = list(set(arr))

        sol = 1

        for i in arr:
            if sol == i:
                sol += 1
            else:
                sol = min(sol,i)
        return sol
