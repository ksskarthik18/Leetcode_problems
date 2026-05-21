class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD =10**9 + 7
        n = len(arr)
        pse = self.findPSE(arr,n)
        nse = self.findNSE(arr,n)
        total=0
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            total += (left*right*arr[i])%MOD
            total = total%MOD
        return total
        
    def findPSE(self,arr,n):
        stack=[]
        pse =[-1]*n
        for i in range(n):
            while len(stack)!=0 and arr[stack[-1]] > arr[i]:
                stack.pop()
            if len(stack) == 0:
                pse[i] = -1
            else:
                pse[i] = stack[-1]
            stack.append(i)
        return pse
    
    def findNSE(self,arr,n):
        stack=[]
        nse =[-1]*n
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                nse[i] = n
            else:
                nse[i] = stack[-1]
            
            stack.append(i)
        return nse
        