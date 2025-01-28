class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        
        def dfs(row, col):

            if row < 0 or row >= m or col < 0 or col >= n or not grid[row][col]:
                return 0

            cur = grid[row][col]
            grid[row][col] = 0

            return cur + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        max_fish = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish