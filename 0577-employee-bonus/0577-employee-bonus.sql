# Write your MySQL query statement below
Select Employee.name, Bonus.bonus
from Employee
Left join Bonus
ON Employee.empId = Bonus.empId
Where bonus < 1000 Or Bonus.bonus is Null;