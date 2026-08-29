# Write your MySQL query statement below
Select query_name,
Round(Avg(rating / position) ,2) As quality,

Round(sum(case when rating < 3 then 1 else 0 end) * 100.0 / count(*) ,2) 
As poor_query_percentage

From Queries
Group by query_name;