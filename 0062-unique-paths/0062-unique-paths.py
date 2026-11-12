class Solution:       
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    up = dp[i - 1][j]
                else:
                    up = 0
                if j == 0:
                    left = 0
                else:
                    left = dp[i][j - 1]
                dp[i][j] = up + left
        return dp[m - 1][n - 1]                        