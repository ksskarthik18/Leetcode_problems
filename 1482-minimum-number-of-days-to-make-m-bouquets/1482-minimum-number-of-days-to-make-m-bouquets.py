class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        low = min(bloomDay)
        high =max(bloomDay)
        ans=-1
        while low<=high:
            mid = (low + high)//2
            if (self.possible(bloomDay,mid,m,k)==True):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
    

    def possible(self,bloomDay,mid,m,k):
        cnt=0
        n=len(bloomDay)
        no_of_boquets=0
        for i in range(n):
            if bloomDay[i]<= mid:
                cnt+=1
            else:
                no_of_boquets+=(cnt/k)
                cnt=0
        no_of_boquets += cnt/k
        if no_of_boquets >= m:
            return True
        return False
            