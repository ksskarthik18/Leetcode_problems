class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        freq = Counter(s)
        buckets = [[] for _ in range(len(s)+1)]

        for ch,f in freq.items():
            buckets[f].append(ch)
        result = ""
        for i in range(len(s),0,-1):
            for ch in buckets[i]:
                result += ch*i
        return result 
        