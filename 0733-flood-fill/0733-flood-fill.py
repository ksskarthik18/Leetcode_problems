from collections import deque
class Solution(object):
    def floodFill(self,image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        if old_color == color:
            return image
        rows = len(image)
        cols = len(image[0])
        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color
        while queue:
            r,c = queue.popleft()
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == old_color:
                        image[nr][nc] = color
                        queue.append((nr,nc))
        return image
