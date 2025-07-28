# Write your MySQL query statement below
-- select 
--     departmentid,name as employee,salary 
-- from employee where id in (
--     select *,DENSE_RANK() over (
--         PARTItION by departmentID order by salary desc 
--     ) as rankk from employee
-- ) where rankk<4;

with ranked as (
    select *,
    DENSE_RANK() over (PARTItION by departmentID order by salary desc ) as rankk
    from employee
)
select d.name as Department,r.name as Employee,r.salary as Salary from ranked r
join department d 
on d.id = r.departmentid
where rankk<4;