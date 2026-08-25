class Solution:
    def backtrack(self,index,total,bracket,result):
        if index == len(bracket):
            if total == 0:
                result.append("".join(bracket))
            return
        elif total < 0:
            return
        elif total > len(bracket) // 2:
            return

        bracket[index] = "("
        sum = total + 1
        self.backtrack(index+1,sum,bracket,result)
        bracket[index] = ")"
        sum = total - 1
        self.backtrack(index+1,sum,bracket,result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        bracket = [""] * (n*2)
        self.backtrack(0,0,bracket,result)
        return result
        