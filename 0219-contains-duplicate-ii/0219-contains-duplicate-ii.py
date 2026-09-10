class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        my_dict = {}
        for i in range(n):
            if nums[i] in my_dict:
                if i - my_dict[nums[i]] <= k:
                    return True
     
            my_dict[nums[i]] = i

        return False        