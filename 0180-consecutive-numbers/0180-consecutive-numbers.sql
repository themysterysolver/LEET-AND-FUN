# Write your MySQL query statement below
with cons as (
    select 
    *,lead(num) over (order by id ) as next,
    lag(num) over (order by id) as prev 
    from logs
)
select distinct(num) as ConsecutiveNums from cons where num = prev and num = next; 