class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            curr_lcm = 1
            for j in range(i,n):
                curr_lcm = self.lcm(curr_lcm,nums[j])

                if curr_lcm == k:
                    count+=1
                elif curr_lcm > k:
                    break
        return count


    
    def lcm(self,a,b):
        return a * b//self.gcd(a,b)
    def gcd(self,a,b):
        while b:
            a,b = b,a%b
        return a
            