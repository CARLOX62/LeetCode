class Solution:
    def rev(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1       
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.rev(nums,n-k,n-1)
        self.rev(nums,0,n-k-1)
        self.rev(nums,0,n-1)