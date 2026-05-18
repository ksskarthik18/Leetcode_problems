class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop()!= pairs[c]:
                    return False
        return len(stack) == 0 
        