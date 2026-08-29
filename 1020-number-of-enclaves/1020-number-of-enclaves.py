from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1) or (c == 0 or c == cols - 1):
                    if grid[r][c] == 1:
                        queue.append((r,c))
                        grid[r][c] = 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            r,c = queue.popleft()
            
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 0
        
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
        
        return count


        