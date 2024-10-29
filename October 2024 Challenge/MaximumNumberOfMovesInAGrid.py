class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        max_moves = 0

        for j in range(n - 2, -1, -1):
            for i in range(m - 1 , -1, -1):

                lt_top = i > 0 and grid[i][j] < grid[i - 1][j + 1]
                lt_middle = grid[i][j] < grid[i][j + 1]
                lt_bottom = i < m - 1 and grid[i][j] < grid[i + 1][j + 1]

                top = dp[i - 1][j + 1] if lt_top else 0
                middle = dp[i][j + 1] if lt_middle else 0
                bottom = dp[i + 1][j + 1] if lt_bottom else 0

                dp[i][j] = (1 + max(top, middle, bottom)) if lt_top or lt_middle or lt_bottom else 0

                if j == 0: max_moves = max(max_moves, dp[i][j])

        return max_moves