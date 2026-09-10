class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0 
        right = 0 
        jump = 0
        while right < n-1:
            furthest = 0
            for i in range(left,right+1):
                furthest = max(furthest,i+nums[i])
            left = right + 1
            right = furthest
            jump += 1
        return jump        

