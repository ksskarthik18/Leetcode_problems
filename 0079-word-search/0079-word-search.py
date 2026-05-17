class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        row = len(board)
        col = len(board[0])

        def backTrack(r,c,index):
            if index == len(word):
                return True
            
            if r< 0 or c<0  or r >= row or c >= col or board[r][c]!= word[index]:
                return False
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                backTrack(r+1,c,index+1) or
                backTrack(r-1,c,index+1) or
                backTrack(r,c+1,index+1) or
                backTrack(r,c-1,index+1) 
            )

            board[r][c] = temp

            return found

        for r in range(row):
            for c in range(col):
                if backTrack(r,c,0):
                    return True

        return False