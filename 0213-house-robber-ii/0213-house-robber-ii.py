class Solution:
    def solve(self, nums):
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        for index in range(1, n):
            # Pick current + two steps back if possible
            if index > 1:
                pick = nums[index] + dp[index - 2]
            else:
                pick = nums[index]
            # Skip current, take previous result
            not_pick = dp[index - 1]
            dp[index] = max(pick, not_pick)
        return dp[n - 1]
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # Exclude last and exclude first scenarios
        ans1 = self.solve(nums[0 : n - 1])
        ans2 = self.solve(nums[1 : n])
        return max(ans1, ans2)  