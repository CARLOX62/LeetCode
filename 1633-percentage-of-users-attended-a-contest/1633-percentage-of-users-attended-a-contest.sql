# Write your MySQL query statement below
Select contest_id,
Round(count(user_id) * 100.0 / (select count(*) From Users), 2)
As percentage
from Register
group by contest_id
order by percentage desc, contest_id asc;
 