# Write your MySQL query statement below
with stock_buy_cte as (
    select stock_name,sum(price) as p1 from stocks where operation='Buy' group by stock_name
),stock_sell_cte as (
     select stock_name,sum(price) as p2 from stocks where operation='Sell' group by stock_name 
)

select t1.stock_name,t2.p2 - t1.p1 as capital_gain_loss from stock_buy_cte t1 join stock_sell_cte t2 on t1.stock_name=t2.stock_name;