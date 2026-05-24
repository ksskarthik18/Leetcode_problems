#Time Complexity : O((n*m) + n)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        height = [0]*m
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    height[j]+=1
                else:
                    height[j]=0
            area = self.largestRectangleHeights(height)
            maxArea = max(area,maxArea)
        return maxArea

    def largestRectangleHeights(self,heights):
        n = len(heights)
        stack = []
        maxArea = 0
        for i in range(n):
            while len(stack)!= 0 and heights[stack[-1]] > heights[i]:
                element = stack[-1]
                stack.pop()
                nse = i
                pse = -1 if len(stack)==0 else stack[-1]
                maxArea = max(maxArea,heights[element]*(nse-pse-1))
            stack.append(i)

        while len(stack)!=0:
            nse = n
            element = stack[-1]
            stack.pop()
            pse = -1 if len(stack)==0 else stack[-1]
            maxArea = max(maxArea,heights[element]*(nse-pse-1))
        return maxArea

        