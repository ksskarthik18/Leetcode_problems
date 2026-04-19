import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n = len(piles)
        low = 1
        high = max(piles)
        result = high
        while low<=high:
            mid = (low + high)//2
            t_hr = self.hours(piles,mid)
            if t_hr <= h :
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
                
    def hours(self,piles,mid):
        total_hours=0
        for pile in piles:
            total_hours += math.ceil((pile + mid - 1)//mid)
        return total_hours       