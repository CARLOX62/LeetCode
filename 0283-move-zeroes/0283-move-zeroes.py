class Solution:
    def zero(self,nums):
        i = 0
        if len(nums) == 1:
            return
        while i<len(nums):
            if nums[i] == 0:
                break
            i+=1
        if i == len(nums):
            return
        j = i+1
        while j<len(nums):
            if nums[j]!= 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+=1                    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.zero(nums)