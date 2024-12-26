class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = [0]
        left = [0] * n
        right =[n-1]  * n

        for i in range(n):
            if not stk:
                stk.append(i)
                left[i] = 0
            else:
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                left[i] = 0 if not stk else stk[-1] + 1
                stk.append(i)
        stk = []
        for i in range(n-1,-1,-1):
            if not stk:
                stk.append(i)
                right[i] = n-1
            else:
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                right[i] = n-1 if not stk else stk[-1] - 1
                stk.append(i)
        max_area = 0
        for i in range(n):
            area = (right[i] - left[i] + 1) * heights[i]
            max_area = max(area,max_area)
        return max_area

        #second method

        # area = 0
        # for i in range(len(heights)):
        #     c = heights[i]
        #     j,k = i-1,i+1
        #     while j>0 and heights[j] >= heights[i]:
        #         c += heights[i]
        #         j -= 1
        #     if j==0 and heights[j] >= heights[i]:
        #         c += heights[i]

        #     while k<len(heights)-1 and heights[k]>=heights[i]:
        #         c += heights[i]
        #         k+=1
        #     if k==len(heights)-1 and heights[k]>=heights[i]:
        #         c += heights[i]
        #     area=max(area,c)
        # return area
