from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1) or (c == 0 or c == cols -1):
                    if board[r][c] == 'O':
                        queue.append((r,c))
                        board[r][c] = '#'
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 'O':
                        queue.append((nr,nc))
                        board[nr][nc] = '#'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'


        