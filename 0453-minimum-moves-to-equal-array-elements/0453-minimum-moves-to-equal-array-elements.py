class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minm = min(nums)
        return sum(nums) - minm * len(nums)