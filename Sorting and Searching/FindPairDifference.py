from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if i!=j and abs(arr[j]-arr[i])==x:
        #             return True
        # return False

        seen = set()
        for num in arr:
            if (num - x) in seen or (num + x) in seen:
                return True
            seen.add(num)
        return False
