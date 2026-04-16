class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        map1={}
        count1=0
        for a,b in dominoes:
            key = (min(a,b),max(a,b))

            if key in map1:
                count1+=map1[key]
                map1[key]+=1

            else:
                map1[key]=1

        return count1     