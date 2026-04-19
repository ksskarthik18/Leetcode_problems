class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low=1
        high=n-2
        if n == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1

        while low <=high:
            mid = (low + high)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid]:
                high = mid - 1
            elif nums[mid-1]<nums[mid]:
                low = mid + 1
            else:
                low = mid + 1
        return -1



        