class Solution:
    def duplicate(self,nums):
        n = len(nums)
        i=0
        j=i+1
        if n == 1:
            return 1
        while j < n:
            if nums[j] != nums[i]:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
            j+=1
        return i+1          
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.duplicate(nums)
        