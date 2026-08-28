class Solution:
    def backtrack(self,index,subset):
        if index == len(self.digits):
            self.result.append("".join(subset))
            return
        for chr in self.chr_map[self.digits[index]]:
            subset.append(chr)
            self.backtrack(index+1,subset)
            subset.pop()
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        if digits == "":
            return []

        self.digits = digits
        self.chr_map = {'2':'abc','3':'def','4':'ghi',
        '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.backtrack(0,[])
        return self.result

