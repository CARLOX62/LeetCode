class Solution:
    def Backtrack(self,index,total,subset):
        if total == 0:
            self.result.append(subset.copy())
            return
        elif total < 0:
            return
        if index == len(self.candidates):
            return
        for i in range(index,len(self.candidates)):
            if i > index and self.candidates[i] == self.candidates[i-1]:
                continue
            subset.append(self.candidates[i])
            sum = total - self.candidates[i]
            self.Backtrack(i+1,sum,subset)
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.result = []
        self.Backtrack(0,target,[])
        return self.result

        