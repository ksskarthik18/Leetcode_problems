class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+high)//2
            if (self.find_sum(nums,mid,k)== True):
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    

    def find_sum(self,nums,split,k):
        t_sum=0
        cnt=1
        for num in nums:
            t_sum +=num
            if t_sum > split:
                t_sum=num
                cnt+=1
        
        if cnt>k:
            return True
        return False