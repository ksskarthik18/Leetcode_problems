import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high=max(nums)
        while low<=high:
            mid = (low+high)//2
            t_sum=self.get_sum(nums,mid,threshold)
            if t_sum <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low


    def get_sum(self,nums,mid,threshold):
        total_sum=0
        for num in nums:
            total_sum += math.ceil((num+mid-1)//mid)
        return total_sum
        