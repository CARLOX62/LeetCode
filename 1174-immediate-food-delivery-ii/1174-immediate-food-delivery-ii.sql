# Write your MySQL query statement below
Select
  Round(Sum(IF(order_date = customer_pref_delivery_date,1,0)) * 100  / Count(Distinct customer_id), 2) As immediate_percentage
From Delivery
Where(customer_id, order_date) In (
    Select customer_id, min(order_date) As First_order
    From Delivery
    Group by customer_id
)