class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        ans = 0
        maxFreq = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            maxFreq = max(maxFreq,count[s[right]])
            while (right - left + 1) - maxFreq > k:
                count[s[left]]-=1
                left+=1
            
            ans = max(ans,right-left+1)
        return ans