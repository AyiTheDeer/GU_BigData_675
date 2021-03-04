/*
Создайте двух пользователей которые имеют доступ к базе данных shop. 
Первому пользователю shop_read должны быть доступны только запросы на чтение данных,
второму пользователю shop — любые операции в пределах базы данных shop.
*/

create user shop_read identified by '123456';
grant select on shop.* to shop_read;

create user shop identified by '123456';
grant all on shop.* to shop;