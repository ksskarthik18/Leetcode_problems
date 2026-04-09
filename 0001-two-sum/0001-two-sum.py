class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                    return result

        
nums=[2,7,11,15]
target=9
s=Solution()
print("Result :",s.twoSum(nums,target))
    