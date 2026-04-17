class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        fst=self.first(nums,target)
        lst=self.last(nums,target)
        return [fst,lst]

    def first(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        first=-1
        while low<= high:
            mid = (low+high)//2
            if nums[mid] == target:
                first=mid
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
            else :
                high = mid -1
        
        return first

    def last(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        last=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                last=mid
                low = mid + 1
            elif nums[mid]> target :
                high= mid - 1
            else :
                low = mid + 1
        return last

        