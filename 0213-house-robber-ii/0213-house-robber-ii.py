class Solution:
    def solve(self, nums):
        n = len(nums)
        prev = nums[0]   # DP for index - 1
        prev2 = 0        # DP for index - 2
        for index in range(1, n):
            # Pick current house and add loot from two steps back
            if index > 1:
                pick = nums[index] + prev2
            else:
                pick = nums[index]
            # Skip current house, use prev result
            not_pick = prev
            curr = max(pick, not_pick)
            # Update window
            prev2 = prev
            prev = curr
        return prev
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # Try both scenarios (excluding first or last house)
        ans1 = self.solve(nums[0 : n - 1])
        ans2 = self.solve(nums[1 : n])
        return max(ans1, ans2) 