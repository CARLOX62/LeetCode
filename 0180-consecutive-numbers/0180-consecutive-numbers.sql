# Write your MySQL query statement below
Select Distinct num As ConsecutiveNums
From (
    Select 
        num,
            Lag(num, 1) Over (order by id) As prev1,
            Lag(num, 2) Over (order by id) As prev2
    From Logs
    ) t
Where num = prev1
 And num = prev2;    
