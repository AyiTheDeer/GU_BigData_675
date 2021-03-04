-- Агрегация данных
-- Task 1
select round(avg((to_days(now()) - to_days(birthday_at)) / 365), 0) as avg_age from users;