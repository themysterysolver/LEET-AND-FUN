# Write your MySQL query statement below
select 
    case
        when (select count(distinct(salary)) from employee)<2 then null 
        else (select distinct(salary) from employee order by salary desc limit 1 offset 1)
    end as SecondHighestSalary