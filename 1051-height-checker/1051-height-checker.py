class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        expected= sorted(heights)
        result = []
        for i in range(len(heights)):
            if heights[i] != expected[i] :
                result.append(i)
        
        return len(result)
        