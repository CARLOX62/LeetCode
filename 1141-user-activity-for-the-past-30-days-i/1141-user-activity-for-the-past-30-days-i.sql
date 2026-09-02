# Write your MySQL query statement below
Select activity_date As day,
Count(Distinct user_id) As active_users
From Activity
Where activity_date Between '2019-06-28' And '2019-07-27' 
Group by activity_date

