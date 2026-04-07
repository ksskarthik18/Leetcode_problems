class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []

        count = {}
        for x in arr1:
            count[x] = count.get(x, 0) + 1
        
    
        for x in arr2:
            if x in count:
                res.extend([x] * count[x])
                del count[x]
        
        # Sort the remaining elements not in arr2 and append them
        remaining = sorted(count.keys())
        for x in remaining:
            res.extend([x] * count[x])
            
        return res