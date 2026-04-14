class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map1={0:1}
        pre_sum=0
        count=0
        for num in nums:
            pre_sum+=num
            remove = pre_sum - k
            if remove in map1:
                count+=map1[remove]
            map1[pre_sum]=map1.get(pre_sum,0)+1
        
        return count
        