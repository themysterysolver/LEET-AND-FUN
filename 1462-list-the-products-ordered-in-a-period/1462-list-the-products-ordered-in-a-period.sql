# Write your MySQL query statement below
# common expression table!
with grp_cet as (
    select product_id,sum(unit) as units,order_date from orders  
    where DATE_FORMAT(order_date, '%Y-%m') = '2020-02' group by product_id
)
select p.product_name,g.units as unit from grp_cet g join products p on p.product_id = g.product_id 
where g.units>=100