class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low = 0
        high = int(c**0.5)
        while low <= high:
            s = (low*low) +(high*high)
            if s == c:
                return True
            elif s < c:
                low += 1
            else:
                high -= 1
        return False
