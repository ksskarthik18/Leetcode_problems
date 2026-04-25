class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=[]
        word=""
        for ch in s:
            if ch != " ":
                word+=ch
            else:
                if word:
                    words.append(word)
                    word=""
        if word:
            words.append(word)

        return " ".join(words[::-1])