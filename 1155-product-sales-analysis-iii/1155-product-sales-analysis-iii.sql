# Write your MySQL query statement below

#grouping the product_id and taking min val
-- select product_id,min(year)
-- from sales group by product_id

#with is used to created temp table

with firstSalesYear as (
    select product_id,min(year) as first_year
    from sales
    group by product_id
)

select s.product_id,f.first_year,s.quantity,s.price
from sales s 
join firstSalesYear f 
on s.product_id=f.product_id and s.year=f.first_year