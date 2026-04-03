from collections import Counter

class Solution(object):
    def commonChars(self,words):
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        result=[]
        for char in common:
            result.extend([char] * common[char])
        return result
        # return list(common.elements())

        
