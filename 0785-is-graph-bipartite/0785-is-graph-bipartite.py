class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [-1]*n

        def dfs(node):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]

                    if not dfs(neighbour):
                        return False
                
                if color[neighbour] == color[node]:
                    return False
            
            return True

        for start in range(n):
            if color[start] == -1:
                color[start]=0
                if not dfs(start):
                    return False
        
        return True
        