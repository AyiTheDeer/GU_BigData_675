-- Операторы
-- Task 2
alter table users 
	add created_at_new datetime,
	add updated_at_new datetime;
    
update users SET 
	created_at_new = str_to_date(created_at, '%d.%m.%Y %h:%m'),
    updated_at_new = str_to_date(updated_at, '%d.%m.%Y %h:%m');
    
alter table users
	drop created_at,
    drop updated_at,
    rename column created_at_new to created_at,
    rename column updated_at_new to updated_at;