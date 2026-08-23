class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_sub = 1 << n
        result = []
        for num in range(0,total_sub):
            lst = []
            for i in range(0,n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
            result.append(lst)
        return result            