# Write your MySQL query statement below
Select s.product_id,f.first_year,s.quantity,s.price
From sales s
Join (
    Select product_id,
    Min(year) As first_year
    From Sales
    Group by product_id)
f
On s.product_id = f.product_id
And s.year = f.first_year;