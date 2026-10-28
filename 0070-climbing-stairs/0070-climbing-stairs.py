class Solution:
    def func(self,index,dp):
        if index == 0 or index == 1:
            return 1
        if index == 2:
            return 2    
        if dp[index] != -1:
            return dp[index]    
        dp[index] =  self.func(index - 1, dp) + self.func(index - 2, dp)    
        return dp[index]
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.func(n,dp)
        