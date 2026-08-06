class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x    
        result = 0
        while n > 0:
            id = n % 10
            result = (result * 10) + id
            n = n // 10
        return result == x