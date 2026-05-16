class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def backTrack(index,current):
            result.append(current[:])

            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backTrack(i+1,current)
                current.pop()
        backTrack(0,[])
        return result