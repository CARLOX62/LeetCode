# Write your MySQL query statement below
Select e.employee_id,e.name,
Count(s.employee_id) As reports_count,
Round(AVG(s.age)) As average_age
From Employees e
Join Employees s
On e.employee_id = s.reports_to
Group By e.employee_id, e.name
Order By e.employee_id ;
