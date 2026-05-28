class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeroes = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right]==0:
                zeroes+=1
            
            while zeroes > k:
                if nums[left] == 0:
                    zeroes-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans
            
        