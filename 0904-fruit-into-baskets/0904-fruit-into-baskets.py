class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        R = 0
        L = 0
        max_length = 0
        my_dict = {}
        while R < n:
            my_dict[fruits[R]] = my_dict.get(fruits[R],0) + 1
            if len(my_dict) > 2:
                my_dict[fruits[L]] -= 1
                if my_dict[fruits[L]] == 0:
                    del my_dict[fruits[L]]
                L += 1
            max_length = max(max_length,R-L+1)    
            R += 1
        return max_length    
