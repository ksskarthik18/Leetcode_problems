class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack =[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        if self.empty():
            return "Stack Underflow"
        self.min_stack.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return -1
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
    def empty(self):
        return len(self.stack) == 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()