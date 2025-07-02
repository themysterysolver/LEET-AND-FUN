# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary as Salary from
employee e join department d on e.departmentid=d.id 
where (e.departmentid,e.salary) in 
(select departmentid,max(salary) from employee group by departmentid)