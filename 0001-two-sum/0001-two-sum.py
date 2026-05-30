class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,num in enumerate(nums):
            rem = target - num

            if rem in seen:
                return [seen[rem],i]
            
            seen[num] = i
        