class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maxCandy = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= maxCandy)
        return result
                
            
        
        