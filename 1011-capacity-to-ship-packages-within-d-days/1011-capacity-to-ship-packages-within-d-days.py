class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = (low + high)//2
            day=self.find_days(weights,mid)
            if day <= days:
                high = mid -1
            else:
                low = mid + 1
        return low

    def find_days(self,weights,capacity):
        day=1
        total_weight_day=0
        for num in weights:
            total_weight_day+=num
            if total_weight_day>capacity:
                total_weight_day=num
                day+=1
        
        return day
        