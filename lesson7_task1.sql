/* Заполнил таблицу заказов подобными выражениями
INSERT INTO orders (id, user_id, created_at, updated_at) VALUES
  (1, (SELECT FLOOR(RAND()*(6-1+1))+1), now(), now());
*/

select * from users
where exists (select 1 from orders where user_id = users.id);