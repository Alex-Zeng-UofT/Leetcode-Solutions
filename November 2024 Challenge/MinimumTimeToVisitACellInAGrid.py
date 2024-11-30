class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        if grid[1][0] > 1 and grid[0][1] > 1: return -1

        def is_valid(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        min_grid = [[float(inf)] * n for _ in range(m)]
        min_grid[0][0] = grid[0][0]

        pq = [(min_grid[0][0], 0, 0)]

        while pq:

            val, r, c = heapq.heappop(pq)

            if r == m - 1 and c == n - 1:
                return val

            for dr, dc in directions:

                row, col = dr + r, dc + c

                if not is_valid(row, col): continue

                wait_time = 1 if (grid[row][col] - val) % 2 == 0 else 0
                new_val = max(val + 1, grid[row][col] + wait_time)

                if new_val < min_grid[row][col]:
                    heapq.heappush(pq, (new_val, row, col))
                    min_grid[row][col] = new_val

        return -1