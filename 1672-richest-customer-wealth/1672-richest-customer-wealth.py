class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth= 0
        for i in range(len(accounts)):
            maxWealth = max(maxWealth,sum(accounts[i]))
        return maxWealth

        