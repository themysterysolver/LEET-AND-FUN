# Write your MySQL query statement below
with before_it as (
    select * from products p1 where change_date in
    (select max(change_date) from products 
    where p1.product_id = product_id and change_date <= '2019-08-16' 
    group by product_id)
),
perfect as (
select product_id,new_price as price from products where change_date = '2019-08-16' 
),
before_not_perfect as (
    select product_id,new_price as price from before_it 
    where product_id not in 
    (select product_id from perfect)
), def_10 as (
    select product_id,10 as price from 
    (select distinct product_id from products) p 
    where p.product_id not in (select product_id from perfect)
    and p.product_id not in (select product_id from before_not_perfect)
)  
select * from def_10
union all
select * from perfect
union all
select * from before_not_perfect