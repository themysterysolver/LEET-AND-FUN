# Write your MySQL query statement below
# Common expression table
with rating_cnt_cet as (
    select user_id,count(user_id) as cnt from movierating group by user_id
    order by cnt desc 
)
,highest_person_cet as (
    select u.name as results from users u join rating_cnt_cet r
    on u.user_id = r.user_id
    order by r.cnt desc,u.name asc
    limit 1
),avg_rating_cet as (
    select movie_id,avg(rating) as avg_rating_cet from movierating where DATE_FORMAT(created_at,'%Y-%m') = '2020-02'
    group by movie_id order by avg_rating_cet desc
),highest_average_cet as (
    select m.title as results from movies m join avg_rating_cet a 
    on m.movie_id = a.movie_id 
    order by a.avg_rating_cet desc,m.title asc
    limit 1 
)
SELECT * FROM highest_person_cet
UNION ALL
SELECT * FROM highest_average_cet;

