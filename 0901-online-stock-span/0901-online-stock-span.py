#Time Complexity : O(2N)
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.index+=1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        ans = self.index - (-1 if not self.stack else self.stack[-1][1])
        self.stack.append((price,self.index))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)