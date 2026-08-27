# Write your MySQL query statement below
Select p.project_id,
Round(AVG(experience_years),2) AS average_years
From Project p
Join Employee e
On p.employee_id = e.employee_id
Group by project_id