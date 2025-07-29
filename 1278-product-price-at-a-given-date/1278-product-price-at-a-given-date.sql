# Write your MySQL query statement below
select product_id,coalesce(
    (
        select new_price from products p
        where p.product_id = t.product_id and p.change_date<='2019-08-16'
        order by p.change_date desc 
        limit 1
    ),10
) as price from (select distinct product_id from products) t