# Write your MySQL query statement below
Select EmployeeUNI.unique_id, Employees.name
from Employees
LEFT join EmployeeUNI
ON Employees.id = EmployeeUNI.id;