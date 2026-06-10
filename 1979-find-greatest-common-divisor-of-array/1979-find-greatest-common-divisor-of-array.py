class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = min(nums)
        b = max(nums)
        ans = self.gcd(a,b)
        return ans
    
    def gcd(self,a,b):
        while b:
            a , b = b , a % b
        return a