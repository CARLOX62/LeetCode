# Write your MySQL query statement below
Select user_id,
Count(follower_id) As followers_count
From Followers
Group By user_id
Order by user_id Asc;

