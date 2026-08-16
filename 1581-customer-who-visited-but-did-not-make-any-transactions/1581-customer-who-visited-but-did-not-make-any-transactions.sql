# Write your MySQL query statement below
Select Visits.customer_id, 
count(*) As count_no_trans
From Visits
Left join Transactions On
Visits.visit_id = Transactions.visit_id
where Transactions.transaction_id is Null
Group by Visits.customer_id;