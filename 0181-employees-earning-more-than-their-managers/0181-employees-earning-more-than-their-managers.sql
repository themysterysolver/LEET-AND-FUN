# Write your MySQL query statement below
SELECT e2.name as Employee FROM Employee e1 JOIN Employee e2 ON e2.managerID=e1.id WHERE e1.salary<e2.salary;
