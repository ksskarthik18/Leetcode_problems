class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []
        n = len(heights)
        for i in range(n):
            while len(stack)!=0 and heights[stack[-1]] > heights[i]:
                element = stack[-1]
                stack.pop()
                nse = i
                pse = -1 if len(stack) ==0 else stack[-1]
                maxArea = max(maxArea,heights[element]*(nse-pse-1))
            stack.append(i)

        while len(stack)!=0:
            nse = n
            element = stack[-1]
            stack.pop()
            pse = -1 if len(stack)==0 else stack[-1]
            maxArea = max(maxArea,heights[element]*(nse-pse-1))
        return maxArea
            
            
        