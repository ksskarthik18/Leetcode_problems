class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        even_count = (n+1)//2
        odd_count =(n)//2
        
        even_part = self.power(5,even_count,MOD)
        odd_part = self.power(4,odd_count,MOD)

        return (even_part * odd_part)% MOD

    def power(self,x,n,mod):
        result = 1
        while n > 0:
            if n%2 == 1:
                result =(result*x) % mod
            
            x = (x * x) % mod
            n = n//2

        return result
        