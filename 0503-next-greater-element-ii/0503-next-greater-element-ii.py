#Time Complexity : O(2N)
class Solution(object):
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if self.empty():
            return "Stack Underflow"
        return self.stack.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return len(self.stack) == 0
    
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nge =[-1]*n
        for i in range(2*n-1,-1,-1):
            while (not self.empty()) and self.top() <= nums[i%n]:
                self.pop()
            
            if i < n:
                if self.empty():
                    nge[i]=-1
                else:
                    nge[i]= self.top()
            self.push(nums[i%n])

        return nge