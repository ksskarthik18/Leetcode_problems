class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.']*n for _ in range(n)]
        cols = set()
        diagonal1 = set()
        diagonal2 = set()
        result=[]
        def backTrack(row):
            if row == n:
                temp=[]

                for r in board:
                    temp.append("".join(r))
                result.append(temp)
                return
            
            for col in range(n):
                if col in cols or (row-col) in diagonal1 or (row+col) in diagonal2:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                diagonal1.add(row-col)
                diagonal2.add(row+col)

                backTrack(row+1)

                board[row][col] ='.'
                cols.remove(col)
                diagonal1.remove(row-col)
                diagonal2.remove(row+col)
        backTrack(0)
        return result