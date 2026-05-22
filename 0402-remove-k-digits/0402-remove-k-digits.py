class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in num:
            while len(stack)!=0 and k > 0 and stack[-1] > ch:
                stack.pop()
                k-=1
            stack.append(ch)
        
        while k > 0:
            stack.pop()
            k-=1
        
        result = "".join(stack)
        result = result.lstrip('0')
        return result if result else '0'
        