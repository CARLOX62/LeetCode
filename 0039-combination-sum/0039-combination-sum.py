class Solution:
    def Backtrack(self,index,total,subset,nums,target,result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index == len(nums):
            return
        sum = total + nums[index]
        subset.append(nums[index])
        self.Backtrack(index,sum,subset,nums,target,result)
        sum = total
        subset.pop()
        self.Backtrack(index+1,sum,subset,nums,target,result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.Backtrack(0,0,[],candidates,target,result)
        return result
