class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        left ,right = 0, n-1
        top, bottom = 0, n-1
        val = 1
        while left <= right:
            for i in range(left,right+1):
                mat[top][i] = val
                val += 1
            top += 1    

            for i in range(top,bottom+1):
                mat[i][right] = val
                val += 1
            right -= 1 

            for i in range(right,left-1,-1):
                mat[bottom][i] = val
                val += 1
            bottom -= 1

            for i in range(bottom,top-1,-1):
                mat[i][left] = val
                val += 1
            left += 1
        return mat               