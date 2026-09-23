class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        maxwater = 0
        while i < j:
            w = j - i
            h = min(height[i],height[j])
            a = w * h
            maxwater = max(maxwater,a)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxwater            