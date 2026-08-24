class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(index,subset):
            if index == len(nums):
                result.append(subset.copy())
                return

            # Take The Current Element    
            subset.append(nums[index])
            solve(index+1,subset)

            # Donot take The Current Element
            subset.pop()
            solve(index+1,subset)

        solve(0,[])
        return result        


                    