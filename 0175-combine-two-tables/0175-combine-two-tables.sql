# Write your MySQL query statement below
select p.firstName,p.lastName,a.city,a.state from person p LEFT JOIN address a ON a.personID=p.personID;