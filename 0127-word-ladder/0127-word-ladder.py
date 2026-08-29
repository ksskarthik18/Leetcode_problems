from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque()
        queue.append((beginWord,1))

        while queue:
            word,steps = queue.popleft()

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i+1:]

                    if new_word == endWord:
                        return steps + 1
                    elif new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word,steps+1))

        return 0
