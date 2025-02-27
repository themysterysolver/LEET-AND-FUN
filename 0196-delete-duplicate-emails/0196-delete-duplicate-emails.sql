# Write your MySQL query statement below
DELETE p1 FROM Person p1 JOIN Person p2 on p1.email=p2.email and p1.id>p2.id;