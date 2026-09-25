class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        arr = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(arr,nums[i])
        for i in range(k,n):
            if nums[i] > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr,nums[i])
        return arr[0]            