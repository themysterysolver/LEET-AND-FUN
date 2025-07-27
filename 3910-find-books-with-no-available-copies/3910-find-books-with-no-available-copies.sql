# Write your MySQL query statement below
# CET #thx sanjeev!
with count_null_cet as (
    select book_id,count(book_id) as count_null from borrowing_records
    where return_date is null group by book_id
)
select 
    l.book_id,l.title,l.author,l.genre,l.publication_year,c.count_null as current_borrowers
from 
    library_books l join count_null_cet c 
    on c.book_id = l.book_id where l.total_copies - c.count_null = 0
    order by current_borrowers desc,l.title asc