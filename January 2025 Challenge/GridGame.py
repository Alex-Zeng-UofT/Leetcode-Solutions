class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        first = sum(grid[0])
        second = 0
        minimum_sum = float("inf")

        for turn_index in range(len(grid[0])):
            first -= grid[0][turn_index]
            minimum_sum = min(minimum_sum, max(first, second))
            second += grid[1][turn_index]
            
        return minimum_sum