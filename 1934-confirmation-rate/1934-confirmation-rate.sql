# Write your MySQL query statement below
Select Signups.user_id,
Round(COALESCE(Avg(Confirmations.action = 'confirmed'), 0),2) As confirmation_rate
From Signups
Left Join Confirmations
On Signups.user_id = Confirmations.user_id
Group By user_id;