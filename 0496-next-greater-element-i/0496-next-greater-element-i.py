class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Find next greater element for every element in nums2
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        # Elements remaining in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build answer for nums1
        ans = []
        for num in nums1:
            ans.append(next_greater[num])

        return ans