# Write your MySQL query statement below
Select e1.name
From Employee e1
Join Employee e2
On e1.id = e2.managerId
Group By e1.id,e1.name
Having Count(e2.id) >= 5;