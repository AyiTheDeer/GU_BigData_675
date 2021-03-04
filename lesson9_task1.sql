/*
В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных.
Переместите запись id = 1 из таблицы shop.users в таблицу sample.users.
Используйте транзакции.
*/

START TRANSACTION;
insert into sample.users
select * from shop.users where shop.users.id = 1;
DELETE FROM shop.users WHERE shop.users.id = 1;
commit;