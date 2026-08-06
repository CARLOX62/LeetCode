class Solution:
    def Maxcon(self,nums):
        i=0
        count = 0
        max_count = 0
        while i < len(nums):
            if nums[i] == 1:
                count+=1
            else:
                max_count = max(max_count,count)
                count=0
            i+=1
        return max(max_count,count)            
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.Maxcon(nums)