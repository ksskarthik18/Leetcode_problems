class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        posIndex=0
        negIndex=1
        result=[0]*n
        for i in range(n):
            if nums[i]<0:
                result[negIndex]=nums[i]
                negIndex+=2
            
            else:
                result[posIndex]=nums[i]
                posIndex+=2
        
        return result

        