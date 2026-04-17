#Time Complexity : O(log n base 2)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        res=float('inf')
        while low<= high:
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                res = min(res,nums[low])
                low = mid + 1
                
            else:
                res = min(res,nums[mid])
                high = mid - 1
        
        return res

                        