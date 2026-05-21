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

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nge ={}
        n2 = len(nums2)
        for i in range(n2-1,-1,-1):
            while not (self.empty()) and self.top()<= nums2[i]:
                self.pop()
            if self.empty():
                nge[nums2[i]] = -1
            else:
                nge[nums2[i]] = self.top()
            self.push(nums2[i])
        result =[]
        for num in nums1:
            result.append(nge[num])
        return result
    

        