from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    queue.append((r,c))
                    

                    while queue:
                        cr,cc = queue.popleft()

                        for dr,dc in directions:
                            nr = cr + dr
                            nc = cc + dc

                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == '1':
                                    grid[nr][nc] = '0'
                                    queue.append((nr,nc))
        return count
