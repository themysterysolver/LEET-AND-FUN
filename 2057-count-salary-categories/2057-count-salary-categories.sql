# Write your MySQL query statement below

#selecting the tab
-- select case
--         when income<20000 then 'Low Salary'
--         when income>=20000 and income<=50000 then 'Average Salary'
--         else 'High Salary'
--     end as tab
-- from accounts

#deafult thing is missing
-- select tab as category,count(tab) as accounts_count from (
--     select case
--         when income<20000 then 'Low Salary'
--         when income>=20000 and income<=50000 then 'Average Salary'
--         else 'High Salary'
--     end as tab
-- from accounts
-- ) as tabled group by tab;

select base.category,count(t.tab) as accounts_count from (
    select 'Low Salary' as Category UNION ALL SELECT  'High Salary' UNION ALL  SELECT  'Average Salary'
) as base 
left join (
    select case
        when income<20000 then 'Low Salary'
        when income>=20000 and income<=50000 then 'Average Salary'
        else 'High Salary'
    end as tab
    from accounts
) as t 
on base.category=t.tab 
group by base.category;