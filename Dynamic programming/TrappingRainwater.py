class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        left_max,right_max = height[i],height[j]
        a = 0
        while i<j:
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
            if left_max < right_max:
                a += left_max - height[i]
                i+=1
            else:
                a += right_max - height[j]
                j-=1
        return a