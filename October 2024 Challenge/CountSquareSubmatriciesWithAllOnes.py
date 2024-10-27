class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        count = 0

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0: continue
            
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                count += dp[i + 1][j + 1]

        return count