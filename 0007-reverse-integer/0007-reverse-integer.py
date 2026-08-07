class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        n = abs(x)
        result = 0
        while n > 0 or n < 0:
            digit = n % 10
            result = result * 10 + digit
            n //= 10
        result  *= sign  
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
