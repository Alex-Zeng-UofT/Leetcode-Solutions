class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1, 2, 5] + [0] * (n - 3)

        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % MOD

        return dp[n - 1]