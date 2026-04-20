class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)

    # impossible case
        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if self.can_make(bloomDay, m, k, mid):
                ans = mid
                high = mid - 1   # try smaller day
            else:
                low = mid + 1    # need more days

        return ans

    def can_make(self,bloomDay, m, k, day):
        bouquets = 0
        count = 0

        for bloom in bloomDay:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0

        return bouquets >= m        