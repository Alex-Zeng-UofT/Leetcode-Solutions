class Solution:
    def coloredCells(self, n: int) -> int:
        
        side = 2 * n - 1
        
        return side ** 2 // 2 + 1