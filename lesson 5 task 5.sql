-- Агрегация данных
-- Task 2
select dayname(birthday_at) as weekday, count(*) as birthday_count from users group by weekday;