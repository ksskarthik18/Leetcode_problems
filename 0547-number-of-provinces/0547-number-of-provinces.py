class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1:
                    if neighbour not in visited:
                        dfs(neighbour)
            
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        return provinces