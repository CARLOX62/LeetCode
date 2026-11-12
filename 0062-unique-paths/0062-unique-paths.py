class Solution:       
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [-1] * n  # Previous row
        for i in range(0, m):
            curr = [-1] * n  # Current row
            for j in range(0, n):
                if i == 0 and j == 0:
                    curr[0] = 1  # Start
                    continue
                # up: from the row above
                if i == 0:
                    up = 0
                else:
                    up = prev[j]
                # left: from the same row, previous column
                if j == 0:
                    left = 0
                else:
                    left = curr[j - 1]
                curr[j] = up + left
            prev = curr  # Move current row to prev
        return prev[n - 1]                       