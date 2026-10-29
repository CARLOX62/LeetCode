class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev1 = 0
        prev2 = 0
        for i in range(2,n + 1):
            jump1 = prev1 + cost[i - 1]
            jump2 = prev2 + cost[i - 2]
            
            curr = min(jump1,jump2)
            prev2 = prev1
            prev1 = curr
        return prev1        
