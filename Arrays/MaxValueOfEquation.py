class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()
        max_value = float('-inf')

        for x, y in points:
            # Remove points from the deque where x - x_i > k
            while dq and x - dq[0][1] > k:
                dq.popleft()

            # If deque is not empty, calculate the current max value
            if dq:
                max_value = max(max_value, dq[0][0] + y + x)

            # Remove points from the deque that have a smaller (y_i - x_i) than the current point
            while dq and dq[-1][0] <= y - x:
                dq.pop()

            # Add the current point (y - x, x) to the deque
            dq.append((y - x, x))

        return max_value
        # for i in range(len(points)-1):
        #     for j in range(i+1,len(points)):
        #         if abs(points[i][0] - points[j][0]) <= k:
        #             val = points[i][1] + points[j][1] + abs(points[i][0] - points[j][0])
        #             res = max(val,res)
        #         else:
        #             break
        # return res