class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result=[]
        def backTrack(current,openCount,closeCount):
            if len(current) == 2*n:
                result.append(current)
                return

            if openCount<n:
                backTrack(current + "(",openCount+1,closeCount)
            if closeCount<openCount:
                backTrack(current + ")",openCount,closeCount+1)
        backTrack("",0,0)
        return result

        