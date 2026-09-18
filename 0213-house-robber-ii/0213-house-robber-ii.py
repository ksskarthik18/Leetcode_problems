class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_linear(arr):
            m = len(arr)
            dp = [0]*m
            dp[0] = arr[0]
            if m > 1:
                dp[1] = max(arr[0],arr[1])
            
            for i in range(2,m):
                pick = arr[i] + dp[i-2]
                not_pick = dp[i-1]

                dp[i] = max(pick,not_pick)
            
            return dp[m-1]
        
        case1 = rob_linear(nums[1:])
        case2 = rob_linear(nums[:-1])

        return max(case1,case2)


            
        