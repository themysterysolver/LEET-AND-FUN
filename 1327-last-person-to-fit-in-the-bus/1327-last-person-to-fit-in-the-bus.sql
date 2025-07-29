# Write your MySQL query statement below
with running_avg_cte as (
    select turn,person_name,sum(weight) over (order by turn) as run
    from queue
)
select person_name from running_avg_cte
where run<=1000
order by turn desc
limit 1