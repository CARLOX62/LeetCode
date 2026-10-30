class Solution:
    def solve(self, index, nums, dp):
        # If only one house left, rob it
        if index == 0:
            return nums[index]
        # If no houses left
        if index == -1:
            return 0
        # Use cached value if available
        if dp[index] != -1:
            return dp[index]
        # Option 1: Pick and add result from index-2
        pick = nums[index] + self.solve(index - 2, nums, dp)
        # Option 2: Skip current house
        notpick = self.solve(index - 1, nums, dp)
        dp[index] = max(pick, notpick)
        return dp[index] 
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        # Rob from 0 to n-2
        dp1 = [-1] * (n - 1)
        ans1 = self.solve(n - 2, nums[0 : n - 1], dp1)
        # Rob from 1 to n-1
        dp2 = [-1] * (n - 1)
        ans2 = self.solve(n - 2, nums[1 : n], dp2)
        return max(ans1, ans2)   