from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)

            for ch in word_count:
                if word_count[ch] > char_count.get(ch, 0):
                    break
            else:
                total_length += len(word)

        return total_length
        