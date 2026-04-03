class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        maxDist= (rows - 1) + (cols - 1)+1
        buckets= [[] for _ in range(maxDist)]

        for r in range(rows):
            for c in range(cols):
                dist = abs(r-rCenter) + abs (c-cCenter)
                buckets[dist].append([r,c])
        result = []
        for bucket in buckets:
            result.extend(bucket)
        return result
        