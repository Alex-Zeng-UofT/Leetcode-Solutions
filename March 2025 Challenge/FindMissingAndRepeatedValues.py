class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        a, b = 0, 0

        nums = set([i for i in range(1, len(grid) ** 2 + 1)])

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in nums:
                    nums.remove(grid[i][j])
                else:
                    a = grid[i][j]

        for num in nums:
            b = num
        
        return [a, b]