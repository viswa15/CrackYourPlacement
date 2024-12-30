class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = [] #pairs :[val,idx]

        for i,val in enumerate(temperatures):
            while stk and stk[-1][0] < val:
                idx = stk.pop()[1]
                res[idx] =  i - idx
            stk.append([val,i])
        return res