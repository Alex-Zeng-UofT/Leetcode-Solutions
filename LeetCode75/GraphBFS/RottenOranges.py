class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        queue, next = [], []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

        minutes = -1 if queue else 0

        while queue:

            row, col = queue.pop(0)
            
            if row > 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                next.append((row - 1, col))

            if row < m - 1 and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                next.append((row + 1, col))

            if col > 0 and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                next.append((row, col - 1))

            if col < n - 1 and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                next.append((row, col + 1))

            if not queue:
                minutes += 1
                queue = next.copy()
                next = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return minutes