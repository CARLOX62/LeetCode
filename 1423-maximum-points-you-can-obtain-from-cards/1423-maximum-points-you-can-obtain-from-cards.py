class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_point = 0
        left_point = 0
        right_point = 0
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        for i in range(k):
            left_point += cardPoints[i]
        max_point = left_point
        right_ind = n-1
        for i in range(k-1,-1,-1):
            left_point -= cardPoints[i]
            right_point += cardPoints[right_ind]  
            max_point = max(max_point,left_point + right_point)
            right_ind -= 1
        return max_point    
