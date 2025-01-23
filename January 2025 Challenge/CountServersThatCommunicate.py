class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        servers = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    servers += 1

        return servers
            