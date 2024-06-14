class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(cur: int, grid: List[List[int]], visited: List[bool]) -> None:
            for i in range(len(grid[0])):
                if not visited[i] and grid[cur][i] == 1:
                    visited[i] = True
                    dfs(i, grid, visited)
        
        provinces = 0
        visited = [False for i in isConnected]

        for i in range(len(isConnected)):
        
            if not visited[i]:
                visited[i] = True
                provinces += 1
                dfs(i, isConnected, visited)

        return provinces
