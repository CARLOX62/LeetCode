class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        has_map ={}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in has_map:
                return [has_map[remaining],i]
            has_map[nums[i]] = i 