class Solution:
    def back(self,last,total,subset,k,n):
        if total == n and len(subset) == k:
            self.result.append(subset.copy())
            return
        if total > n or len(subset) > k:
            return    
        for i in range(last,10):
            sum = total + i
            subset.append(i)
            self.back(i+1,sum,subset,k,n)   
            subset.pop() 
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.back(1,0,[],k,n)
        return self.result

        