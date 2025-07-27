# Write your MySQL query statement below
# CET
with coord_count as (
    select lat,lon,count(*) as count from insurance
    group by lat,lon
),
correct_coord as (
    select i.pid as ids from insurance i join coord_count c
    on  c.lat = i.lat and c.lon = i.lon
    where count = 1
),
tiv_2015_count as (
    select tiv_2015,count(*) as count from insurance
    group by tiv_2015
),
correct_tiv_2015 as (
    select i.pid as ids from insurance i join tiv_2015_count t
    on i.tiv_2015 = t.tiv_2015
    where t.count>1 
)
,solution_report as (
    select ids from correct_coord where ids in (select ids from correct_tiv_2015)
)
select round(sum(tiv_2016),2) as tiv_2016 
from insurance where pid in (select ids from solution_report); 