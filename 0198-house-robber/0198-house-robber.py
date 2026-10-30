class Solution:
    def func(self,index,nums,dp):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]    
        pick = nums[index] + self.func(index - 2,nums,dp)
        not_pick = 0 + self.func(index - 1,nums,dp) 
        dp[index] = max(pick,not_pick)  
        return dp[index]     
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.func(n - 1,nums,dp)