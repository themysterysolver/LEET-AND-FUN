# Write your MySQL query statement below
with count_distinct as(
    select count(distinct customer_id) as count from delivery 
),earliest_order as (
    select d.customer_id,d.order_date,d.customer_pref_delivery_date from delivery d
    join 
    (select customer_id,min(order_date) as o from delivery
    group by customer_id) t
    on d.customer_id = t.customer_id and d.order_date = t.o 
),immdeiate_orders as (
    select count(customer_id) as count from earliest_order 
    where order_date = customer_pref_delivery_date
)
select round( (i.count * 1.0) / (c.count * 1.0)*100 ,2) as immediate_percentage from count_distinct c,immdeiate_orders i