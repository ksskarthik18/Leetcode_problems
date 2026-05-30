class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        noDuplicates = set(nums)
        return len(nums) != len(noDuplicates)
        