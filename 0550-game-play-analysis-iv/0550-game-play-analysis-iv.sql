# Write your MySQL query statement below
Select Round(Count(Distinct player_id) / (Select Count(Distinct player_id) From Activity),2) As fraction
From Activity
Where (player_id, Date_sub(event_date, interval 1 day)) 
In (Select player_id, min(event_date) As first_login
From Activity
Group by player_id) 
